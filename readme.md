API para gestionar acceso a un conjunto de aplicaciones y sus distintas partes. Permitiendo establecer distintos niveles de acceso por usuario-aplicación, independientemente de la parte de la aplicación. Permitiendo así que dos usuarios puedan acceder a la misma sección de una aplicación, pero con restricciones a la información según el nivel otorgado.
> Esta API se encuentra actualmente en desarrollo.

#### Ejecución de desarrollo

##### Variables de entorno

###### *On Linux*
# In te proyect directori

source venv/bin/activate

export FLASK_APP=entrypoint:app

export FLASK_DEBUG=True

export APP_SETTINGS_MODULE=config.postgres

python3 -m flask run --host 0.0.0.0

###### *On windows*

set FLASK_APP=entrypoint:app

set FLASK_DEBUG=True

set APP_SETTINGS_MODULE=config.default

