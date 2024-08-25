from rdflib import Graph, URIRef, BNode, Literal
from rdflib import Namespace
from rdflib.namespace import CSVW, DC, DCAT, DCTERMS, DOAP, FOAF, ODRL2, ORG, OWL, \
                           PROF, PROV, RDF, RDFS, SDO, SH, SKOS, SOSA, SSN, TIME, \
                           VOID, XMLNS, XSD
import requests
# from datastructure import Triple 
import json
from pydantic import BaseModel
class TestClass(BaseModel):
    jsonstring: str

def check_graph_exist(graph_name: str):
    # check if graph exists (for now only in local directory)
    #   - later on extend to have list of paths + global directories
    
    try: 
        with open(f'graphs/{graph_name}.ttl', 'x') as graph: 
            graph.write("") # create an empty file to not interfere with later additions 
            
        # return True
    except FileExistsError: 
        print(f"The file '{graph_name}' already exists.")
        # return False
    


#make use of rdflib to append to graph
def create_nodes(graph_name:str, graph:Graph):

    # added_graph = add_nodes(graph_name, triples)
    
    check_graph_exist(graph_name)
    g2 = Graph() 
    g2.parse(f'graphs/{graph_name}.ttl')
    
    g1 = graph.parse(format="turtle")

    g = graph + g2

    g.serialize(f'graphs/{graph_name}.ttl', format="turtle")




def add_nodes(graph_name:str):
    #create graph with the changes
    g1 = Graph()

        
    s = Namespace(f'{graph_name}.ttl/')
    g1.bind("s", s)

    g1.add((s.sub1, RDF.type ,s.obj1))

    print(g1.serialize(format="xml"))    


    # json = g1.serialize(format="xml")
    # testclass = TestClass(jsonstring=json)
    # jsondump = json.dumps(testclass, indent=2)
    # requests.post("http://0.0.0.0:8000/test/create_item", 
    #               json = jsondump, 
    #               headers = {
    #                 'Content-Type' : 'application/ld+json'
    #                 })

    # return g1


# print(create_graph("graphtest"))
# print(create_graph("test"))
# t : list[Triple] = [Triple(subject="test",predicate="test",object="test")]
# create_nodes("test",t)
add_nodes("test")
