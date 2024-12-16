import os
import sys 
import pprint
import random 
import pandas as pd

from datetime import date, datetime, timedelta

# Add the directory containing utils.py to the Python path
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "../utils")))

# Import the utility function
from utils import *

def generate_row(dict_types):
    columns = ["start_date", "age", "amount"]
    col_type = ["date", "integer", "float"]
    row = []
    for iter_col, iter_type in zip(columns, col_type):
        print(f"iter_col: {iter_col} -- iter_type: {iter_type}")
        if iter_type == "date":
            # Generate date
            start_date = datetime(2000, 1, 1)
            end_date = date.today()
            print(f"Generating date between {start_date} and {end_date}")

        elif iter_type == "integer":
            # Generate integer
            pass 
        elif iter_type == "float":
            # Generate float
            pass 
        else:
            raise("something missing in schema")




def main():
    pass 

if __name__ == '__main__':
    print("All good")
    dict_types = func_read_yaml("../schema/types.yaml")
    pprint.pprint(dict_types, compact=True)
    
    # generate row
    generate_row(dict_types)

    
    