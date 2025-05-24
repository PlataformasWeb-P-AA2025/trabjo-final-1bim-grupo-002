from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from generar_tablas import Usuario, Publicacion, Reaccion
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

mensaje_publicacion = input("Ingrese el mensaje de la publicacion: ")

publicacion = session.query(Publicacion).filter_by(mensaje=mensaje_publicacion).first()

if publicacion:
    reacciones = session.query(Reaccion).filter_by(publicacion_id=publicacion.id).all()
    print(f"Reacciones de {mensaje_publicacion}:")
    for r in reacciones:
        print(f"- {r.tipo_emocion}")
else:
    print("Publicacion no encontrada")
