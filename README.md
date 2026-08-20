# FastAPI - The Complete Course 2026 (Beginner + Advanced)

My simple todo app created while the [FastAPI - The Complete Course 2026 (Beginner + Advanced)](https://www.udemy.com/course/fastapi-the-complete-course/) course on Udemy.

## Basic setup and how to run:

 * uv - python package manager: https://docs.astral.sh/uv/getting-started/installation/ 
 * before start: `cp .env.dist .env` and modify `SQLALCHEMY_DATABASE_URL` and `SECRET_KEY` if you wish
 * launch: `make run`

## Run app uder console:
```console
make run
```
```console
uv run uvicorn todoapp.main:app --reload --host localhost --port 8000
INFO:     Will watch for changes in these directories: ['/home/projects/todoapp']
INFO:     Uvicorn running on http://localhost:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [657398] using StatReload
INFO:     Started server process [657400]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

