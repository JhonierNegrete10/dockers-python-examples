from fastapi import FastAPI, APIRouter, BackgroundTasks
from fastapi.responses import JSONResponse
from fastapi import __version__ as version
router = APIRouter()


def test_func(s: str) -> bool:

    print(f"~~~ test_func: {s}")
    return True


@router.get(
    "/test",
)
def get_test(background_tasks: BackgroundTasks) -> dict:
    # Only this task's output will be logged
    background_tasks.add_task(test_func, "one")
    background_tasks.add_task(test_func, "two")
    background_tasks.add_task(test_func, "three")
    return {"message": "test"}


@router.get('/version')
def versions():
    return JSONResponse({"version": version})


app = FastAPI()
app.include_router(router)
