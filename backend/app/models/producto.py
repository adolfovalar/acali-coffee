from sqlalchemy import Column, Integer, String, Float
from app.db.base import Base

class Producto(Base): #Necesita heredar de Base para que SQLAlchemy transforme esta clase en una tabla de base de datos. 
    __tablename__ = "productos" #Esta será la tabla de Postgres

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True, nullable=False)
    precio = Column(Float, nullable=False)
    descripcion = Column(String, nullable=True)