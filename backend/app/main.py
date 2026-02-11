from fastapi import FastAPI
from app.schemas.cliente import ClienteBase
from app.schemas.producto import ProductoBase, ProductoCreate, ProductoResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "¡Bienvenido a Acali!"}

@app.post("/registro_producto")
async def registro_producto(producto: ProductoCreate):
    return ProductoCreate

