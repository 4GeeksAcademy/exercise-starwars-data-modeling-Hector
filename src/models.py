import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)

    

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    population = Column(Integer, nullable=False)
    terrain = Column(String(250), nullable=False)
    diameter = Column(Integer, nullable=False)

class Starship(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    cost_in_credits = Column(Integer, nullable=False)

class LightSaber(Base):
    __tablename__ = 'lightsaber'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    color = Column(String(250), nullable=False)
    crystal = Column(String(250), nullable=False)

class Jedi(Base):
    __tablename__ = 'jedi'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    species = Column(String(250), nullable=False)

class Sith(Base):
    __tablename__ = 'sith'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    species = Column(String(250), nullable=False)
    


    
    
    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
