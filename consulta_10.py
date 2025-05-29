from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from generar_tablas import Usuario, Publicacion, Reaccion
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Obtenemos todas las reacciones, mediante la relación, usamos un JOIN para viajar a la tabla Usuario y obtenemos, todas las reacciones
# de algún usuario que en la estructura de su nombre se encuentre (in)
reaccion = session.query(Reaccion).join(Usuario).filter(Usuario.nombre.like("%in%")).all()

# Presentamos las reacciones
for r in reaccion:
    print(r)






