from rdf_api.create_query import process_new_nodes,  check_graph_exist
from rdf_api.datastructure.triple_structure import TripleList, Triple

from rdflib.namespace import (FOAF, RDF, RDFS)
import pytest
from pytest import FixtureRequest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app

graph_name = "test"
graph_path = f'file://{graph_name}/' 
graph_path1 = f'file://{graph_name}1/' 
t1= Triple(
    sub = f'{graph_path}test',
    sub_is_literal=None,
    pred=RDF.type,
    obj= f'{graph_path1}test1',
    obj_is_literal=None
)
# assert t1.sub ==  

t2= Triple(
    sub = f'{graph_path}test2',
    sub_is_literal=None,
    pred=RDF.type,
    obj= f'{graph_path}test2',
    obj_is_literal=None
)

t3= Triple(
    sub = f"{graph_path}test",
    sub_is_literal=None,
    pred=FOAF.name,
    obj= f"{graph_path1}testname",
    obj_is_literal=None
)

t : list[Triple] = [t1,t2,t3]
ns = {"g" : graph_path, "g1": graph_path1}

triples = TripleList(triples=t, namespaces=ns)

# json = TripleList(triples=t, namespaces=ns).model_dump_json()

client = TestClient(app)


def get_token():
    token_headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    token_data = {
        'grant_type': 'password',
        'username': 'testUser',
        'password': 'hashedtest',
        'scope': '',
        'client_id': 'string',
        'client_secret': 'string',
    }

    r = client.post("/token/", data=token_data, headers=token_headers)
    
    return r.json()


def test_API_create_node_query():

    json = triples.model_dump_json()

    r_fail = client.post("/test/create_item/tests", content=json)

    assert r_fail.status_code != 200

    token = get_token()

    r = client.post("/test/create_item/tests", content=json, 
                      headers= {
                      "Authorization": f"Bearer {token}"
                      })
    assert r.status_code == 200
    assert r.json() == {"success": True}


def test_graph_exists():
    graph = check_graph_exist(graph_name, "tests")
    assert graph == True

    graph = check_graph_exist(f"{graph_name}1", "tests")
    assert graph == False


