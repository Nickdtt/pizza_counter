from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime
from database import Base

class Competicao(Base):
    __tablename__ = "competicoes"

    id = Column(Integer, primary_key=True, index=True)
    nome_competidor = Column(String, index=True)
    pizza_slices = Column(Integer)
    data = Column(DateTime, default= datetime.now(datetime.timezone.utc))