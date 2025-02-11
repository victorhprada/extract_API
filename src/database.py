from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

# Criando a classe base para as entidades
Base = declarative_base()

class Bitcoin(Base):
    # Definindo o nome da tabela no banco de dados
    __tablename__ = 'bitcoin'

    # Definindo as colunas da tabela
    id = Column(Integer, primary_key=True, autoincrement=True)
    valor = Column(Float, nullable=False)
    cripto = Column(String, nullable=False)
    moeda = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False, default=datetime.now)
    