"""The setuptools setup file."""
from setuptools import setup

with open('README.md') as file:
    long_description = file.read()

with open('VERSION') as version_file:
    version = version_file.read().strip()

setup(
    name='hola_mundo',
    version=version,
    author='Raul Gonzalez',
    author_email='mindbender@gmail.com',
    url='https//github.com/neoinsanity/hola_mundo',
    license='Apache License 2.0',
    description='Hola Mundo!',
    long_description=long_description,
    packages=['hola_mundo', 'hola_mundo/util', ],
    install_requires=['PyYAML==3.11', ],
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',

    ]
)
