Copycheck
=========

Copyright 2016 Janus Friis Nielsen.

This file is part of *copycheck*.

.. image:: https://circleci.com/gh/janusdn/copycheck/tree/master.svg?style=shield&circle-token=4112427381753afc2f073a61fba23263d1f86d13
    :target: https://circleci.com/gh/janusdn/copycheck/tree/master


Introduction
------------
*Copycheck* inspects the beginning of all files reports any file without a copyright
header.

The recognition of copyright headers is very rudimentary. *Copycheck* scans the 
10 first lines for occurrences of the word "copyright" in any casing.


Installation
------------

*copycheck* is available for install through `PyPI`_:

.. code-block:: bash

  $ pip install copycheck

*copycheck* can also be installed from source with:

.. code-block:: bash

  $ python setup.py install

.. _`PyPI`: http://pypi.python.org/pypi/copycheck
.. _`setuptools`: https://pypi.python.org/pypi/setuptools


Usage
-----

The tool will show a description of usage when given the 
`--help` option:

.. code-block:: bash
    
    $ copycheck --help

      usage: copycheck [-h] [-v] [--debug DEBUG] {check} ...

      Check source files for missing copyright headers

      positional arguments:
        {check}        sub-commands
          check        check for missing copyright headers

      optional arguments:
        -h, --help     show this help message and exit
        -v, --verbose  Enable verbose output
        --debug DEBUG  Enable debug output

Check all files in current directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    $ copycheck check .


Check all files in a directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    $ copycheck check path/to/directory


Check all files in a number of directories
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    $ copycheck check path/to/directory path/to/another/directory /and/so/on/..


Ignore files
~~~~~~~~~~~~

You can put a files called `.copycheckignore` in the base directory of your 
project.

The syntax of the files is Git wildmatch. The same as used in .gitignore.


Get files sorted
~~~~~~~~~~~~~~~~

.. code-block:: bash

    $ copycheck check path/to/directory | sort


Add copyright header
~~~~~~~~~~~~~~~~~~~~

Add copyright header to all Python files available from current directory"

.. code-block:: bash

    $ copycheck check . | sort | grep "\.py" | xargs -L1 sed -i '' '1i\
      # Copyright 2016 (c) Janus Friis Nielsen, all rights reserved. \
      \
      '


License
-------

*copycheck* is licensed under the `Mozilla Public License Version 2.0`_. See
`LICENSE`_ or the `FAQ`_ for more information.

In summary, you may use *copycheck* with any closed or open source project
without affecting the license of the larger work so long as you:

- give credit where credit is due,

- and release any custom changes made to *copycheck*.

.. _`Mozilla Public License Version 2.0`: http://www.mozilla.org/MPL/2.0
.. _`LICENSE`: LICENSE
.. _`FAQ`: http://www.mozilla.org/MPL/2.0/FAQ.html


Source
------

The source code for *copycheck* is available from the GitHub repo
`janusdn/copycheck`_.

.. _`janusdn/copycheck`: https://github.com/janusdn/copycheck


Contributing
------------

When contributing changes remember to update the `CHANGELOG.rst`.


Building copycheck
------------------
Make sure you have a Python 3.5 environment with the requirements. 

E.g. use pyenv:

.. code-block:: bash
    
    $ pyenv virtualenv 3.5.0 copycheck-venv
    $ pyenv activate copycheck-venv

Make sure pip is up-to-date:

.. code-block:: bash
    
    $ pip install --upgrade pip

Install requirements:

.. code-block:: bash
    
    $ pip install --upgrade -r requirements.txt

Build the wheel:

.. code-block:: bash
    
    $ make


Development
~~~~~~~~~~~

Use the following command to install the package in the local 
environment during development.

.. code-block:: bash
    
    $ pip install -e .

This allows you to change the code and test *copycheck*
directly.


Releasing
---------

Do the following to release a new version:

1. Commit changes
2. Push changes
3. Merge with master
4. Update local master
5. Find the next release version, e.g. 6.6.6
6. Create new branch with name core/release-6.6.6
7. Bump version in __about__.py
8. Run `./release.sh 6.6.6`


Upload to Pypi
--------------
First, perform a test upload to verify everything is nice and dandy.
Then perform the real upload.

Make sure the following environment variables have been properly defined:

.. code-block:: bash
    
    $ export PYPI_TEST_USERNAME="<username>"
    $ export PYPI_TEST_PASSWORD="<your_test_password>"
    $ export PYPI_USERNAME="<your_password>"
    $ export PYPI_PASSWORD="<username>"


Test upload to pypi
~~~~~~~~~~~~~~~~~~~

You may need to register on the Pypi test server. This can be done here:

.. code-block:: bash
    
    $ https://testpypi.python.org/pypi


Register:

.. code-block:: bash
    
    $ twine register -u ${PYPI_TEST_USERNAME} -p ${PYPI_TEST_PASSWORD} -r https://testpypi.python.org/pypi dist/Copycheck-6.6.6-py3-none-any.whl

Upload

.. code-block:: bash
    
    $ twine upload -u ${PYPI_TEST_USERNAME} -p ${PYPI_TEST_PASSWORD} -r https://testpypi.python.org/pypi dist/Copycheck-6.6.6-py3-none-any.whl

Goto:

.. code-block:: bash
    
    $ https://testpypi.python.org/pypi/Copycheck/6.6.6

An check that everything looks nice.

You can check the HTML by running:

 .. code-block:: bash
    
    $ python setup.py --long-description | rst2html.py --no-raw > output.html 


Test if it installs (do it in a different environment):

.. code-block:: bash
    
    $ pip install -i https://testpypi.python.org/pypi copycheck


Real upload to Pypi
~~~~~~~~~~~~~~~~~~~

Upload

.. code-block:: bash
    
    $ twine upload -u ${PYPI_USERNAME} -p ${PYPI_PASSWORD} -r https://pypi.python.org/pypi dist/copycheck-6.6.6-py3-none-any.whl

Goto:

.. code-block:: bash
    
    $ https://pypi.python.org/pypi/copycheck/6.6.6

And check that everything looks nice.


Thanks
------
A bug thank you goes to the author of the *pathspec* package. Using *pathspec* 
made it a lot easier to build this tool.
