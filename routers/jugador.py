from fastapi import APIRouter, Request, Depends, Form, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlmodel import Session, select
from starlette.status import HTTP_303_SEE_OTHER
from models import Jugador, JugadorBase
from db import get_session
from typing import Optional


router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def listado_jugadores_html(request: Request, session: Session = Depends(get_session)):
    Jugador = session.exec(select(Jugador).where(Jugador.active == True)).all()
    return request.app.state.templates.TemplateResponse(
        "jugador_list.html",
        {"request": request, "jugadores": Jugador}
    )



@router.get("/new", response_class=HTMLResponse)
def formulario_nuevo_jugador(request: Request):
    return request.app.state.templates.TemplateResponse(
        "new_jugador.html",
        {"request": request}
    )


@router.post("/new")
async def crear_jugador(
    nombre: str = Form(...),
    dorsal: int = Form(""),
    peso: float = Form(""),
    altura: float= Form(...),
    session: Session = Depends(get_session)
):
    nuevo_jugador=Jugador(nombre=nombre, dorsal=dorsal,peso=peso,altura=altura, active=True)
    session.add(nuevo_jugador)
    session.commit()
    session.refresh(nuevo_jugador)

@router.get("/editar/{Jugador_id}", response_class=HTMLResponse)
def editar_jugador_form(jugador_id: int, request: Request, session: Session = Depends(get_session)):
    Jugador = session.get(Jugador, jugador_id)
    if not Jugador:
        return HTMLResponse("Jugador no encontrado", status_code=404)

    return request.app.state.templates.TemplateResponse(
        "jugador_edit.html",
        {"request": request, "Jugador": Jugador}
    )


@router.post("/editar/{Jugador_id}")
async def editar_jugador(
    dorsal: int,
    nombre: str = Form(...),
    altura: Optional[float] = Form(""),
    peso: Optional[float]= Form(""),
    pie_dominante: str = Form(""),
    goles: int = Form(...),
    session: Session = Depends(get_session)

):
    cliente = session.get(Jugador, Jugador_id)
    if not cliente:
        return HTMLResponse("Cliente no encontrado", status_code=404)

    Jugador.nombre = nombre
    Jugador.dorsal = dorsal
    Jugador.altura = altura
    Jugador.peso = peso
    Jugador.pie_dominante= pie_dominante
    Jugador.goles = goles




    session.add(cliente)
    session.commit()

    return RedirectResponse("/Jugador", status_code=HTTP_303_SEE_OTHER)




@router.get("/eliminar/{Jugador_id}")
def eliminar_Jugador(Jugador_id: int, session: Session = Depends(get_session)):
    Jugador = session.get(Jugador, Jugador_id)
    if Jugador:
        Jugador.active = False
        session.add(Jugador)
        session.commit()

    return RedirectResponse("/Jugador", status_code=HTTP_303_SEE_OTHER)



@router.get("/eliminados", response_class=HTMLResponse)
def eliminados(request: Request, session: Session = Depends(get_session)):
    Jugadores = session.exec(select(Jugador).where(Jugador.active == False)).all()

    return request.app.state.templates.TemplateResponse(
        "jugador_eliminados.html",
        {"request": request, "Jugadores": Jugadores}
    )



@router.get("/restaurar/{Jugador_id}")
def restaurar_cliente(cliente_id: int, session: Session = Depends(get_session)):
    cliente = session.get(Jugador, cliente_id)
    if cliente:
        cliente.active = True
        session.add(cliente)
        session.commit()

    return RedirectResponse("/jugadores/eliminados", status_code=HTTP_303_SEE_OTHER)