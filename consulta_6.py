from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from generar_tablas import *
from configuracion import cadena_base_datos
from sqlalchemy import or_

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

usuarios = session.query(Usuario).filter(
    or_(
        Usuario.nombre.like("%al%"),
        Usuario.nombre.like("%el%"),
        Usuario.nombre.like("%il%"),
        Usuario.nombre.like("%ol%"),
        Usuario.nombre.like("%ul%"),
    )
)

for u in usuarios:
    print(u.nombre)
