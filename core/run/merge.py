import os

from core.compare import merge_entry
from core.util import folder


def run_merge_option(script_dir_path):
    # Choose folder with cif files
    merge_entry.combine_features_with_database_excel(script_dir_path)