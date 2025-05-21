import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del
# archivo genera_tablas
from generar_tablas import *

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Leemos el txt con csv, con codificacion utf-8
with open('DATA/usuarios_red_x.csv', newline='', encoding='utf-8') as f:
    lector = csv.reader(f, delimiter=';')
    next(lector)
    datos_usuarios = list(lector)
    for u in datos_usuarios:
        usuario = Usuario(nombre=u[0])
        session.add(usuario)

with open('DATA/usuarios_publicaciones.csv', newline='', encoding='utf-8') as f:
    lector = csv.reader(f, delimiter='|')
    next(lector)
    datos_usuarios_publicaciones = list(lector)

    for d in datos_usuarios_publicaciones:
        usuario = session.query(Usuario).filter_by(nombre=d[0]).one()
        publicacion = Publicacion(usuario_id=usuario.id, mensaje=d[1])
        session.add(publicacion)

with open('DATA/usuario_publicacion_emocion.csv', newline='', encoding='utf-8') as f:
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
