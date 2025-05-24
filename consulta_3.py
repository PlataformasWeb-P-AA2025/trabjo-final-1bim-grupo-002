from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from generar_tablas import Usuario, Reaccion
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

nombre_usuario = input("Ingrese el nombre del usuario: ")

usuario = session.query(Usuario).filter_by(nombre=nombre_usuario).first()

if usuario:
    reacciones = session.query(Reaccion).filter_by(usuario_id=usuario.id).all()
    if reacciones:
        print(f"\n{nombre_usuario} reaccionó en las siguientes publicaciones:")
        for r in reacciones:
            print(f"- {r.publicacion.mensaje}")
    else:
        print(f"{nombre_usuario} no ha reaccionado en ninguna publicación.")
else:
    print("Usuario no encontrado")
    
# ALISrj & cbhas
