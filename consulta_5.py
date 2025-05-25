from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_, and_
from generar_tablas import Reaccion, Usuario
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

reacciones = (session.query(Reaccion)
              .join(Usuario)
              .filter(
    and_(
        ~or_(Usuario.nombre.startswith("A"),
             Usuario.nombre.startswith("E"),
             Usuario.nombre.startswith("I"),
             Usuario.nombre.startswith("O"),
             Usuario.nombre.startswith("U")),
        or_(
            Reaccion.tipo_emocion == "alegre",
            Reaccion.tipo_emocion == "enojado",
            Reaccion.tipo_emocion == "pensativoS"
        )

    )

).all())

for r in reacciones:
    print(r)

# ALISrj & cbhas
