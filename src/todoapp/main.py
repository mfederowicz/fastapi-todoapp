from fastapi import FastAPI, Request, status
from pathlib import Path

from fastapi.responses import RedirectResponse
import todoapp.models
from todoapp.database import engine
from todoapp.routers import admin, auth, todos, users

from fastapi.staticfiles import StaticFiles

app = FastAPI()

todoapp.models.Base.metadata.create_all(bind=engine)

app.mount(
    "/static",
    StaticFiles(directory="assets/static"),
    name="static",
)


@app.get("/")
def test(request: Request):
    return RedirectResponse(url="/todos/todo-page", status_code=status.HTTP_302_FOUND)


@app.get("/healthy")
def health_check():
    return {"status": "Healthy"}


app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)
