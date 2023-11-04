import asyncio

from fastapi import FastAPI
from fastapi import __version__ as version
from fastapi.responses import JSONResponse

app = FastAPI()


async def productor(queue):
    for i in range(1, 6):
        await asyncio.sleep(1)  # Simula la generación de un dato
        dato = f"Dato {i}"
        await queue.put(dato)
        print(f"Productor: Generado {dato}")


async def consumidor(queue):
    while True:
        dato = await queue.get()
        print(f"Consumidor: Recibido {dato}")
        # Aquí puedes manipular el dato como desees


queue = asyncio.Queue()


@app.post("/start")
async def iniciar_procesos():
    # Inicia los procesos productor y consumidor
    asyncio.create_task(productor(queue))
    asyncio.create_task(consumidor(queue))

    # Devuelve una respuesta indicando que los procesos se han iniciado
    return {"mensaje": "Procesos iniciados"}


@app.get("/version")
def versions():
    return JSONResponse({"version": version})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
