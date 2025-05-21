from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Base = declarative_base()


class Reaccion(Base):
    __tablename__ = 'reaccion'
    usuario_id = Column(Integer, ForeignKey('usuario.id'), primary_key=True)
    publicacion_id = Column(Integer, ForeignKey('publicacion.id'), primary_key=True)
    tipo_emocion = Column(String(50), nullable=False)
    publicacion = relationship("Publicacion", back_populates="usuarios")
    usuario = relationship("Usuario", back_populates="publicaciones")


class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    publicaciones = relationship("Reaccion", back_populates="usuario")


class Publicacion(Base):
    __tablename__ = 'publicacion'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    mensaje = Column(String(50))

    usuarios = relationship("Reaccion", back_populates="publicacion")


Base.metadata.create_all(engine)
