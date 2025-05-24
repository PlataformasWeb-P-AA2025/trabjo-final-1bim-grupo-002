import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from generar_tablas import *
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

with open('data/usuarios_red_x.csv', newline='', encoding='utf-8') as f:
    lector = csv.reader(f, delimiter=';')
    next(lector)
    datos_usuarios = list(lector)
    for u in datos_usuarios:
        usuario = Usuario(nombre=u[0])
        session.add(usuario)

with open('data/usuarios_publicaciones.csv', newline='', encoding='utf-8') as f:
    lector = csv.reader(f, delimiter='|')
    next(lector)
    datos_usuarios_publicaciones = list(lector)

    for d in datos_usuarios_publicaciones:
        usuario = session.query(Usuario).filter_by(nombre=d[0]).one()
        publicacion = Publicacion(usuario_id=usuario.id, mensaje=d[1])
        session.add(publicacion)

with open('data/usuario_publicacion_emocion.csv', newline='', encoding='utf-8') as f:
    lector = csv.reader(f, delimiter='|')
    next(lector)
    datos_u_p_emocion = list(lector)
    print(len(datos_u_p_emocion))

    for d in datos_u_p_emocion:
        print(d)
        usuario = session.query(Usuario).filter_by(nombre=d[0]).one()
        publicacion = session.query(Publicacion).filter_by(mensaje=d[1]).one()
        reaccion = Reaccion(usuario_id=usuario.id, publicacion_id=publicacion.id, tipo_emocion=d[2])
        session.add(reaccion)

session.commit()
