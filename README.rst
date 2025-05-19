|Icon| |title|_
===============

.. |title| replace:: composition-analyzer-featurizer
.. _title: https://bobleesj.github.io/composition-analyzer-featurizer

.. |Icon| image:: https://avatars.githubusercontent.com/bobleesj
        :target: https://bobleesj.github.io/composition-analyzer-featurizer
        :height: 100px

|PyPI| |Forge| |PythonVersion| |PR|

|CI| |Codecov| |Black| |Tracking|

.. |Black| image:: https://img.shields.io/badge/code_style-black-black
        :target: https://github.com/psf/black

.. |CI| image:: https://github.com/bobleesj/composition-analyzer-featurizer/actions/workflows/matrix-and-codecov-on-merge-to-main.yml/badge.svg
        :target: https://github.com/bobleesj/composition-analyzer-featurizer/actions/workflows/matrix-and-codecov-on-merge-to-main.yml

.. |Codecov| image:: https://codecov.io/gh/bobleesj/composition-analyzer-featurizer/branch/main/graph/badge.svg
        :target: https://codecov.io/gh/bobleesj/composition-analyzer-featurizer

.. |Forge| image:: https://img.shields.io/conda/vn/conda-forge/composition-analyzer-featurizer
        :target: https://anaconda.org/conda-forge/composition-analyzer-featurizer

.. |PR| image:: https://img.shields.io/badge/PR-Welcome-29ab47ff

.. |PyPI| image:: https://img.shields.io/pypi/v/composition-analyzer-featurizer
        :target: https://pypi.org/project/composition-analyzer-featurizer/

.. |PythonVersion| image:: https://img.shields.io/pypi/pyversions/composition-analyzer-featurizer
        :target: https://pypi.org/project/composition-analyzer-featurizer/

.. |Tracking| image:: https://img.shields.io/badge/issue_tracking-github-blue
        :target: https://github.com/bobleesj/composition-analyzer-featurizer/issues

Python package for generating compositional features for binary, ternary, and quaternary formulas with Oliynyk elemental properties.

* LONGER DESCRIPTION HERE

For more information about the composition-analyzer-featurizer library, please consult our `online documentation <https://bobleesj.github.io/composition-analyzer-featurizer>`_.

Citation
--------

If you use composition-analyzer-featurizer in a scientific publication, we would like you to cite this package as

        composition-analyzer-featurizer Package, https://github.com/bobleesj/composition-analyzer-featurizer

Installation
------------

The preferred method is to use `Miniconda Python
<https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html>`_
and install from the "conda-forge" channel of Conda packages.

To add "conda-forge" to the conda channels, run the following in a terminal. ::

        conda config --add channels conda-forge

We want to install our packages in a suitable conda environment.
The following creates and activates a new environment named ``composition-analyzer-featurizer_env`` ::

        conda create -n composition-analyzer-featurizer_env composition-analyzer-featurizer
        conda activate composition-analyzer-featurizer_env

To confirm that the installation was successful, type ::

        python -c "import CAF; print(CAF.__version__)"

The output should print the latest version displayed on the badges above.

If the above does not work, you can use ``pip`` to download and install the latest release from
`Python Package Index <https://pypi.python.org>`_.
To install using ``pip`` into your ``composition-analyzer-featurizer_env`` environment, type ::

        pip install composition-analyzer-featurizer

If you prefer to install from sources, after installing the dependencies, obtain the source archive from
`GitHub <https://github.com/bobleesj/composition-analyzer-featurizer/>`_. Once installed, ``cd`` into your ``composition-analyzer-featurizer`` directory
and run the following ::

        pip install .

Getting Started
---------------

You may consult our `online documentation <https://bobleesj.github.io/composition-analyzer-featurizer>`_ for tutorials and API references.

Support and Contribute
----------------------

If you see a bug or want to request a feature, please `report it as an issue <https://github.com/bobleesj/composition-analyzer-featurizer/issues>`_ and/or `submit a fix as a PR <https://github.com/bobleesj/composition-analyzer-featurizer/pulls>`_.

Feel free to fork the project and contribute. To install composition-analyzer-featurizer
in a development mode, with its sources being directly used by Python
rather than copied to a package directory, use the following in the root
directory ::

        pip install -e .

To ensure code quality and to prevent accidental commits into the default branch, please set up the use of our pre-commit
hooks.

1. Install pre-commit in your working environment by running ``conda install pre-commit``.

2. Initialize pre-commit (one time only) ``pre-commit install``.

Thereafter your code will be linted by black and isort and checked against flake8 before you can commit.
If it fails by black or isort, just rerun and it should pass (black and isort will modify the files so should
pass after they are modified). If the flake8 test fails please see the error messages and fix them manually before
trying to commit again.

Improvements and fixes are always appreciated.

Before contributing, please read our `Code of Conduct <https://github.com/bobleesj/composition-analyzer-featurizer/blob/main/CODE_OF_CONDUCT.rst>`_.

Contact
-------

For more information on composition-analyzer-featurizer please visit the project `web-page <https://bobleesj.github.io/>`_ or email Sangjoon Lee at bobleesj@gmail.com.

Acknowledgements
----------------

``composition-analyzer-featurizer`` is built and maintained with `scikit-package <https://scikit-package.github.io/scikit-package/>`_.
