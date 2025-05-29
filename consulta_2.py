from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from generar_tablas import Usuario, Publicacion, Reaccion
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Pedimos la publicación por consola
mensaje_publicacion = input("Ingrese el mensaje de la publicacion: ")

# Buscamos la publicación en la base de datos
publicacion = session.query(Publicacion).filter_by(mensaje=mensaje_publicacion).first()

# Si la publicación existe, buscamos sus reacciones
if publicacion:
    reacciones = session.query(Reaccion).filter_by(publicacion_id=publicacion.id).all() # Obtenemos todas las reacciones de la publicación
    
    # Si la publicación tiene reacciones, las mostramos
    if reacciones:
        print(f"Reacciones de '{publicacion.mensaje}':")
        for r in reacciones: # Iteramos sobre las reacciones
            print(f"- {r.tipo_emocion}")
    # Si la publicación no tiene reacciones, mostramos un mensaje
    else:
        print("La publicación no tiene reacciones registradas.")
# Si la publicación no existe, mostramos un mensaje
else:
    print("Publicación no encontrada.")

# ALISrj & cbhas
