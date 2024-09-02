
import requests
from rdflib.namespace import (CSVW, DC, DCAT, DCTERMS, DOAP, FOAF, ODRL2, ORG,
                              OWL, PROF, PROV, RDF, RDFS, SDO, SH, SKOS, SOSA,
                              SSN, TIME, VOID, XMLNS, XSD, URIPattern)

from rdf_api.datastructure.triple_structure import Triple, TripleList

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


# t1= Triple(
#     sub = "test",
#     sub_namespace=f'file://{graph_name}.ttl/',
#     sub_namespace_prefix="s",
#     pred=FOAF.name,
#     obj= "testname",
#     obj_namespace=f'file://{graph_name}1.ttl/',
#     obj_namespace_prefix="o"
# )
#
# t2= Triple(
#     sub = "test2",
#     sub_namespace=f'file://{graph_name}.ttl/',
#     sub_namespace_prefix="s",
#     pred=FOAF.name,
#     obj= "test2name",
#     obj_namespace=f'file://{graph_name}2.ttl/',
#     obj_namespace_prefix="o"
# )




t : list[Triple] = [t1,t2]


test = TripleList(triples=t).model_dump_json()


# print(test)

print(test)
r = requests.post("http://0.0.0.0:5000/test/create_item", test)
print(r)



