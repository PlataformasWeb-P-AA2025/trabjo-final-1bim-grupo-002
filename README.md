
# Mini Proyecto: FutRedX – La Red de Fútbol de la Premier League

# Proceso V1.0.0
1. Primero creamos el modelo para la base de datos, está conformado por tres tablas: Reaccion, Usuario, Publicacion. Además agregamos las relaciones correspondientes entre las tablas. Reaccion funciona como tabla intermedia entre Publicacion y Usuario, es decir esta tabla además de tener su valor `tipo_emocion` también tiene las primary keys de la tabla Publicación y Reacción, como foreign keys. Toda esta estructura la definimos en el archivo generar_tablas.py, el cual al ser ejecutado genera la base de datos con sus relacioes y atributos correspondientes.
2. Una vez hicimos el modelo, procedimos a insertar los datos dentro de la base de datos. primero leímos la información de los usuarios de `usuarios_red_x.csv` y poblamos la tabla de Usuarios, luego llenamos la tabla de Publicaciones, la cual está compuesta por el mensaje y el id del usuario que publicó. Por último para insertar los datos en la tabla Reaccion agregamos las foreigns keys correspondientes y el tipo de emocion. Todo esto en el archivo `generar_tablas.py`.

## Contexto

Un grupo de estudiantes apasionados por el fútbol ha creado *FutRedX*, una red social ficticia dedicada exclusivamente a compartir opiniones, noticias y momentos sobre la **Premier League inglesa**. Los usuarios pueden publicar frases, comentar eventos deportivos, y reaccionar a las publicaciones de otros.

La base de datos de esta red social está en desarrollo, y tú, como desarrollador/a, debes analizar los datos disponibles y modelar las clases necesarias para implementarla correctamente.

---

## Archivos entregados

1. `usuarios_red_x.csv`: contiene **100 usuarios únicos** registrados en la red FutRedX.
2. `usuarios_publicaciones.csv`: contiene **100 frases únicas** generadas por estos usuarios sobre la Premier League.
3. `usuario_publicacion_emocion.csv`: contiene las emociones de los usuarios para los comentarios.

---

## Solución

A partir del análisis de los datos y los requerimientos de la red FutRedX, se debe construir un modelo de base de datos con SQLAlchemy que represente adecuadamente el funcionamiento de esta red social. Realizar la migración de datos de los **csv** a la base de datos generada.

---

## Requisitos funcionales

1. Cada **usuario** puede hacer muchas publicaciones.
2. Cada **publicación** pertenece a un solo usuario.
3. Cada usuario puede **reaccionar a muchas publicaciones** (propias o ajenas).
4. Cada publicación puede recibir **reacciones de muchos usuarios**.
5. Solo se permite **una reacción por usuario en cada publicación**.
6. La reacción debe tener un campo `tipo de emocion`.

---

## Tareas a realizar
0. **Usar el número de archivos de python** que se crea necesario.

1. **Diseñar las clases con el ORM SQLAlchemy** necesarias:
   - `Usuario`
   - `Publicacion`
   - `Reaccion` (como tabla intermedia)

2. **Analizar e importar los archivos CSV**:
   - Crear instancias de usuarios, publicaciones y reacciones

3. **Realizar consultas ORM útiles**:
   - Listar publicaciones de un usuario.
   - Listar las reacciones a una publicación.
   - Mostrar en qué publicaciones reaccionó un usuario.
   - Obtener un reporte de reacciones en función del número de veces que fueron usadas.
   - Listar todas las reacciones de tipo "alegre", "enojado", "pensativo" que sean de usuarios que cuyos nombre no inicien con vocal.
   - Crear 5 consultas adicionales

Las consultas debe estar documentadas / comentadas en cada archivo

---

## Sugerencia de clases ORM

```python
class Usuario
class Publicacion
class Reaccion
```

---

## Referente a la base de datos

- Usar una base de datos SQLite.
- Usar una base de datos Postgres a través de Docker.
---

## En caso de usar IA-Generativa para consulta de información

- En un archivo llamado informacion.md; explicando a detalle el uso de cada prompt
