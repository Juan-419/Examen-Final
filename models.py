from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import date


class JugadorBase(SQLModel):
    nombre: Optional[str]=None
    altura: Optional[float]=None
    peso: Optional[str]=None
    pie_dominante: Optional[str]=None
    tiempo_cancha: Optional[str]=None
    goles: Optional[str]=None
    faltas: Optional[str]=None
    

class Jugador(JugadorBase, table=True):
    dorsal:Optional[str]=None
    active: bool = Field(default=True)
    goles: Optional[str]=None
    altura = Optional[float]=None
    pie_dominante = optional[str]=None


class Estadistica():
    pass


class Partido():


/////




class ClienteBase(SQLModel):
    nombre: Optional[str] = None
    telefono: Optional[str] = None
    correo: Optional[str] = None
    anio: Optional[int] = None


class Cliente(ClienteBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    img: Optional[str] = None
    active: bool = Field(default=True)

    carros: List["Carro"] = Relationship(back_populates="cliente")


class CarroBase(SQLModel):
    marca: Optional[str] = None
    modelo: Optional[int] = None
    anio: Optional[int] = None
    placa: Optional[str] = None


class Carro(CarroBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    cliente_id: Optional[int] = Field(default=None, foreign_key="cliente.id", nullable=True)
    active: bool = Field(default=True)

    cliente: Optional[Cliente] = Relationship(back_populates="carros")
    soat: Optional["SOAT"] = Relationship(back_populates="carro", sa_relationship_kwargs={"uselist": False})
    reparaciones: List["Reparacion"] = Relationship(back_populates="carro")


class SOATBase(SQLModel):
    numero: Optional[str] = None
    fecha_vigencia: Optional[date] = None


class SOAT(SOATBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    carro_id: Optional[int] = Field(default=None, foreign_key="carro.id", unique=True, nullable=True)
    carro: Optional[Carro] = Relationship(back_populates="soat")

class SOATCreate(SOATBase):
    carro_id: int



class MecanicoBase(SQLModel):
    nombre: Optional[str] = None
    especialidad: Optional[str] = None


class Mecanico(MecanicoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    active: bool = Field(default=True)
    reparaciones: List["Reparacion"] = Relationship(back_populates="mecanicos", link_model=ReparacionMecanicoLink)


class ReparacionBase(SQLModel):
    descripcion: Optional[str] = None
    fecha: Optional[date] = None
    costo: Optional[float] = None


class ReparacionCreate(ReparacionBase):
    carro_id: int
    mecanico_ids: Optional[List[int]] = []


class Reparacion(ReparacionBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    carro_id: Optional[int] = Field(default=None, foreign_key="carro.id")
    active: bool = Field(default=True)

    carro: Optional[Carro] = Relationship(back_populates="reparaciones")
    mecanicos: List[Mecanico] = Relationship(
        back_populates="reparaciones",
        link_model=ReparacionMecanicoLink
    )