===========
Hola Mundo
===========

Project Purpose
================
This project demonstrates how to get an open source python project actually 
open sourced. This means getting:

    - Getting the source control.
    - Getting a dev environment.
    - Getting test and coverage.
    - Getting the documentation.
    - Publishing to Pypi.
    - Publishing the docs.
 
If you care to jump straight to the dry explanations of how *Hola Mundo* 
configuration can help as examples for getting an open source Pypi project, then
generate the help documentation, and it will guide you across the various 
ways that *Hola Mundo* comes together to be open source worthy.

What follows is *Hola Mundo* the App!

share and enjoy


=================
Hola Mundo 0.0.2
=================

Hola Munda Usage
=================

*Hola Mundo* makes it easy for you to internationalize your greetings.

The execution of *Hola Mundo* can be accomplished with:

    > python -m hola_mundo.main <index>

    or
    
    > python hola_mundo/main.py <index>
    
    :index: An optional integer that will display `Hola Mundo` in a given
        language. If not provided, then a random version of `Hola Mundo` will
        be provided.


Documentation
--------------

For the latest documentation, visit http://neoinsanity.github.io/hola_mundo/

====================
Project Development
====================

If you are interested in developing **Hola Mundo** code, utilize the helper 
scripts in the *hola_mundo/bin* directory. Just follow the instruction below 
for setting up the 

Get the Source First!
----------------------

The latest stable release source of **Hola Mundo** can be found on the
at https://github.com/neoinsanity/hola_mundo. 

Run the Dev Environment Setup
------------------------------

Prior to running the dev setup scripts:

    1. Ensure that *python3* is installed. You can check by using the command:
    
        python3 --version
    
    2. Ensure that you have *virtualenv* installed. You can check by using the
     command:
     
        virtualenv --version
    
Keep in mind that all scripts to be executed are assumed to be from the 
project `root` directory. This is the directory with the *setup.py* file.

Once you have the pre-requisites out of the way, we can run the development 
configuration scripts.


Prep the development environment with the command:

  > bin/dev_setup.sh

This command will setup the virtualenv for the project in the  directory 
*/venv*. It will also install the **Hola Mundo** in a develop mode,  with the
creation of a development egg file.

The Development Environment Usage
==================================

In this section will be demonstrated the dev tools available for a session of
source development. This features enabling the dev environment, executing the
unit test with coverage, and building the docs.

Enable the Development Environment
-----------------------------------

This command MUST be executed at the beginning of each developer session. It 
will ensure that the dev tools are available, and that the virtual 
environment is active.

The command is given below, note that it is sourced to set virtualenv:

  > . bin/enable_dev.sh
  
or

  > source bin/enable_dev.sh
  
Enabling the dev environment adds the *bin* directory scripts to environment 
*PATH*. This allows for the commands below to be typed at the prompt from the
project <root>. 

Running Tests and Code Coverage
--------------------------------

To run the unit tests:

  > run_tests.sh

To view the code coverage report, open the file 
`root`/BUILD/CONVERAGE_REPORT/index.html.

Building Documentation
-----------------------

To run the documentation generation:

  > doc_build.sh

To view the documentation, open the file `root`/BUILD/doc/index.html.
