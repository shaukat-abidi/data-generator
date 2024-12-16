"""
utils.py: A utility module for data preprocessing functions.

This module contains a set of utility functions for common data preprocessing
tasks such as renaming and casting columns in a pandas DataFrame.

"""

import os
import sys
import pandas as pd
import yaml

def check_file_exists(filepath, error_message):
    """
    Check if a file exists. Exit the script with a message if the file is missing.
    
    Args:
        filepath (str): Path to the file to check.
        error_message (str): Message to display if the file is missing.
    """
    if not os.path.exists(filepath):
        print(error_message)
        sys.exit(1)
    print(f"{filepath} exists.")

def func_read_yaml(read_filepath):
    """
    Load YAML file and return the content as a dictionary.
    
    Args:
        filepath (str): Path to the YAML file.
    
    Returns:
        dict: Parsed YAML content.
    """
    
    try:
        with open(read_filepath, "r") as file:
            print(f"Loading YAML: {read_filepath}")
            return yaml.safe_load(file)
    except Exception as e:
        print(f"Error details: {e}")
        sys.exit(1) 

