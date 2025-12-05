from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from db import create_db_and_tables
from jugadores import router as jugador_router
from routers.estadisticas import router as estadistica_router

app = FastAPI(title="sigmotoa FC")

templates = Jinja2Templates(directory="templates")

app.state.templates = templates

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    print("Base de datos inicializada y servidor listo.")

app.include_router(jugador_router, prefix="/jugadores", tags=["Jugadores"])
app.include_router(estadistica_router, prefix="/estadisticas", tags=["Estadisticas"])

@app.get("/")
async def root():
    return {"message": "sigmotoa FC data"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Bienvenido a sigmotoa FC {name}"}


@app.get("/", response_class=HTMLResponse, tags=["Vistas HTML"])
def root(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "texto": "Bienvenido a la página de sigmota FC",
            "titulo_pagina": "Sigmotoa FC ⚽"
        }
    )