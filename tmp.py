from fastapi import FastAPI, APIRouter, BackgroundTasks
from fastapi.responses import JSONResponse
from fastapi import __version__ as version
import multiprocessing
import time

router = APIRouter()


def worker_function(s: str):
    while True:
        print(f"~~~ test_func: {s}")
        time.sleep(2)


def test_func(s: str):
    process = multiprocessing.Process(target=worker_function, args=(s,))
    # Para que el proceso se detenga cuando la aplicación principal se detenga
    process.daemon = True
    process.start()


@router.get("/test")
def get_test(background_tasks: BackgroundTasks) -> dict:
    background_tasks.add_task(test_func, "one")
    background_tasks.add_task(test_func, "two")
    background_tasks.add_task(test_func, "three")
    return {"message": "test"}


@router.get('/version')
def versions():
    return JSONResponse({"version": version})


app = FastAPI()
app.include_router(router)
