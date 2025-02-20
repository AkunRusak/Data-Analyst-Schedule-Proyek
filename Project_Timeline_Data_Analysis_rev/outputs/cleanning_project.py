import os
import pandas as pd

from scripts import data_cleaning

if not os.path.exists('outputs'):
    os.makedirs('outputs')

data_cleaning.to_csv('outputs/clean_project_data.csv', index=False)
