"""The module for executing the application.

"""
import sys
import el_grito
import el_mundo

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
        print 'Argument must be an integer.'
        sys.exit(-1)

# Print the message.
print grito.grito(index), mundo.mundo(index)
