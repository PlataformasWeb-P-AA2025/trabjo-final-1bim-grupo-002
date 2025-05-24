from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from generar_tablas import Usuario, Publicacion
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

nombre_usuario = input("Ingrese el nombre del usuario: ")

usuario = session.query(Usuario).filter_by(nombre=nombre_usuario).first()

if usuario:
    publicaciones = session.query(Publicacion).filter_by(usuario_id=usuario.id).all()
    print(f"Publicaciones de {nombre_usuario}:")
    for p in publicaciones:
        print(f"- {p.mensaje}")
else:
    print("Usuario no encontrado")
