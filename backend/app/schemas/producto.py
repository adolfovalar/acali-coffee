from pydantic import BaseModel

class ProductoBase(BaseModel):
    nombre: str
    precio: float
    descripcion: str | None = None # Esto hace que la descripción sea opcional. 

class ProductoCreate(ProductoBase):
    pass

class ProductoResponse(ProductoBase):
    id: int

class Config:
    from_attributes = True #Esto es importante para que funcione con SQLAlchemy





