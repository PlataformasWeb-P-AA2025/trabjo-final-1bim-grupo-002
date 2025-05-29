# Información de la consulta de información

## Implementación de PostgreSQL junto con DOCKER

Para la implementación de PostreSQL con Docker, recurrimos a articulos web, 
El que usamos como base y guía fue el siguiente artículo: https://es.linux-console.net/?p=34617

En este árticulo, no se contemplaba la instalación de docker, asumía que ya estaba instalado y trabajaba directamente con docker compose. Para instalar Docker, reucurrimos a la documentación oficial de Docker.

## Uso de ChatGPT

A lo largo de la ejecución de las instrucciones mencionadas en el artículo anterior, nos topoamos con varios obstáculos, entonces recurrimos a Chat GPT, para solventar dudas y seguir con el proceso, los prompts usados son:

1. Tengo este artículo para levantar postgress en docker "https://es.linux-console.net/?p=34617", esto lo estoy usando para poder usar postgress en mi proyecto de python, estoy trabajando con el ORM SqlAlchemy, tengo un archivo llamado configuración, donde escribo la cadena de la conexión, para que luego SqlAlchemy pueda conectarse usando engine y create_engine.  Voy en la parte del artículo que dice: Paso 2: cree un archivo de redacción de Docker. Y tengo que crear un directorio y un archivo. Tengo dos preguntas: ¿El proceso que estoy usando es correcto? ¿El directorio y el archivo, debo crearlos en cualquier lado de mi computadora o dentro del proyecto?

### Comentario: 
Este prompt fue usado, para conocer si el proceso del artículo era correcto, y para conocer si el archivo .yml junto a la carpeta pg, se creaban dentro o fuera del proyecto, le brindamos todo el contexto posible, y nos explicó que esta carpera y el archivo se crean dentro del proyecto, para mayor portabilidad, ya que es el archivo de configuración es muy importante, si forma parte del proyecto, podemos clonarlo y leventarlo rápidamente si tenemos todos los requerimientos necesarios (docker y docker compose).

2. Estoy en el paso 3:  Paso 3: Ejecute PostgreSQL y pgAdmin como contenedores Docker tengo que ejecutar el siguiente comando "docker-compose up -d", mi archivo docker-compose-yaml, quedó así: [ archivo ] Pero me sale el siguiente error: unable to get image 'postgres': permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.49/images/postgres/json": dial unix /var/run/docker.sock: connect: permission denied

### Comentario: 
Este prompt fue usado para solucionar un error específico que salía al momento de querer levantar toda la configuración, se le proporcionó a ChatGPT el contexto del archivo, el cuál no creíamos que estaba mal, ya que la configuración usada en el .yaml la obtuvimos del artículo web. ChatGPT respondió, que este error ocurríá cuando docker estaba instalado y nusetro usuario no pertenecía al grupo "docker", indicó que la solución más directa era usar sudo en la instrucción.

3. Completé el Paso 4: conecte pgAdmin al contenedor PostgreSQL. Y todo parece estar funcionando correctamente. Ahora quiero usarlo. En mi archivo de configuracion.py tengo solo una linea: cadena_base_datos = 'sqlite:///futredx.db'  Y ahora debo cambiarla para apuntar a postgres.  ¿Cómo lo hago?  También agrego como uso esa variable en mi archivo generar_tablas.py: engine = create_engine(cadena_base_datos) Base = declarative_base() En este archivo hago todo el proceso de creación de las clases (tablas), para trabajar con el ORM

### Comentario:
Este prompt fue usado, para conocer cómo se escribía la ruta, para apuntar a la base de dato de Postgres, le pasamos el contexto de como veníamos trabajando con sqlite. Nos enseñó como se escribía la ruta y que información o valor iba en cada campo de la misma, nos indicó algunas variaciones de la ruta si nuestro proyecto estaba desplegado dentro del docker o en localhost y finalmente nos indicó, que dentro de las dependencias del proyecto, debíamos instalar un driver (psycopg2-binary), para que sqlAlchemy pueda comunicarse con postgreSQL