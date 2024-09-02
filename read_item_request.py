import requests

from rdf_api.datastructure.query_structure import Query
from rdf_api.read_query import run_query

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
print(token_res)
print(token_res.json())
token = token_res.json()["access_token"]

r = requests.post("http://0.0.0.0:5000/graphtest/get_item/", data=json, 
                  headers= {
                  "Authorization": f"Bearer {token}"
                  })
print(r)
print(r.json())



