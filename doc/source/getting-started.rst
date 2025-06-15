Getting started
===============


CAF is primarily used as an interactive application that can automatically detect folders and files. Use the following steps in your command-line interface:

.. code-block:: bash

   # Download the code
   git clone https://github.com/bobleesj/composition-analyzer-featurizer-app.git

   # Navigate to the directory
   cd composition-analyzer-featurizer-app

   # Install CAF package
   pip install composition-analyzer-featurizer

   # Execute the script
   python main.py

Upon running ``python main.py``, you will be prompted to choose from one of the following options:

.. code-block:: text

   Options:
   1: Filter chemical formulas and generate periodic table heatmap
   2: Sort chemical formulas in Excel
   3: Create compositional features for formulas in Excel
   4: Match .cif files in a folder against Excel
   5: Merge two Excel files based on id/entry
   Please enter the number of the option you want to run: 1

.. note::

   Are you having trouble running code? Please learn to use conda environments by following the instructions provided `here <https://scikit-package.github.io/scikit-package/tutorials/tutorial-level-1-2-3.html#required-use-conda-environment-to-install-packages-and-run-python-code>`_.
