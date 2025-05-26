from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from generar_tablas import Usuario
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

usuarios = session.query(Usuario).all()

print("Usuarios registrados:")
for u in usuarios:
    print(f"- {u.nombre}")

# ALISrj & cbhas
