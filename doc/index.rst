
.. image:: images/evil-world.png
    :align: right

==============================
Hola Mundo! - Sanitarium Inc.
==============================

**Hola Mundo** is a project that shows off the basic setting up of Python 3
project.


.. warning:: Rough Drafts and Section collections.
    Here are the collection of topics that need to be curated into a usable
    form. But until enough documentation generated, and can decide how to
    organize, they will be collected below.


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

    #. Ensure that *python3* is installed. You can check by using the command:

        python3 --version

    #. Ensure that you have *virtualenv* installed. Check by using the command:

        virtualenv --version

Keep in mind that all scripts to be executed are assumed to be from the
project <root> directory. This is the directory with the *setup.py* file.

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
<root>/BUILD/CONVERAGE_REPORT/index.html.

Building Documentation
-----------------------

To run the documentation generation:

  > doc_build.sh

To view the documentation, open the file <root>/BUILD/doc/index.html.


=================
Of Documentation
=================

Setting up documentation for publication required:

    #. Selection of documentation markdown.
    #. Configuring the documentation generator.
    #. Selecting and deploying to a documentation site.

ReStructured Markdown and Usage
--------------------------------

.. warning:: Todo(raul).
    Add cruft about ReStructured text and where it is used in the project.

Documentation Generation via Sphinx
------------------------------------

.. warning:: Todo(raul).
    Add cruft about Sphinx. How is it used? Where does it run? Where is it
    configured?

Documentation Site and Deployment
----------------------------------

The selection for the documentation site was based purely for convenience.
Github Pages was selected, as a github account is at hand. For information on
the various means to publish to GithHub Pages, see `Github Pages Basics`_.

For simplicity to this project, the `Creating Project Pages manually`_ was
the selected method. No new account to setup, as a github account is
obviously at hand. To demonstrate all the steps for this project a setup
script and a deployment script are provided.

.. note:: Scripts must be executed in <root> dir, with development
    environment enabled.

The `git_pages_setup.sh`_ script provides the steps to setup the project git
repository for documentation deployment.

    (venv)root/> git_pages_set.sh

The `deploy_docs.sh`_ script provides the steps to deploy the project
documentation whenever it needs to be updated.

    (venv)root/> deploy_docs.sh

Upon successfully documentation deployment, you can view the changes by going
to the deployment url http://neoinsanity.github.io/hola_mundo/.

.. _Github Pages Basics: https://help.github.com/categories/github-pages-basics/
.. _Creating Project Pages manually: https://help.github.com/articles/creating-project-pages-manually/
.. _git_pages_setup.sh: https://github.com/neoinsanity/hola_mundo/blob/master/bin/git_pages_setup.sh
.. _deploy_docs.sh: https://github.com/neoinsanity/hola_mundo/blob/master/bin/deploy_docs.sh
