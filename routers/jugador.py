from fastapi import APIRouter, Request, Depends, Form, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlmodel import Session, select
from starlette.status import HTTP_303_SEE_OTHER
from models import Jugador, JugadorBase
from db import get_session


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

@router.get("/editar/{Jugador_dorsal}", response_class=HTMLResponse)
def editar_jugador_form(jugador_dorsal: int, request: Request, session: Session = Depends(get_session)):
    Jugador = session.get(Jugador, jugador_dorsal)
    if not Jugador:
        return HTMLResponse("Jugador no encontrado", status_code=404)

    return request.app.state.templates.TemplateResponse(
        "jugador_edit.html",
        {"request": request, "Jugador": Jugador}
    )
