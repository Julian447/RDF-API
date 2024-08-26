from rdflib import Graph, URIRef, BNode, Literal
from rdflib import Namespace
from rdflib.namespace import CSVW, DC, DCAT, DCTERMS, DOAP, FOAF, ODRL2, ORG, OWL, \
                           PROF, PROV, RDF, RDFS, SDO, SH, SKOS, SOSA, SSN, TIME, \
                           VOID, XMLNS, XSD, URIPattern
import os
import requests
# from datastructure import Triple 
import json
from pydantic import BaseModel


class Triple(BaseModel):
    sub:str 
    sub_namespace:str
    pred:str
    obj:str
    obj_namespace:str

class TripleList(BaseModel):
    triples:list[Triple]

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
    
    check_graph_exist(graph_name)

    g2 = Graph() 
    g2.parse(f'graphs/{graph_name}.ttl', format="turtle")
    
    # ensure format is correct
    g1 = graph.parse("graphs/tempgraph.ttl", format="turtle")
    
    # combine graphs
    g = g1 + g2

    os.remove("graphs/tempgraph.ttl")

    g.serialize(f'graphs/{graph_name}.ttl', format="turtle")




def process_new_nodes(graph_name:str, triples:TripleList):
    #create graph with the changes
    g = Graph()

    check_graph_exist(graph_name)
    g.parse(f'graphs/{graph_name}.ttl')

    for triple in triples.triples:
 
        s = Namespace(triple.sub_namespace)
        g.bind("s", s)

        sub = URIRef(f'{s}{triple.sub}')

        pred = URIRef(triple.pred)

        obj = URIRef(f'{s}{triple.obj}')

        g.add((sub,pred,obj))
        g.print()

    print(g.serialize(f'graphs/{graph_name}.ttl', format="turtle"))    
    return g





graph_name = "test"
t1= Triple(
    sub = "test",
    sub_namespace=f'file://{graph_name}.ttl/',
    pred=RDF.type,
    obj= "test",
    obj_namespace=f'{graph_name}.ttl/'
)

t2= Triple(
    sub = "test2",
    sub_namespace=f'file://{graph_name}.ttl/',
    pred=RDF.type,
    obj= "test2",
    obj_namespace=f'{graph_name}.ttl/'
)

t : list[Triple] = [t1,t2]


test = TripleList(triples=t)
g = process_new_nodes(graph_name, test)
# create_nodes(graph_name,g)
