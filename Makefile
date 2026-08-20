.PHONY: run dev install

include .env

run:
	uv run uvicorn todoapp.main:app --reload --host $(HOST) --port $(PORT)
test:
	uv run pytest

install:
	uv sync
