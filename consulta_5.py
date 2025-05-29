from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_, and_
from generar_tablas import Reaccion, Usuario
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Obtenemos todas las reacciones, navegamos hasta la tabla de Usuario, mediante un JOIN, para poder filtrar por los nombres
# de los usuarios que no empiecen por vocal, y por los tipo de emociones específicos
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

# Imprimos las reacciones
for r in reacciones:
    print(r)

# ALISrj & cbhas
