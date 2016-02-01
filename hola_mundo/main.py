#!/usr/bin/env python

"""A command line tool for internationalizing `Hola Mundo`.

Hola Mundo Usage
=================

*Hola Mundo* makes it easy for you to internationalize your greetings.

The execution of *Hola Mundo* can be accomplished with::

    > python -m hola_mundo.main <index>

    or

    > python hola_mundo/main.py <index>

    :index: An optional integer that will display `Hola Mundo` in a given
        language. If not provided, then a random version of `Hola Mundo` will
        be provided.
"""
import sys
from hola_mundo import el_grito
from hola_mundo import el_mundo

if __name__ == '__main__':
    # Initialize the translation resources.
    grito = el_grito.ElGrito()
    mundo = el_mundo.ElMundo()

    # Configure the input options.
    args = sys.argv
    index = None
    if len(args) > 1:
        if args[1].isdigit():
            index = int(args[1])
        else:
            print('Argument must be an integer.')
            sys.exit(-1)

    # Print the message.
    print(grito.grito(index), mundo.mundo(index))
