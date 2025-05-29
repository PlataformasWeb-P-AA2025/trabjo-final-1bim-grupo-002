from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from generar_tablas import Usuario
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)   
Session = sessionmaker(bind=engine)
session = Session()

# Obtenemos todos los usuarios registrados
usuarios = session.query(Usuario).all()

# Si hay usuarios, los mostramos
if usuarios:
    print("Usuarios registrados:")
    for u in usuarios: # Iteramos sobre los usuarios
        print(f"- {u.nombre}")
# Si no hay usuarios, mostramos un mensaje
else:
    print("No hay usuarios registrados.")

# ALISrj & cbhas
