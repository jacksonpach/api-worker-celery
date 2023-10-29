from fastapi import FastAPI
from app.worker import celery_worker
from app.worker import celery_app
from celery.result import AsyncResult

app = FastAPI()


@app.post("/send-task/")
def send_task(a: int, b: int):
    task = celery_worker.delay(a, b)
    return {"task_id": task.id}


@app.get("/task-status/{task_id}")
def get_status(task_id: str):
    task = AsyncResult(task_id, app=celery_app)

    if task.ready():
        return {"status": task.status, "result": task.result}
    else:
        return {"status": task.status, "message": "Task still processing."}
