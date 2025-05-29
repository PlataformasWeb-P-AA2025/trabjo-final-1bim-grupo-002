from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from generar_tablas import Usuario, Publicacion
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Pedimos el nombre del usuario por consola
nombre_usuario = input("Ingrese el nombre del usuario: ")

# Consultamos las publicaciones del usuario que coincida con el nombre
publicaciones = session.query(Publicacion).join(Usuario).filter(Usuario.nombre == nombre_usuario).all()

# Si hay publicaciones, las mostramos
if publicaciones:
    for p in publicaciones: # Iteramos sobre las publicaciones
        print(p)
# Si no hay publicaciones, informamos al usuario
else:
    print(f"No se encontraron publicaciones para el usuario '{nombre_usuario}'.")


# ALISrj & cbhas
