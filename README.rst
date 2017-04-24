===============================
full async web app example
===============================


.. image:: https://img.shields.io/pypi/v/full_async_web_app_example.svg
        :target: https://pypi.python.org/pypi/full_async_web_app_example

.. image:: https://img.shields.io/travis/beetleman/full_async_web_app_example.svg
        :target: https://travis-ci.org/beetleman/full_async_web_app_example

.. image:: https://readthedocs.org/projects/full-async-web-app-example/badge/?version=latest
        :target: https://full-async-web-app-example.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/beetleman/full_async_web_app_example/shield.svg
     :target: https://pyup.io/repos/github/beetleman/full_async_web_app_example/
     :alt: Updates


Example


* Free software: MIT license
* Documentation: https://full-async-web-app-example.readthedocs.io.

Migrations
----------

* create:
.. code-block:: bash
   docker-compose exec app bash migrate_create.sh migration-name

* run migration
.. code-block:: bash
   docker-compose exec app bash migrate_run.sh

Features
--------

* TODO

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
