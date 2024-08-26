
import uvicorn
from fastapi import FastAPI
from read_query import run_query
from create_query import create_nodes, process_new_nodes

from rdflib import Graph
from pydantic import BaseModel

class Triple(BaseModel):
    sub:str
    pred:str
    obj:str
class TestClass(BaseModel):
    triples:list[Triple]


app = FastAPI()

@app.get("/")
async def test():
    query = """
        PREFIX txn: <http://example.org/data/transaction/> 
        PREFIX srv: <http://example.org/data/server/> 
        PREFIX log: <http://example.org/ont/transaction-log/> 
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 

        SELECT DISTINCT ?a ?b WHERE {
            ?a a ?b .
        }
        ORDER BY ?a
        LIMIT 3
        """

    res = run_query("graphtest", query)
    res.serialize(format="json")
    return res

# should this actually have endpoint?
@app.get("/create_graph/{graph_name}")
async def create_graph(graph_name: str):
    #should this even be an endpoint?
    return {"Graph": graph_name}

# should this actually have endpoint?
@app.post("/{graph_name}/create_item/")
async def create_item(graph_name : str, item_id : TestClass):
    graph = process_new_nodes("test")
    create_nodes(graph_name, graph)
    # return {"Hello": "World"}
    return True

@app.get("/get_graph/{graph_name}")
async def get_graph():
    return {"Hello": "World"}


#! Returns JSON format for every single answer
#!      Need to set up custom objects which return only desired output (i.e. subject predicate or object)
@app.get("/{graph_name}/get_item/{item_query}")
async def get_item(graph_name: str, item_query: str):

    return {"Hello": "World"}


@app.get("/get_item/{item_id}")
async def list_items():
    return {"Hello": "World"}

@app.get("/list_graphs")
async def list_graphs():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)




