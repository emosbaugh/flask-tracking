try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='flask_tracking',
      version='1.0',
      py_modules=['flask_tracking'],
      install_requires=['Flask', 'mongoengine'],
      )
