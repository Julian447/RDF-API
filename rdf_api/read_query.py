import rdflib.graph 
from rdf_api.datastructure.query_structure import Query

# implement search through graph names
# keep a document with all paths of all graphs in use
def get_graph(graphname) :
    
    graph = rdflib.Graph()

    graph.parse(f'graphs/{graphname}.ttl', format="turtle")
    return graph.serialize()


#! change name later
def run_query(graphname, query : Query):

    graph = rdflib.Graph()

    graph.parse(f'graphs/{graphname}.ttl', format="turtle")

    qres = graph.query(query.query)

    return qres

