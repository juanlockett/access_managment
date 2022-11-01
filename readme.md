Ejecución de desarrollo
=======================
variables de entorno:
=====
*On Linux*
export FLASK_APP=entrypoint:app
export FLASK_DEBUG=True
export APP_SETTINGS_MODULE=config.default
*On windows*
set FLASK_APP=entrypoint:app
set FLASK_ENV=development
set APP_SETTINGS_MODULE=config.default