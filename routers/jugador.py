from fastapi import APIRouter, Request, Depends, Form, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlmodel import Session, select
from starlette.status import HTTP_303_SEE_OTHER
from models import Jugador


router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def listado_jugadores_html(request: Request, session: Session = Depends(get_session)):
    Jugador = session.exec(select(Jugador).where(Jugador.active == True)).all()
    return request.app.state.templates.TemplateResponse(
        "jugador_list.html",
        {"request": request, "jugadadores": jugadores}
    )



@router.get("/new", response_class=HTMLResponse)
def formulario_nuevo_cliente(request: Request):
    return request.app.state.templates.TemplateResponse(
        "new_cliente.html",
        {"request": request}
    )