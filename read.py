import rdflib.graph

# implement search through graph names
# keep a document with all paths of all graphs in use
def get_graph(graphname) -> str :
    return "graphtest.ttl"


#! change name later
def run_query(graphname, query):

    graph = rdflib.Graph()

    graph.parse(get_graph(graphname), format="ttl")

    qres = graph.query(query)

    return qres


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

qres = run_query("test", query)


for row in qres:
    print(f"{row.a} is a transaction")

