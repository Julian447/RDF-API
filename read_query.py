import rdflib.graph 
import json

# implement search through graph names
# keep a document with all paths of all graphs in use
def get_graph(graphname) -> str :
    return "graphtest.ttl"


#! change name later
def run_query(graphname, query):

    graph = rdflib.Graph()

    graph.parse(get_graph(graphname))
    # v = graph.serialize(format="json-ld")

    qres = graph.query(query)

    return qres


query = """
    PREFIX txn: <http://example.org/data/transaction/> 
    PREFIX srv: <http://example.org/data/server/> 
    PREFIX log: <http://example.org/ont/transaction-log/> 
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 

    SELECT DISTINCT ?a ?b WHERE {
        ?a a ?b .
    }
    ORDER BY ?a
    LIMIT 3
    """

qres = run_query("test", query)


# for row in qres:
#     print(row)

print(qres.serialize(format="json"))

