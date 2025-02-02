from rdf_api.create_query import process_new_nodes,  check_graph_exist
from rdf_api.datastructure.triple_structure import TripleList, Triple
from rdf_api.datastructure.query_structure import Query
from rdf_api.read_query import get_graph, run_query

from rdflib.namespace import (FOAF, RDF, RDFS, XSD)
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
t1_read = Query(
query = """
    PREFIX t1: <t1_path>
    PREFIX t2: <t2_path> 
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 

    SELECT * WHERE {
        t1:test a t2:test1 
    }
    """.replace("t1_path", graph_path).replace("t2_path", graph_path1)
)

t2= Triple(
    sub = f'{graph_path}test2',
    sub_is_literal=None,
    pred=RDF.type,
    obj= f'{graph_path}test2',
    obj_is_literal=None
)
t2_read = Query(
query = """
    PREFIX t1: <t1_path>
    PREFIX t2: <t2_path> 
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 

    SELECT * WHERE {
        t1:test2 a t1:test2 
    }
    """.replace("t1_path", graph_path).replace("t2_path", graph_path1)
)

t3= Triple(
    sub = f"{graph_path}test",
    sub_is_literal=None,
    pred=FOAF.name,
    obj= f"{graph_path1}testname",
    obj_is_literal=XSD.string
)
t3_read = Query(
query = """
    PREFIX t1: <t1_path>
    PREFIX t2: <t2_path> 
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 

    SELECT * WHERE {
        t1:test xsd:string t2:testname 
    }
    """.replace("t1_path", graph_path).replace("t2_path", graph_path1)
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

def test_API_read_query():

    json = triples.model_dump_json()

    # r_fail = client.post("/test/create_item/tests", content=json)
    #
    # assert r_fail.status_code != 200
    #
    token = get_token()

    r = client.post("/test/create_item/tests", content=json, 
                      headers= {
                      "Authorization": f"Bearer {token}"
                      })
    res = run_query(graphname="test",query=t1_read,graph_path="tests")
    print(res)
    # assert 
    # assert r.status_code == 200
    # assert r.json() == {"success": True}
test_API_read_query()

def test_graph_exists():
    graph = check_graph_exist(graph_name, "tests")
    assert graph == True

    graph = check_graph_exist(f"{graph_name}1", "tests")
    assert graph == False


