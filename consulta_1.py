from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from generar_tablas import Usuario, Publicacion
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Pedimos el nombre del usuario por consola
nombre_usuario = input("Ingrese el nombre del usuario: ")

publicaciones = session.query(Publicacion).join(Usuario).filter(Usuario.nombre == nombre_usuario).all()

if publicaciones:
    for p in publicaciones:
        print(p)


# ALISrj & cbhas
