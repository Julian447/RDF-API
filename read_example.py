
import rdflib.graph as g

graph = g.Graph()

graph.parse("graphtest.ttl", format="ttl")

query = """
    PREFIX txn: <http://example.org/data/transaction/> 
    PREFIX srv: <http://example.org/data/server/> 
    PREFIX log: <http://example.org/ont/transaction-log/> 
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 

    SELECT * WHERE {
        ?a a log:Transaction .
    }
    ORDER BY ?a
    LIMIT 3
    """

qres = graph.query(query)

for row in qres:
    print(f"{row.a} is a transaction")



