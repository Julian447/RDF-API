import requests
import rdflib
import requests
from rdflib import Graph, Literal, URIRef
from rdflib.namespace import (CSVW, DC, DCAT, DCTERMS, DOAP, FOAF, ODRL2, ORG,
                              OWL, PROF, PROV, RDF, RDFS, SDO, SH, SKOS, SOSA,
                              SSN, TIME, VOID, XMLNS, XSD, NamespaceManager,
                              URIPattern)

from main import create_item
from rdf_api.datastructure.query_structure import Query
from rdf_api.read_query import run_query
from rdf_api.create_query import process_new_nodes
from rdf_api.datastructure.triple_structure import Triple, TripleList


def get_token():
    token_headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    token_data = {
        'grant_type': 'password',
        'username': 'Nistec',
        'password': 'hashedtest',
        'scope': '',
        'client_id': 'string',
        'client_secret': 'string',
    }

    token_res = requests.post("http://0.0.0.0:5000/token", data=token_data, headers=token_headers)
    # print(token_res)
    # print(token_res.json())
    return token_res.json()["access_token"]


def add_item():
    graph_name = "test"
    graph_path = f'file://{graph_name}/' 
    graph_path1 = f'file://{graph_name}1/' 
    graph_path2 = f'file://{graph_name}2/' 
    t1= Triple(
        sub = f'{graph_path}test',
        sub_is_literal=None,
        pred=RDF.type,
        obj= f'{graph_path1}test1',
        obj_is_literal=None
    )

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

    t4= Triple(
        sub = f"{graph_path}test2",
        sub_is_literal=None,
        pred=FOAF.name,
        obj= f"{graph_path2}test2name",
        obj_is_literal=None
    )

    t : list[Triple] = [t1,t2,t3,t4]
    ns = {"g" : graph_path, "g1": graph_path1, "g2": graph_path2}

    json = TripleList(triples=t, namespaces=ns).model_dump_json()

    token = get_token()

    # print(test)
    # r = requests.post("http://0.0.0.0:5000/test/create_item", test)

    r = requests.post("http://0.0.0.0:5000/test/create_item/", data=json, 
                      headers= {
                      "Authorization": f"Bearer {token}"
                      })
    print(r)
    print(r.json())

def create_user():
    name = "Nistec"
    password = "hashedtest"
    hash = "hashed"
    
    usr_def = "file://users_definition.ttl/"
    usr = f"file://users.ttl/"

    a_user = Triple(
        sub = f'{usr}{name}',
        sub_is_literal=None,
        pred=RDF.type,
        obj= f'{usr_def}User',
        obj_is_literal=None
    )

    usrname = Triple(
        sub = f'{usr}{name}',
        sub_is_literal=None,
        pred=f"{usr_def}name",
        obj= name,
        obj_is_literal=XSD.string
    )

    passwd = Triple(
        sub = f'{usr}{name}',
        sub_is_literal=None,
        pred=f"{usr_def}password",
        obj= f'{password}',
        obj_is_literal=XSD.string
    ) 


    hashed = Triple(
        sub = f'{usr}{name}',
        sub_is_literal=None,
        pred=f"{usr_def}passwordHash",
        obj= f'{hash}',
        obj_is_literal=XSD.string
    )


    t : list[Triple] = [a_user,usrname,passwd,hashed]


    ns = {"usr" : usr_def, "": usr}
    # test = TripleList(triples=t).model_dump_json()
    triples = TripleList(triples=t,namespaces=ns)


    process_new_nodes(graph_name="users", triples=triples, graph_path="users")

def find_user(username:str):
    q = Query(
    query = """
        PREFIX usr: <file://users_definition/>
        PREFIX : <file://username.ttl/> 

        SELECT DISTINCT ?a ?c ?b WHERE {
            ?a ?c ?b .
        }
        """.replace("username", username)
    )

    res = run_query(graphname=f"{username}", query=q, graph_path="users")

    for row in res:
        print(f'Sub: {row.a} \nPred: {row.c} \nObj: {row.b} \n')
        print("\n")



def read_item():
    q = Query(
    query = """
        PREFIX txn: <http://example.org/data/transaction/> 
        PREFIX srv: <http://example.org/data/server/> 
        PREFIX log: <http://example.org/ont/transaction-log/> 
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 

        SELECT DISTINCT ?c ?b WHERE {
            ?a ?c ?b .
        }
        """.replace("?a", "txn:123")
    )

    json = q.model_dump_json()


    token = get_token()

    r = requests.post("http://0.0.0.0:5000/graphtest/get_item/", data=json, 
                      headers= {
                      "Authorization": f"Bearer {token}"
                      })
    print(r)
    print(r.json())


# read_item()
# add_item()
find_user("Nistec")
# create_user()
