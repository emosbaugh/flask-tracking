try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='flask_tracking',
      version='1.0',
      packages=['flask_tracking'],
      install_requires=['Flask', 'mongoengine'],
      )
