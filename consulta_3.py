from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from generar_tablas import Usuario, Reaccion
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

nombre_usuario = input("Ingrese el nombre del usuario: ")

usuario = session.query(Usuario).filter_by(nombre=nombre_usuario).first()

# Si el usuario existe, buscamos sus reacciones
if usuario:
    reacciones = session.query(Reaccion).filter_by(usuario_id=usuario.id).all() # Obtenemos todas las reacciones que hizo el usuario
    
    # Si el usuario tiene reacciones, las mostramos
    if reacciones:
        print(f"\n{usuario.nombre} reaccionó en las siguientes publicaciones:")
        for r in reacciones: # Iteramos sobre las reacciones
            print(f"- {r.publicacion.mensaje} ({r.tipo_emocion})")
    # Si el usuario no tiene reacciones, mostramos un mensaje
    else:
        print(f"{usuario.nombre} no ha reaccionado en ninguna publicación.")
# Si el usuario no existe, mostramos un mensaje
else:
    print("Usuario no encontrado.")
    
# ALISrj & cbhas
