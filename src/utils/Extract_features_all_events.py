"""
Filename: Extract_features_all_events.py
Author : Brahim Fakri
Description: This file is used to define functions used for time series embeddings  extraction
Date of last modification : 2023/03/20
"""

from src.data import constants
import pandas as pd
from pandas import read_csv
import datetime as dt
import numpy as np

import tsfresh
from tsfresh import extract_features


'''
Function extract_chart_events that transforms chartevents to features

'''

def extract_chart_events(source, patient):
    
    
    # Reading the chartevents csv file 
    df_chartevents =read_csv(source,low_memory=False, dtype={'value': 'object', 'valueuom': 'object'}, nrows = constants.NROWS)
    
    # Converting the charttime column to datetime type
    df_chartevents.charttime = pd.to_datetime(df_chartevents.charttime)
    
    # filling missing values with 0 as instructed by the study
    df_chartevents['valuenum'] = df_chartevents['valuenum'].fillna(0)

    # Reading the d_items csv file that contains the description of all chart events
    df_d_items = pd.read_csv(constants.d_items)

    # filtering the dataset to include only the desired patient to study
    df_chartevents_subject_id_example = df_chartevents[df_chartevents["subject_id"] == patient]
    
    
    # Creating a list of variable names to be used to store chartevents
    df_chartevents_subject_id_example_events=["df_chartevents_subject_id_example_events"+str(i) for i in range(len(constants.chart_event_list))]
    for i in range(len(df_chartevents_subject_id_example_events)):
        exec("%s = %d" % (df_chartevents_subject_id_example_events[i] ,0))
        
    
    # Creating a list of variable names to be used to store chart series
    chart_series=["chart_series"+str(i) for i in range(len(constants.chart_event_list))]
    for i in range(len(chart_series)):
        exec("%s = %d" % (chart_series[i] ,0))
        
 
    # Creating a list of variable names to be used to store chart extracted features
    chart_extracted_features = ["chart_extracted_features"+str(i) for i in range(len(constants.chart_event_list))]
    for i in range(len(chart_extracted_features)):
        exec("%s = %d" % (chart_extracted_features[i] ,0))
    
    # Filtering chart events by events of interest from chart event list
    for i in range(len(df_chartevents_subject_id_example_events)):
        df_chartevents_subject_id_example_events[i] = df_chartevents_subject_id_example[df_chartevents_subject_id_example["itemid"].isin(df_d_items[df_d_items["label"] == constants.chart_event_list[i]]["itemid"])]

    # Assigning the corresponding values
    for i in range(len(df_chartevents_subject_id_example_events)):
        df_chartevents_subject_id_example_events[i][constants.chart_event_list[i]] = df_chartevents_subject_id_example_events[i]["valuenum"]

    # Creation of chart series to be used with TS Fresh
    for i in range(len(df_chartevents_subject_id_example_events)):
        chart_series[i] = df_chartevents_subject_id_example_events[i][["subject_id","charttime",constants.chart_event_list[i]]]
        
        # Extraction of the features using TS Fresh
        chart_extracted_features[i] = extract_features(chart_series[i], column_id="subject_id", column_sort="charttime", default_fc_parameters = constants.fc_parameters)



    # Concatenation of the extracted features
    chart_extracted_features_concat = pd.concat(chart_extracted_features, axis=1)
    
    # Return the concatenated dataframe
    return chart_extracted_features_concat





'''
Function extract_lab_events that transforms lab events to features

'''

def extract_lab_events(source, patient):
    
    # Reading the labevents csv file 
    df_labevents =read_csv(source,low_memory=False, dtype={'storetime': 'object', 'value': 'object', 'valueuom': 'object', 'flag': 'object', 'priority': 'object', 'comments': 'object'}, nrows = constants.NROWS)

    # Converting the charttime column to datetime type
    df_labevents.charttime = pd.to_datetime(df_labevents.charttime)

    # filling missing values with 0 as instructed by the study
    df_labevents['valuenum'] = df_labevents['valuenum'].fillna(0)

    # Reading the df_d_labitems csv file that contains the description of all lab events
    df_d_labitems = pd.read_csv(constants.d_labitems)

    # filtering the dataset to include only the desired patient to study
    df_labevents_subject_id_example = df_labevents[df_labevents["subject_id"] == patient]

    # Creating a list of variable names to be used to store labevents
    df_labevents_subject_id_example_events=["df_labevents_subject_id_example_events"+str(i) for i in  range(len(constants.lab_event_list))]
    for i in range(len(df_labevents_subject_id_example_events)):
        exec("%s = %d" % (df_labevents_subject_id_example_events[i] ,0))


    # Creating a list of variable names to be used to store lab series
    lab_series=["lab_series"+str(i) for i in range(len(constants.lab_event_list))]
    for i in range(len(lab_series)):
        exec("%s = %d" % (lab_series[i] ,0))

    # Creating a list of variable names to be used to store lab extracted features
    lab_extracted_features = ["lab_extracted_features"+str(i) for i in range(len(constants.lab_event_list))]
    for i in range(len(lab_extracted_features)):
        exec("%s = %d" % (lab_extracted_features[i] ,0))

    # Filtering lab events by events of interest from lab event list
    for i in range(len(df_labevents_subject_id_example_events)):
        df_labevents_subject_id_example_events[i] = df_labevents_subject_id_example[df_labevents_subject_id_example["itemid"].isin(df_d_labitems[df_d_labitems["label"] == constants.lab_event_list[i]]["itemid"])]

    # Assigning the corresponding values
    for i in range(len(df_labevents_subject_id_example_events)):
        df_labevents_subject_id_example_events[i][constants.lab_event_list[i]] = df_labevents_subject_id_example_events[i]["valuenum"]

    # Creation of lab series to be used with TS Fresh
    for i in range(len(df_labevents_subject_id_example_events)):
        lab_series[i] = df_labevents_subject_id_example_events[i][["subject_id","charttime",constants.lab_event_list[i]]]

        # Extraction of the features using TS Fresh
        try:
            lab_extracted_features[i] = extract_features(lab_series[i], column_id="subject_id", column_sort="charttime", default_fc_parameters = constants.fc_parameters)
        
        except ZeroDivisionError:
            lab_extracted_features[i] = pd.DataFrame()


    # Concatenation of the extracted features
    lab_extracted_features_concat = pd.concat(lab_extracted_features, axis=1)

    # Return the concatenated dataframe
    return lab_extracted_features_concat



'''
Function extract_procedure_events that transforms procedure events to features

'''



def extract_procedure_events(source, patient):

    # Reading the procedureevents csv file 
    df_procedureevents =read_csv(source)

    # Converting the charttime column to datetime type
    df_procedureevents.storetime = pd.to_datetime(df_procedureevents.storetime)

    # filling missing values with 0 as instructed by the study
    df_procedureevents['value'] = df_procedureevents['value'].fillna(0)

    # Reading the d_items csv file that contains the description of all procedure events
    df_d_items = pd.read_csv(constants.d_items)

    # filtering the dataset to include only the desired patient to study
    df_procedureevents_subject_id_example = df_procedureevents[df_procedureevents["subject_id"] == patient]

    # Creating a list of variable names to be used to store procedureevents
    df_procedureevents_subject_id_example_events=["df_procedureevents_subject_id_example_events"+str(i) for i in range(len(constants.procedure_event_list))]
    for i in range(len(df_procedureevents_subject_id_example_events)):
        exec("%s = %d" % (df_procedureevents_subject_id_example_events[i] ,0))

    # Creating a list of variable names to be used to store procedure series
    procedure_series=["procedure_series"+str(i) for i in range(len(constants.procedure_event_list))]
    for i in range(len(procedure_series)):
        exec("%s = %d" % (procedure_series[i] ,0))

    # Creating a list of variable names to be used to store procedure extracted features
    procedure_extracted_features = ["procedure_extracted_features"+str(i) for i in range(len(constants.procedure_event_list))]
    for i in range(len(procedure_extracted_features)):
        exec("%s = %d" % (procedure_extracted_features[i] ,0))

    # Filtering procedure events by events of interest from procedure event list
    for i in range(len(df_procedureevents_subject_id_example_events)):
        df_procedureevents_subject_id_example_events[i] = df_procedureevents_subject_id_example[df_procedureevents_subject_id_example["itemid"].isin(df_d_items[df_d_items["label"] == constants.procedure_event_list[i]]["itemid"])]

    # Assigning the corresponding values
    for i in range(len(df_procedureevents_subject_id_example_events)):
        df_procedureevents_subject_id_example_events[i][constants.procedure_event_list[i]] = df_procedureevents_subject_id_example_events[i]["value"]

    # Creation of chart series to be used with TS Fresh
    for i in range(len(df_procedureevents_subject_id_example_events)):
        procedure_series[i] = df_procedureevents_subject_id_example_events[i][["subject_id","storetime",constants.procedure_event_list[i]]]

        # Extraction of the features using TS Fresh
        try:
            procedure_extracted_features[i] = extract_features(procedure_series[i], column_id="subject_id", column_sort="storetime", default_fc_parameters = constants.fc_parameters)
        
        except ZeroDivisionError:
            procedure_extracted_features[i] = pd.DataFrame()


    # Concatenation of the extracted features
    procedure_extracted_features_concat = pd.concat(procedure_extracted_features, axis=1)


        

    # Return the concatenated dataframe
    return procedure_extracted_features_concat



