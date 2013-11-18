try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='googleplay-api',
      version='0.1',
      packages=['googleplay_api'],
      install_requires=['protobuf'],
      )
