#!/usr/bin/env python
##############################################################################
#
# (c) 2025 Sangjoon Lee.
# All rights reserved.
#
# File coded by: Sangjoon Lee, Emil Jaffal, Danila Shiryaev, Nikhil Kumar Barua
#
# See GitHub contributions for a more detailed list of contributors.
# https://github.com/bobleesj/composition-analyzer-featurizer/graphs/contributors
#
# See LICENSE.rst for license information.
#
##############################################################################
"""Definition of __version__."""

#  We do not use the other three variables, but can be added back if needed.
#  __all__ = ["__date__", "__git_commit__", "__timestamp__", "__version__"]

# obtain version information
from importlib.metadata import version

__version__ = version("composition-analyzer-featurizer")

# End of file
