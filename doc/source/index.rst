#######
|title|
#######

.. |title| replace:: Composition Analyzer/Featurizer (CAF)

.. image:: https://img.shields.io/badge/PR-Welcome-29ab47ff
   :alt: PR Welcome
   :target: https://github.com/bobleesj/composition-analyzer-featurizer/pulls
.. image:: https://img.shields.io/github/issues/bobleesj/composition-analyzer-featurizer
   :alt: GitHub issues
   :target: https://github.com/bobleesj/composition-analyzer-featurizer/issues
.. image:: https://img.shields.io/pypi/v/composition-analyzer-featurizer
   :alt: PyPI
   :target: https://pypi.org/project/composition-analyzer-featurizer/
.. image:: https://img.shields.io/pypi/pyversions/composition-analyzer-featurizer
   :alt: Python Version

| Software version |release|
| Last updated |today|.

Composition Analyzer/Featurizer (CAF) offers a user-interactive Python script that provides tools for generating compositional descriptors of binary, ternary, and quaternary compounds from Excel or `.cif` files. CAF also offers utility functions to filter, sort chemical formulas, and merge Excel files.

Publications and scientific utility
===================================

* *Digital Discovery*, https://doi.org/10.1039/D4DD00332B
* *Data in Brief*, https://doi.org/10.1016/j.dib.2024.110178

In the above Digital Discovery paper (`DOI <https://doi.org/10.1039/D4DD00332B>`_), we describe the performance of CAF in combination with SAF for generating compositional and structural numerical features for ML applications in crystal classification of binary compounds. The results are shown in Figure 1 below, where we compare the performance of our developments (CAF and SAF) with existing feature generation methods such as JARVIS, MAGPIE, mat2vec, and OLED.

.. image:: img/SAF-CAF-performance.png
   :alt: PLS-DA latent value plot using the first two latent value dimensions: (a) JARVIS, (b) MAGPIE, (c) mat2vec, (d) OLED (all sets of features were generated with CBFV), and our developments – (e) CAF and (f) SAF.

.. note::
   **Figure 1:** PLS-DA latent value plot using the first two latent value dimensions: (a) JARVIS, (b) MAGPIE, (c) mat2vec, (d) OLED (all sets of features were generated with CBFV), and our developments – (e) CAF and (f) SAF.

How CAF works
=============

For a given chemical formula, CAF determines the number of unique elements and categorizes them into binary, ternary, or quaternary compounds. It then generates a set of compositional features based on the chemical formula:

- 133 binary features
- 204 ternary features
- 305 quaternary features are generated

The features generated based on the elemental property Oliynyk elemental property dataset (`DOI <https://doi.org/10.1016/j.dib.2024.110178>`_). The full lists of features are provided in the :ref:`features` page.


Getting started
===============

You can simply generate compositional features using our application so that you don't have to write any code. Please visit :ref:`getting-started` to learn how to generate features.

Scope
=====

There are two constraints. First, formulas of either **binary**, **ternary**, or **quaternary** compounds are supported. Second, formulas containing the elements in blue below are supported:

.. image:: img/elements-supported-in-periodic-table.png
   :alt: Elements supported in CAF

5 Options provided in CAF App
=============================

The recommended way to generate features is using the interactive application. Beyond generating features from a list of formulas listed in an Excel file under the "Formula" column, there are other utility options that can help you filter, sort, and merge Excel files which are used for generating features and handling data.

.. image:: img/process-diagram.png
   :alt: process diagram

How to ask for help
===================

- Do you have any feature requests? Please feel free to open an issue on GitHub using the ``Bug Report or Feature Request`` template.
- Do you have any questions about running the code? Please feel free to reach out to Sangjoon Bob Lee at bobleesj@stanford.edu.
- Do you want to learn how to publish scientific software? ``CAF`` is developed and maintained using the Level 5 package standards provided in `scikit-package <https://scikit-package.github.io/scikit-package/>`_.

How you can contribute to CAF
=============================

- Did you find CAF helpful? You can show support by starring the `GitHub repository <https://github.com/bobleesj/composition-analyzer-featurizer>`_ and recommending it to colleagues.
- Did you find any bugs? Please feel free to report it by creating a new issue so that we can fix it as soon as possible.-

.. seealso::

   Do you want to learn how to use GitHub and develop Python package to reuse your code? Please feel free to reach out to Sasngjoon Bob Lee (bobleesj@stanford.edu). There are resources you can use to get started such as `scikit-package <https://scikit-package.github.io/scikit-package/>`_.

Authors
=======

- Sangjoon Bob Lee - development lead, maintainer
- Anton Oliynyk - development lead, feature design
- Emil Jaffal - filter
- Danila Shiryaev - sort
- Alex Vtorov - feature
- Nikhil Kumar Barua - feature

Acknowledgements
================

``CAF`` is built and maintained with `scikit-package <https://scikit-package.github.io/scikit-package/>`_.

.. toctree::
   :maxdepth: 2
   :caption: GUIDES
   :hidden:

   getting-started
   app

.. toctree::
   :maxdepth: 2
   :caption: REFERENCE
   :hidden:

   features
   Package API <api/CAF>
   release
   license
