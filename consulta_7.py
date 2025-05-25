from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from generar_tablas import *
from configuracion import cadena_base_datos
from sqlalchemy import or_

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()
