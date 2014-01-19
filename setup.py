"""The setuptools setup file.

"""

from setuptools import find_packages, setup

setup(
    name='hola_mundo',
    version='0.1.0',
    license='Apache License 2.0',
    description='This is the ultimate Hola Mundo',
    package=find_packages('hola_mundo'),
    install_requires=['PyYAML==3.10',],
    include_package_data = True,
)
