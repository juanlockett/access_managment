Ejecución de desarrollo
=======================
variables de entorno:
=====
*On Linux*
export FLASK_APP=entrypoint:app
export FLASK_ENV=development
export APP_SETTINGS_MODULE=config.development
*On windows*
set FLASK_APP=entrypoint:app
set FLASK_ENV=development
set APP_SETTINGS_MODULE=config.development