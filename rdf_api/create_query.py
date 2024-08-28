from rdflib import Graph, URIRef, BNode, Literal
from rdflib import Namespace
from rdf_api.datastructure.triple_structure import Triple, TripleList




def check_graph_exist(graph_name: str):
    # check if graph exists (for now only in local directory)
    #   - later on extend to have list of paths + global directories
    
    try: 
        with open(f'graphs/{graph_name}.ttl', 'x') as graph: 
            graph.write("") # create an empty file to not interfere with later additions 
            print(f"The file '{graph_name}' has been created")
        # return True
    except FileExistsError: 
        print(f"The file '{graph_name}' already exists.")
        # return False
    

def process_new_nodes(graph_name:str, triples:TripleList):
    #create graph with the changes
    g = Graph()

    check_graph_exist(graph_name)
    g.parse(f'graphs/{graph_name}.ttl')

    for triple in triples.triples:
 
        s = Namespace(triple.sub_namespace)
        g.bind(triple.sub_namespace_prefix, s)
        o = Namespace(triple.obj_namespace)
        g.bind(triple.obj_namespace_prefix, o)

        sub = URIRef(f'{triple.sub_namespace}{triple.sub}')

        pred = URIRef(triple.pred)

        obj = URIRef(f'{triple.obj_namespace}{triple.obj}')

        g.add((sub,pred,obj))
        g.print()

    print(g.serialize(f'graphs/{graph_name}.ttl', format="turtle"))    
    return g

