from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from generar_tablas import Usuario, Publicacion
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Obtenemos el conteo de publicaciones por usuario
conteo = session.query(Usuario.nombre, func.count(Publicacion.id)).join(Publicacion).group_by(Usuario.id).all()

# Si hay resultados, los mostramos
if conteo:
    print("Cantidad de publicaciones por usuario:")
    for n, t in conteo: # Iteramos sobre los resultados
        print(f"- {n}: {t}")
# Si no hay resultados, mostramos un mensaje
else:
    print("No hay publicaciones registradas.")

# ALISrj & cbhas
