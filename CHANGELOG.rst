=============
Release notes
=============

.. current developments

0.0.2
=====

**Added:**

* Add sphinx automatic API doc building when rendered.
* Add publication DOIs using OLED or CAF in index.rst of the documentation.
* Add GitHub URLs to authors (Bob, Emil, Danilla, Oliynyk) in the documentation.
* Describe the difference between CAF and SAF in the documentation.
* Add where to download OLED dataset, either from bobleesj.utils Python package or Excel file hosted on GitHub.
* Add SAF+CAF combined performance image in the documentation.
* Add Emil, Danila to authors in pyproject.toml.
* Generate online documentation.

**Fixed:**

* Update heatmap periodic table in the documentation
* Fix duplicates dropping during feature generation.
* Update CAF supported elements table in the documentation.
* Remove electron max/min in the universal feature to resolve division by zero error.

**Removed:**

* Remove sort by property and stoichiometry as they are implemented in bobleesj.utils.
* Remove sort by custom label features since it is migrated to bobleesj.utils.


0.0.1
=====

**Added:**

* Implement CAF package and use scikit-package to support Level 5 package standard.
* Implement sort function within CAF.

**Changed:**

* Implement line-lenght of 79 characters to ensure code is easier to read on smaller screens.
* Separate the CLI code for running CAF to a separate repository to maintain modularity of CAF.

**Removed:**

* Remove the CLI code for running SAF to a separate repository to maintain modularity of CAF.
