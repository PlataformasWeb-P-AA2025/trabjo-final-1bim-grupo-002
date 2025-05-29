from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from generar_tablas import Reaccion
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Obtenemos el conteo de reacciones por tipo de emoción
resultados = session.query(Reaccion.tipo_emocion, func.count(Reaccion.tipo_emocion)).group_by(Reaccion.tipo_emocion).all()

print("Reporte de reacciones:")
for t, c in resultados: # Iteramos sobre los resultados
    print(f"- {t}: {c} veces")
    
# ALISrj & cbhas
