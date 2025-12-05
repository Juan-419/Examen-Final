from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class JugadorBase(SQLModel):
    nombre: Optional[str]=None
    altura: Optional[str]=None
    peso: Optional[str]=None
    pie_dominante: Optional[str]=None
    tiempo_cancha: Optional[str]=None
    goles: Optional[str]=None
    faltas: Optional[str]=None
    

class Jugador(JugadorBase, table=True):
    dorsal:Optional[str]=None
    active: bool = Field(default=True)
    estadisticas:

class Estadistica():
    pass


class Partido():
    pass

