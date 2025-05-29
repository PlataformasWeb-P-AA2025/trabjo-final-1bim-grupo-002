from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from generar_tablas import Usuario, Publicacion
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Pedimos el nombre del usuario por consola
nombre_usuario = input("Ingrese el nombre del usuario: ")

# Buscamos al usuario en la base de datos
usuario = session.query(Usuario).filter_by(nombre=nombre_usuario).first()

# Si el usuario existe, buscamos sus publicaciones
if usuario:
    publicaciones = session.query(Publicacion).filter_by(usuario_id=usuario.id).all() # Obtenemos todas las publicaciones del usuario
    
    # Si el usuario tiene publicaciones, las mostramos
    if publicaciones:
        print(f"\nPublicaciones de {usuario.nombre.title()}:")
        for p in publicaciones: # Iteramos sobre las publicaciones
            print(f"- {p.mensaje}")
    # Si el usuario no tiene publicaciones, mostramos un mensaje
    else:
        print("El usuario no tiene publicaciones registradas.")
# Si el usuario no existe, mostramos un mensaje
else:
    print("Usuario no encontrado.")

# ALISrj & cbhas
