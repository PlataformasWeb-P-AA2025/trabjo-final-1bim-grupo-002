from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from generar_tablas import Usuario, Publicacion
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

conteo = session.query(Usuario.nombre, func.count(Publicacion.id)).join(Publicacion).group_by(Usuario.id).all()

print("Cantidad de publicaciones por usuario:")
for nombre, total in conteo:
    print(f"- {nombre}: {total}")

# ALISrj & cbhas
