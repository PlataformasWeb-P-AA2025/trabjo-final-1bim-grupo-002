from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from generar_tablas import Usuario, Publicacion, Reaccion
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

reaccion = session.query(Reaccion).join(Usuario).filter(Usuario.nombre.like("Justin")).all()

for r in reaccion:
    print(r)






