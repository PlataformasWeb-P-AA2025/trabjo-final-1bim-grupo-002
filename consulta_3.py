from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from generar_tablas import *
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Mostrar en qué publicaciones reaccionó un usuario.
nombre_usuario = input("Ingrese el nombre del usuario: ")

publicaciones = session.query(Publicacion).join(Reaccion).join(Usuario).filter(Usuario.nombre == nombre_usuario).all()

for publicacion in publicaciones:
    print(publicacion)


# ALISrj & cbhas
