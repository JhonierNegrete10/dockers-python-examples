from fastapi import FastAPI, APIRouter, BackgroundTasks
from fastapi.responses import JSONResponse
from fastapi import __version__ as version
from multiprocessing import Queue, Process
import time

router = APIRouter()


def worker_function(s, input_queue: Queue, output_queue: Queue):
    while not input_queue.empty():
        # Espera a que llegue un valor desde el proceso anterior
        received_s = input_queue.get_nowait()
        result_s = f"{received_s} -> {s}"
        print(f"~~~ test_func: {result_s}")
        output_queue.put_nowait(result_s)  # Pasa el valor al siguiente proceso
        time.sleep(2)


def test_func(s):
    input_queue = Queue()
    output_queue = Queue()
    process = Process(
        target=worker_function, args=(s, input_queue, output_queue))
    process.daemon = True
    process.start()
    return input_queue, output_queue


@router.get("/test")
def get_test(background_tasks: BackgroundTasks) -> dict:
    input_queue1, output_queue1 = test_func("one")
    input_queue2, output_queue2 = test_func("two")
    input_queue3, output_queue3 = test_func("three")

    input_queue1.put_nowait("start")  # Inicia el proceso inicial

    # Agrega un último elemento a la cola para que el último proceso imprima y termine
    background_tasks.add_task(lambda: input_queue3.put_nowait("stop"))

    return {"message": "test"}


@router.get('/version')
def versions():
    return JSONResponse({"version": version})


app = FastAPI()
app.include_router(router)
