"""
Filename: Generate_Final_Features.py
Author : Brahim Fakri
Description: This file is used to define the function used for demographic embeddings extraction
Date of last modification : 2023/05/02
"""


import pandas as pd
import numpy as np

from pandas import read_csv

from src.data import constants
from src.utils import *

'''

Function Generate_Final_Features that concatenates all types of features to generate the embeddings file

'''

def Generate_Final_Features():
    ### Read features files
    
    fusion_ts_dem_dataframe = read_csv(constants.fusion_ts_dem_dataframe)
    fusion_vision_dataframe = read_csv(constants.fusion_vision_dataframe)
    
    ## Concatenate

    Final_Features = pd.merge(fusion_ts_dem_dataframe, fusion_vision_dataframe, on='subject_id')

    return Final_Features

    




