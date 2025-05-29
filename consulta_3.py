from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from generar_tablas import *
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Mostrar en qué publicaciones reaccionó un usuario.
nombre_usuario = input("Ingrese el nombre del usuario: ")

# Consultamos las publicaciones en las que el usuario ha reaccionado
publicaciones = session.query(Publicacion).join(Reaccion).join(Usuario).filter(Usuario.nombre == nombre_usuario).all()

# Si hay publicaciones, las mostramos
if publicaciones:
    print(f"Publicaciones en las que el usuario '{nombre_usuario}' ha reaccionado:")
    for p in publicaciones: # Iteramos sobre las publicaciones
        print(p)
else:
    print(f"No se encontraron publicaciones en las que el usuario '{nombre_usuario}' haya reaccionado.")

# ALISrj & cbhas
