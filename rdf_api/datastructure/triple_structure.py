from pydantic import BaseModel


class Triple(BaseModel):
    sub:str 
    sub_is_literal:str|None
    pred:str
    obj:str
    obj_is_literal:str|None

class TripleList(BaseModel):
    triples:list[Triple]
    namespaces:dict[str,str] = {}



