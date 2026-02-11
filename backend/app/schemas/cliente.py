from pydantic import BaseModel

class ClienteBase (BaseModel):
    nombre: str
    telefono: str

class ClienteCreate (ClienteBase):
    password: str



