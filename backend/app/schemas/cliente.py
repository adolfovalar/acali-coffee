from pydantic import BaseModel

class Cliente (BaseModel):
    nombre: str
    telefono: str
    