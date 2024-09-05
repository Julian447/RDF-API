from rdflib import BNode, Graph, Literal, Namespace, URIRef

from rdf_api.datastructure.triple_structure import Triple, TripleList


def check_graph_exist(graph_name: str, graph_path:str):
    # check if graph exists (for now only in local directory)
    #   - later on extend to have list of paths + global directories
    #   - later make able to create directories if not exists
    
    try: 
        with open(f'{graph_path}/{graph_name}.ttl', 'x') as graph: 
            graph.write("") # create an empty file to not interfere with later additions 
            print(f"The file '{graph_name}' has been created")
    except FileExistsError: 
        print(f"The file '{graph_name}' already exists.")
    

def process_new_nodes(graph_name:str, triples:TripleList, graph_path:str = "graphs"):
    #create graph with the changes
    g = Graph(bind_namespaces="rdflib")

    check_graph_exist(graph_name, graph_path)
    g.parse(f'{graph_path}/{graph_name}.ttl')
    
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
    
    g.serialize(f'{graph_path}/{graph_name}.ttl', format="turtle")
    return g

