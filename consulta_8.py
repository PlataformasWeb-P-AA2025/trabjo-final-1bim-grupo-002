from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from generar_tablas import Publicacion
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

palabra = input("Ingrese palabra clave para buscar en publicaciones: ")

publicaciones = session.query(Publicacion).filter(Publicacion.mensaje.like(f"%{palabra}%")).all()

print("Publicaciones encontradas:")
for p in publicaciones:
    print(f"- {p.mensaje}")

# ALISrj & cbhas
