
.. image:: images/evil-world.png
    :align: right

==============================
Hola Mundo! - Sanitarium Inc.
==============================

**Hola Mundo** is a project that shows off the basic setting up of Python 3
project.


.. warning:: Rough Drafts and Secion collections.
    Here are the collection of topics that need to be curated into a usable
    form. But until enough documentation generated, and can decide how to
    organize, they will be collected below.

Publishing the Documentation
=============================

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
