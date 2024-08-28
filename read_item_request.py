import requests
from rdf_api.read_query import run_query
from rdf_api.datastructure.query_structure import Query 

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
# print(q.query)

# res = run_query("graphtest", query)
# r = res.serialize()

# print(r)
# print(res.serialize(format="json"))

# for row in res:
#     print(f"Sub: txn:123 \nPred: {row.c}\nObj: {row.b}")
#     print("\n")
# print(q.model_dump())

json = q.model_dump_json()
print(json)
# print(f"\n{Query.model_validate_json(json)}")

r = requests.post("http://0.0.0.0:8000/graphtest/get_item/", json)
print(r)




