from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from generar_tablas import *
from configuracion import cadena_base_datos
from sqlalchemy import or_

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Obtenemos todos los usuarios
usuarios = session.query(Usuario).filter(
    # Usamos una sentencia or_, para obtener usuarios que tengan diferentes tipos de combinaciones dentro de su nombre,
    # en este caso todo usuario que en su nombre tenga la combinacion (al, el il, ol, ul)
    or_(
        Usuario.nombre.like("%al%"),
        Usuario.nombre.like("%el%"),
        Usuario.nombre.like("%il%"),
        Usuario.nombre.like("%ol%"),
        Usuario.nombre.like("%ul%"),
    )
)

# Por cada usuario mostramos su nombre
for u in usuarios:
    print(u.nombre)
