# TinyApp API

A small FastAPI + PostgreSQL app, containerized with Docker Compose, built as a hands-on project for learning container orchestration.

## Stack
- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker Compose

## Running locally

1. Copy `.env.example` to `.env` and fill in your own values
2. `docker compose up --build`
3. Visit `http://localhost:8000/docs` for the interactive API

## Endpoints
- `POST /add_user` — create a user
- `GET /users` — list all users
- `GET /users/{id}` — get a specific user