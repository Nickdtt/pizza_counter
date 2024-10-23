from pydantic import BaseModel

class Save_Competition(BaseModel):
    nome_competidor: str
    pizza_slices: str


    