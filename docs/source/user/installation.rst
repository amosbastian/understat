.. _installation:

Installing **understat**
========================

The recommended way to install ``understat`` is via ``pip``.

.. code-block:: bash

   pip install understat

.. note:: Depending on your system, you may need to use ``pip3`` to install
          packages for Python 3.

Updating **understat** with pip
-------------------------

To update **understat** you can run:

.. code-block:: bash

   pip install --upgrade understat

Example output:

.. code-block:: bash

    Installing collected packages: understat
      Found existing installation: understat 0.1.0
        Uninstalling understat-0.1.0:
          Successfully uninstalled understat-0.1.0
    Successfully installed understat-0.1.1

Installing older versions
-------------------------

Older versions of **understat** can be installed by specifying the version number
as part of the installation command:

.. code-block:: bash

   pip install understat==0.1.1

Installing from GitHub
----------------------

The source code for **understat** is available on GitHub repository
`<https://github.com/amosbastian/understat>`_. To install the most recent
version of **understat** from here you can use the following command::

    $ git clone git://github.com/amosbastian/understat.git

You can also install a `.tar file <https://github.com/requests/requests/tarball/master>`_
or `.zip file <https://github.com/requests/requests/tarball/master>`_

    $ curl -OL https://github.com/amosbastian/understat/tarball/master
    $ curl -OL https://github.com/amosbastian/understat/zipball/master # Windows

Once it has been downloaded you can easily install it using `pip`::

    $ cd understat
    $ pip install .
