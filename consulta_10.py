from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from generar_tablas import Usuario, Publicacion, Reaccion
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Obtenemos todos los usuarios
usuarios = session.query(Usuario).all()

# Presentamos los usuarios y el número de reacciones por cada uno, gracias a la relación del ORM, entre reacciones y usuario
# podemos obtener toda la lista de reacciones, y en este caso, aplicamos len, para contarlas.
for u in usuarios:
    print(f"Usuario: {u.nombre} - Número de reacciones: {len(u.reacciones)}")






