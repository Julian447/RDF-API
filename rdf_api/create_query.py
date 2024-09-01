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
    g = Graph(bind_namespaces="rdflib")

    check_graph_exist(graph_name)
    g.parse(f'graphs/{graph_name}.ttl')
    
    # make sure all needed namespaces are present
    for prefix in triples.namespaces.keys():
        g.bind(prefix=prefix,namespace=triples.namespaces[prefix])
    
    for triple in triples.triples:
 
        if triple.sub_is_literal:
            sub = Literal(triple.sub, datatype=triple.obj_is_literal)
        else:
            sub = URIRef(f'{triple.sub}')

        pred = URIRef(triple.pred)
        
        if triple.obj_is_literal:
            obj = Literal(triple.obj, datatype=triple.obj_is_literal)
        else:
            obj = URIRef(f'{triple.obj}')

        g.add((sub,pred,obj))
        g.print()

    print(g.serialize(f'graphs/{graph_name}.ttl', format="turtle"))    
    return g

