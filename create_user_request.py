
from rdflib import Graph, Literal, URIRef
import rdflib
from rdflib.namespace import CSVW, DC, DCAT, DCTERMS, DOAP, FOAF, ODRL2, ORG, OWL, \
                           PROF, PROV, RDF, RDFS, SDO, SH, SKOS, SOSA, SSN, TIME, \
                           VOID, XMLNS, XSD, NamespaceManager, URIPattern
import requests
from rdf_api.datastructure.triple_structure import TripleList, Triple
from rdf_api.create_query import process_new_nodes


usr = "file://users.ttl/"

name = "Nistec"
password = "hashedtest"
hash = "hashed"

a_user = Triple(
    sub = f'{usr}{name}',
    sub_is_literal=None,
    pred=RDF.type,
    obj= f'{usr}User',
    obj_is_literal=None
)

usrname = Triple(
    sub = f'{usr}{name}',
    sub_is_literal=None,
    pred="file://users.ttl/name",
    obj= name,
    obj_is_literal=XSD.string
)

passwd = Triple(
    sub = f'{usr}{name}',
    sub_is_literal=None,
    pred="file://users.ttl/password",
    obj= f'{password}',
    obj_is_literal=XSD.string
) 


hashed = Triple(
    sub = f'{usr}{name}',
    sub_is_literal=None,
    pred="file://users.ttl/passwordHash",
    obj= f'{hash}',
    obj_is_literal=XSD.string
)


t : list[Triple] = [a_user,usrname,passwd,hashed]


ns = {"usr" : "file://users.ttl/"}
# test = TripleList(triples=t).model_dump_json()
test = TripleList(triples=t,namespaces=ns)


# print(test)

# url = f'http://0.0.0.0:5000/{name}/create_item'
# r = requests.post(url, test)
# print(r)
process_new_nodes("users", test)


