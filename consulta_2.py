from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from generar_tablas import Usuario, Publicacion, Reaccion
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Pedimos la publicación por consola
mensaje_publicacion = input("Ingrese el mensaje de la publicacion: ")

# Consultamos las reacciones a la publicación que coincida con el mensaje
reacciones = session.query(Reaccion).join(Publicacion).filter(Publicacion.mensaje == mensaje_publicacion).all()

# Si hay reacciones, las mostramos
if reacciones:
    for r in reacciones: # Iteramos sobre las reacciones
        print(r)
# Si no hay reacciones, informamos al usuario
else:
    print(f"No se encontraron reacciones para la publicación '{mensaje_publicacion}'.")
# ALISrj & cbhas
