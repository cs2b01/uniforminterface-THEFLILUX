from sqlalchemy import Column, Integer, String, Sequence, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import connector

class Usuario(connector.Manager.Base):
    __tablename__ = 'usuario'
    usuario_id = Column(Integer, Sequence('usuario_id_seq'), primary_key=True)
    nombre = Column(String(50))
    codigo = Column(String(12))
    password = Column(String(120))
