import os
from dotenv import dotenv_values
from rdflib import Literal
from rdflib.namespace import XSD
import uvicorn
from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import PlainTextResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from rdf_api.read_query import run_query, get_graph
from rdf_api.create_query import process_new_nodes
from rdf_api.datastructure.triple_structure import TripleList, Triple
from rdf_api.datastructure.query_structure import Query
from auth import Authentication
from pydantic import BaseModel

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


auth = Authentication(dotenv_values(".env"))




@app.get("/", response_class=PlainTextResponse)
async def test():
    return "This is an api for querying rdf databases"

@app.post("/{graph_name}/create_item/")
async def create_item(graph_name : str, item: TripleList):
    process_new_nodes(graph_name, item)
    # return {"Hello": "World"}
    return True

@app.get("/get_graph/{graph_name}", response_class=PlainTextResponse)
async def get_static_graph(graph_name : str):
    return get_graph(graph_name)


#! Returns JSON format for every single answer
#!      Need to set up custom objects which return only desired output (i.e. subject predicate or object)
@app.post("/{graph_name}/get_item/")
async def get_item(graph_name: str, query : Query):
    # auth.auth(token)
    res = run_query(graph_name, query)
    # print(res.serialize(format="json"))
    return res

@app.get("/list_graphs")
async def list_graphs():
    return {"Hello": "World"}


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    username: str
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str
u = UserInDB(username="Nistec", hashed_password="hashedtest")


@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    data = UserInDB(username=form_data.username, hashed_password=form_data.password)
    q = Query(
    query = """

        PREFIX usr: <file://users.ttl/> 
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 

        SELECT * WHERE {
            usr:username a usr:User ;
                usr:name ?usrname ;
                usr:password ?passwd
        }
        """.replace("username", data.username)
    )
    print(q.query)
    res = run_query("users",q)

    res_usr = UserInDB(username="", hashed_password="")
    for row in res:
        print(f'Login attempt from User: {row.usrname}')
        res_usr = UserInDB(username=row.usrname, hashed_password=row.passwd)

    if not (data == res_usr):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    # token = auth.encode_token(res_usr.username)
    return {"access_token": res_usr.username, "token_type": "bearer"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)


