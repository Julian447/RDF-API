
from rdflib import Graph, Literal
from rdflib.namespace import CSVW, DC, DCAT, DCTERMS, DOAP, FOAF, ODRL2, ORG, OWL, \
                           PROF, PROV, RDF, RDFS, SDO, SH, SKOS, SOSA, SSN, TIME, \
                           VOID, XMLNS, XSD, URIPattern
import requests
from rdf_api.datastructure.triple_structure import TripleList, Triple
from rdf_api.read_query import run_query
from rdf_api.datastructure.query_structure import Query 


q = Query(
query = """

    PREFIX usr: <file://users.ttl/> 

    SELECT DISTINCT ?c ?b WHERE {
        usr:Nistec ?c ?b .
    }
    """
)

res = run_query("users", q)

for row in res:
    print(f'Sub: usr:Nistec \nPred: {row.c} \nObj: {row.b} \n')
    print("\n")





