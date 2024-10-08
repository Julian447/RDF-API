from typing import Annotated

import uvicorn
from dotenv import dotenv_values
from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import PlainTextResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from auth import Authentication
from rdf_api.create_query import process_new_nodes
from rdf_api.datastructure.query_structure import Query
from rdf_api.datastructure.triple_structure import TripleList
from rdf_api.datastructure.user_structure import User, UserInDB
from rdf_api.read_query import get_graph, run_query

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

env = dotenv_values(".env")

auth = Authentication(env)




@app.get("/", response_class=PlainTextResponse)
async def test():
    return "This is an api for querying rdf databases"

@app.post("/{graph_name}/create_item/")
async def create_item(graph_name : str, item: TripleList, token: Annotated[str, Depends(oauth2_scheme)]):
    # use token for user group authentication
    process_new_nodes(graph_name, item)
    return True

@app.get("/get_graph/{graph_name}", response_class=PlainTextResponse)
async def get_static_graph(graph_name : str, token: Annotated[str, Depends(oauth2_scheme)]):
    # use token for user group authentication
    return get_graph(graph_name)


#! Returns JSON format for every single answer
#!      Need to set up custom objects which return only desired output (i.e. subject predicate or object)
@app.post("/{graph_name}/get_item/")
async def get_item(graph_name: str, query : Query, token: Annotated[str, Depends(oauth2_scheme)]):
    # use token for user group authentication
    # auth.auth(token)
    res = run_query(graph_name, query)
    # print(res.serialize(format="json"))
    return res

@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    # add usergroup to token
    data = UserInDB(username=form_data.username, hashed_password=form_data.password)
    res_usr = get_user(form_data.username)

    if not (data == res_usr):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    token = auth.encode_token(res_usr.username)
    return {"access_token": token, "token_type": "bearer"}


def get_user(username: str) -> UserInDB:
    q = Query(
    query = """
        PREFIX : <file://users.ttl/>
        PREFIX usr: <file://users_definition.ttl/> 
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 

        SELECT * WHERE {
            :username a usr:User ;
                usr:name ?usrname ;
                usr:password ?passwd
        }
        """.replace("username", username)
    )
    res = run_query(graphname="users",query=q,graph_path="users")
    
    # define response user
    res_usr = UserInDB(username="", hashed_password="")
    for row in res:
        print(f'Login attempt from User: {row.usrname}')
        res_usr = UserInDB(username=row.usrname, hashed_password=row.passwd)
    
    return res_usr




if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)


