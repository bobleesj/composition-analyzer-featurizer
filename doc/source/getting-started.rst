.. _getting-started:

Getting started
===============

There are two ways to generate compositional features. The recommended way is to use the CAF app, a command-line interface (CLI) application that can automatically detect folders and files.

The **second** way is to use the Python package directly in your code, which is useful for advanced users who want to integrate CAF into their own workflows in Python scripts or Jupyter notebooks. This method requires some coding knowledge and familiarity with Python packages.

.. _CAF-app-installation:

Method 1. Using CAF Application
-------------------------------

First, download the CAF application from the GitHub repository. You can clone (download) the files using the following command:

.. code-block:: bash

   git clone https://github.com/bobleesj/composition-analyzer-featurizer-app.git

.. note::

   Alternatively, you can download the ZIP file from the GitHub repository (https://github.com/bobleesj/composition-analyzer-featurizer-app) by clicking the green :guilabel:`Code` button and :guilabel:`Download ZIP`. After downloading, extract the contents of the ZIP file to a directory of your choice.

Next, navigate to the directory and install the required package using pip:

.. code-block:: bash

   cd composition-analyzer-featurizer-app
   pip install composition-analyzer-featurizer

You can then run the application by executing the following command:

.. code-block:: bash

   python main.py

Upon running ``python main.py``, you will be prompted to choose from one of the following options:

.. code-block:: text

   Options:
   1: Filter chemical formulas and generate periodic table heatmap.
   2: Sort chemical formulas in Excel.
   3: Create compositional features for formulas in Excel.
   4: Match .cif files in a folder against Excel.
   5: Merge two Excel files based on id/entry.
   Please enter the number of the option you want to run: 3

Type ``3`` and press ``Enter`` to generate compositional features for a list of chemical formulas in an Excel file. The application already contains example Excel files. Once the features are generated, you can find the output Excel file in the same directory.

.. note::

   Are you having trouble running code? Learn to use conda environments by following the instructions provided `here <https://scikit-package.github.io/scikit-package/tutorials/tutorial-level-1-2-3.html#required-use-conda-environment-to-install-packages-and-run-python-code>`_.

Method 2. Import CAF in Python file or Jupyter notebook
-------------------------------------------------------

You might be interested in generating compositional features without using the CAF application. You can generate features by calling the function provided in the ``CAF`` package directly. First, you need to install the package using pip.

.. code-block:: bash

   pip install composition-analyzer-featurizer bobleesj.utils

In your Python module, add the following to generate features for a binary compound:

.. code-block:: python

   from CAF.features import binary, ternary, quaternary
   from bobleesj.utils.sources.oliynyk import Oliynyk

   # Example binary compound formula
   formula = "NdSi2"
   # Get Oliynyk elemental property dataset. Visit https://bobleesj.github.io/bobleesj.utils for more info.
   oliynyk_db = Oliynyk().db
   binary_features = binary.generate_features(formula, oliynyk_db)
   print(binary_features)

For more information, please see the ``src/CAF/features/generator.py`` file and the ``get_composition_features`` function to learn how to generate a list of features for binary, ternary, or quaternary compounds. The source code can be found in the `GitHub repository <https://github.com/bobleesj/composition-analyzer-featurizer/tree/main/src/CAF>`_.
