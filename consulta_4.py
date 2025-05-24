from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from generar_tablas import Reaccion
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

resultados = session.query(Reaccion.tipo_emocion, func.count(Reaccion.tipo_emocion)).group_by(Reaccion.tipo_emocion).all()

print("Reporte de reacciones:")
for t, c in resultados:
    print(f"- {t}: {c} veces")
