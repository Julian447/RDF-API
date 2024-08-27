from pydantic import BaseModel


class Triple(BaseModel):
    sub:str 
    sub_namespace:str
    sub_namespace_prefix:str
    pred:str
    obj:str
    obj_namespace:str
    obj_namespace_prefix:str

class TripleList(BaseModel):
    triples:list[Triple]



