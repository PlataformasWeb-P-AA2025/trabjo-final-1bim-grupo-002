from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from generar_tablas import Publicacion
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Pedimos la palabra clave por consola
palabra = input("Ingrese palabra clave para buscar en publicaciones: ")

# Buscamos las publicaciones que contengan la palabra clave
publicaciones = session.query(Publicacion).filter(Publicacion.mensaje.like(f"%{palabra}%")).all()

# Si se encontraron publicaciones, las mostramos
if publicaciones:
    print("Publicaciones encontradas:")
    for p in publicaciones: # Iteramos sobre las publicaciones encontradas
        print(f"- {p.mensaje}")
# Si no se encontraron publicaciones, mostramos un mensaje
else:
    print("No se encontraron publicaciones con esa palabra.")
    
# ALISrj & cbhas
