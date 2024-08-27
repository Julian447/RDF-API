
from rdflib import Graph, URIRef, BNode, Literal
from rdflib import Namespace
from rdflib.namespace import CSVW, DC, DCAT, DCTERMS, DOAP, FOAF, ODRL2, ORG, OWL, \
                           PROF, PROV, RDF, RDFS, SDO, SH, SKOS, SOSA, SSN, TIME, \
                           VOID, XMLNS, XSD, URIPattern
import requests
from pydantic import BaseModel
from rdf_api.datastructure.triple_structure import TripleList, Triple






graph_name = "test"
# t1= Triple(
#     sub = "test",
#     sub_namespace=f'file://{graph_name}.ttl/',
#     sub_namespace_prefix="s",
#     pred=RDF.type,
#     obj= "test2",
#     obj_namespace=f'file://{graph_name}1.ttl/',
#     obj_namespace_prefix="o"
# )
#
# t2= Triple(
#     sub = "test2",
#     sub_namespace=f'file://{graph_name}.ttl/',
#     sub_namespace_prefix="s",
#     pred=RDF.type,
#     obj= "test2",
#     obj_namespace=f'file://{graph_name}2.ttl/',
#     obj_namespace_prefix="o"
# )


t1= Triple(
    sub = "test",
    sub_namespace=f'file://{graph_name}.ttl/',
    sub_namespace_prefix="s",
    pred=FOAF.name,
    obj= "testname",
    obj_namespace=f'file://{graph_name}1.ttl/',
    obj_namespace_prefix="o"
)

t2= Triple(
    sub = "test2",
    sub_namespace=f'file://{graph_name}.ttl/',
    sub_namespace_prefix="s",
    pred=FOAF.name,
    obj= "test2name",
    obj_namespace=f'file://{graph_name}2.ttl/',
    obj_namespace_prefix="o"
)




t : list[Triple] = [t1,t2]


test = TripleList(triples=t).model_dump_json()


# print(test)


r = requests.post("http://0.0.0.0:8000/test/create_item", test)
print(r)



