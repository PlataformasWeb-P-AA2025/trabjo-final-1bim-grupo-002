import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from generar_tablas import *
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Cargamos los usuarios
with open('data/usuarios_red_x.csv', newline='', encoding='utf-8') as f:
    lector = csv.reader(f, delimiter=';')
    next(lector)  # Saltamos el encabezado
    datos_usuarios = list(lector)

    for u in datos_usuarios:
        usuario = Usuario(nombre=u[0])  # Creamos usuario con su nombre
        session.add(usuario)  # Lo añadimos a la sesión

# Cargamos las publicaciones de los usuarios
with open('data/usuarios_publicaciones.csv', newline='', encoding='utf-8') as f:
    lector = csv.reader(f, delimiter='|')
    next(lector)  # Saltamos encabezado
    datos_usuarios_publicaciones = list(lector)

    for d in datos_usuarios_publicaciones:
        usuario = session.query(Usuario).filter_by(nombre=d[0]).one()  # Buscamos el usuario por su nombre
        publicacion = Publicacion(usuario_id=usuario.id, mensaje=d[1])  # Creamos publicación con el mensaje
        session.add(publicacion)  # Añadimos a la sesión

# Cargamos las reacciones de los usuarios a las publicaciones
with open('data/usuario_publicacion_emocion.csv', newline='', encoding='utf-8') as f:
    lector = csv.reader(f, delimiter='|')
    next(lector)
    datos_u_p_emocion = list(lector)
    print(len(datos_u_p_emocion))  # Mostramos cuántas reacciones hay

    for d in datos_u_p_emocion:
        print(d)  # Imprimimos los datos para ver que se está cargando
        usuario = session.query(Usuario).filter_by(nombre=d[0]).one()  # Buscamos usuario
        publicacion = session.query(Publicacion).filter_by(mensaje=d[1]).one()  # Buscamos publicación
        reaccion = Reaccion(usuario_id=usuario.id, publicacion_id=publicacion.id, tipo_emocion=d[2])  # Creamos reacción
        session.add(reaccion)  # Añadimos a la sesión

# Guardamos todo en la base de datos
session.commit()

# ALISrj & cbhas
