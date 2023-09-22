from fastapi import FastAPI, APIRouter, BackgroundTasks
from fastapi.responses import JSONResponse
from fastapi import __version__ as version
import multiprocessing
import time

router = APIRouter()


def worker_function(s: str, conn):
    while True:
        print(f"~~~ test_func: {s}")
        time.sleep(2)
        conn.send(f"Message from {s}")  # Envía un mensaje al otro proceso
        conn.recv()  # Espera a recibir una respuesta


def test_func(s: str):
    parent_conn, child_conn = multiprocessing.Pipe()
    process = multiprocessing.Process(
        target=worker_function, args=(s, child_conn))
    process.daemon = True
    process.start()
    return parent_conn


@router.get("/test")
def get_test(background_tasks: BackgroundTasks) -> dict:
    conn_one = test_func("one")
    conn_two = test_func("two")
    conn_three = test_func("three")

    # Enviar un mensaje desde el proceso three al proceso two
    conn_three.send("Message from three to two")

    # Esperar a recibir un mensaje en el proceso two
    message = conn_two.recv()
    print(f"Received in process two: {message}")

    # Cerrar las conexiones
    conn_one.close()
    conn_two.close()
    conn_three.close()

    return {"message": "test"}


@router.get('/version')
def versions():
    return JSONResponse({"version": version})


app = FastAPI()
app.include_router(router)
