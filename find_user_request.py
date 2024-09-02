
import requests

from rdf_api.datastructure.query_structure import Query
from rdf_api.datastructure.triple_structure import Triple, TripleList
from rdf_api.read_query import run_query

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





