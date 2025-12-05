from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from utils.positions import Position
from utils.states import States

class JugadorEstadisticasLink(SQLModel, table=True):
    jugador_dorsal: Optional[int] = Field(default=None, foreign_key="jugador.dorsal", primary_key=True)
    estadistica_id: Optional[int] = Field(default=None, foreign_key="estadistica.id", primary_key=True)

class JugadorPosicionLink(SQLModel, table=True):
    jugador_dorsal: Optional[int] = Field(default=None, foreign_key="jugador.dorsal", primary_key=True)
    posicion: Optional[int] = Field(default=None, foreign_key="position.", primary_key=True)

class JugadorBase(SQLModel):
    nombre: Optional[str]=None
    altura: Optional[str]=None
    peso: Optional[str]=None
    año_nacimiento: Optional[str]=None
    pie_dominante: Optional[str]=None
    tiempo_cancha: Optional[str]=None
    goles: Optional[str]=None
    faltas: Optional[str]=None
    

class Jugador(JugadorBase, table=True):
    dorsal:Optional[str]=None
    active: bool = Field(default=True)
    estadisticas: List[Estadistica] = Relationship(back_populates="jugador", link_model=JugadorEstadisticasLink)
    posición: List[]=

class EstadisticaBase(SQLModel):
   tiempo:


class Estadistica(EstadisticaBase, table=True):
    pass


class Partido():
    pass

