"""The setuptools setup file.

"""

from setuptools import setup

setup(
    name='hola_mundo',
    version='0.1.0',
    license='Apache License 2.0',
    description='This is the ultamite Hola Mundo',
    package=['hola_mundo'],
    install_requires=['PyYAML==3.10',],
)
