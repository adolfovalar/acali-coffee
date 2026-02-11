from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "¡Bienvenido a Acali!"}

@app.post("/registro_cliente")
async def registro_cliente():
    pass

@app.put("/actualizar_cliente")
async def actualizar_cliente():
    pass

@app.get("/clientes")
async def mostrar_clientes():
    pass

@app.get("/clientes/{id_cliente}")
async def mostrar_cliente(id_cliente: int):
    pass

