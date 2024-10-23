from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class Partida(Base):
    __tablename__ = "partidas"

    id = Column(Integer, primary_key=True, index=True)
    nome_competicao = Column(String, index=True)
    data = Column(DateTime, default= datetime.now(datetime.timezone.utc))
    competidores = relationship("Competidor", back_populates="partida")

class Competidor(Base):
    __tablename__= "competidores"

    id = Column(Integer, primary_key=True, index=True)
    nome_competidor = Column(String, index = True)
    slices = Column(Integer, default=0)
    competition_id = Column(Integer, ForeignKey("competicao.id"))
    partida = relationship("Partida", back_populates="competidores")
