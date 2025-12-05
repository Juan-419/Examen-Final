from fastapi import APIRouter, Request, Depends, Form, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlmodel import Session, select
from starlette.status import HTTP_303_SEE_OTHER
from db import get_session
from models import Jugador
from supa.supabase_upload import upload_to_bucket

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def listado_jugadores_html(request: Request, session: Session = Depends(get_session)):
    clientes = session.exec(select(Jugador).where(Jugador.active == True)).all()
    return request.app.state.templates.TemplateResponse(
        "cliente_list.html",
        {"request": request, "clientes": clientes}
    )