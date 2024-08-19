
import uvicorn
from fastapi import FastAPI

app = FastAPI()


# should this actually have endpoint?
@app.get("/create_graph/{graph_name}")
async def create_graph():
    return {"Hello": "World"}

# should this actually have endpoint?
@app.get("/{graph_name}/create_item/{item_id}")
async def create_item():
    return {"Hello": "World"}

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




