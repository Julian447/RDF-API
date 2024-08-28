
import uvicorn
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from rdf_api.read_query import run_query, get_graph
from rdf_api.create_query import process_new_nodes

from rdf_api.datastructure.triple_structure import TripleList, Triple
from rdf_api.datastructure.query_structure import Query



app = FastAPI()

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
    res = run_query(graph_name, query)
    # print(res.serialize(format="json"))
    return res

@app.get("/list_graphs")
async def list_graphs():
    return {"Hello": "World"}



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)




