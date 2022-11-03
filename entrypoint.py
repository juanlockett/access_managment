import os
import unittest

from app import create_app


settings_module = os.getenv('APP_SETTINGS_MODULE')
app = create_app(settings_module)


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')