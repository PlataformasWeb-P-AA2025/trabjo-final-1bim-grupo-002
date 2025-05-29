from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from generar_tablas import Usuario, Publicacion, Reaccion
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Pedimos la publicación por consola
mensaje_publicacion = input("Ingrese el mensaje de la publicacion: ")

reacciones = session.query(Reaccion).join(Publicacion).filter(Publicacion.mensaje == mensaje_publicacion).all()

if reacciones:
    for r in reacciones:
        print(r)

# ALISrj & cbhas
