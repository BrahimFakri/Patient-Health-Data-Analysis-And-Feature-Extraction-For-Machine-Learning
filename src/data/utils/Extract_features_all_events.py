from src.data import constants
import pandas as pd
from pandas import read_csv
import datetime as dt
import numpy as np

import tsfresh
from tsfresh import extract_features


# # Function extract_chart_events that transforms chartevents to features

# In[2]:


def extract_chart_events(source, patient):
    
    df_chartevents =read_csv(source,low_memory=False, dtype={'value': 'object', 'valueuom': 'object'}, nrows=20000000)
    
    df_chartevents.charttime = pd.to_datetime(df_chartevents.charttime)
    
    df_chartevents['valuenum'] = df_chartevents['valuenum'].fillna(0)

    df_d_items = pd.read_csv(constants.d_items)

    df_chartevents_subject_id_example = df_chartevents[df_chartevents["subject_id"] == patient]
    
    #####
            ###########################################

    df_chartevents_subject_id_example_events=["df_chartevents_subject_id_example_events"+str(i) for i in                                              range(len(constants.chart_event_list))]
    for i in range(len(df_chartevents_subject_id_example_events)):
        exec("%s = %d" % (df_chartevents_subject_id_example_events[i] ,0))
        
    #####
            ###########################################   

    chart_series=["chart_series"+str(i) for i in range(len(constants.chart_event_list))]
    for i in range(len(chart_series)):
        exec("%s = %d" % (chart_series[i] ,0))
        
    #####
            ###########################################   

    chart_extracted_features = ["chart_extracted_features"+str(i) for i in range(len(constants.chart_event_list))]
    for i in range(len(chart_extracted_features)):
        exec("%s = %d" % (chart_extracted_features[i] ,0))

    #####

    for i in range(len(df_chartevents_subject_id_example_events)):
        df_chartevents_subject_id_example_events[i] = df_chartevents_subject_id_example[df_chartevents_subject_id_example["itemid"].isin(df_d_items[df_d_items["label"] == constants.chart_event_list[i]]["itemid"])]


    for i in range(len(df_chartevents_subject_id_example_events)):
        df_chartevents_subject_id_example_events[i][constants.chart_event_list[i]] = df_chartevents_subject_id_example_events[i]["valuenum"]


    for i in range(len(df_chartevents_subject_id_example_events)):
        chart_series[i] = df_chartevents_subject_id_example_events[i][["subject_id","charttime",constants.chart_event_list[i]]]

        chart_extracted_features[i] = extract_features(chart_series[i], column_id="subject_id", column_sort="charttime", default_fc_parameters = constants.fc_parameters)




    chart_extracted_features_concat = pd.concat(chart_extracted_features, axis=1)

    return chart_extracted_features_concat


# In[3]:


#extract_chart_events(constants.chartevents, constants.subject_id_example)


# # Function extract_lab_events that transforms lab events to features

# In[4]:


def extract_lab_events(source, patient):
    
    df_labevents =read_csv(source,low_memory=False, dtype={'storetime': 'object', 'value': 'object', 'valueuom': 'object', 'flag': 'object', 'priority': 'object', 'comments': 'object'}, nrows=30000000)

    df_d_labitems = pd.read_csv(constants.d_labitems)

    df_labevents.charttime = pd.to_datetime(df_labevents.charttime)

    df_labevents['valuenum'] = df_labevents['valuenum'].fillna(0)


    df_labevents_subject_id_example = df_labevents[df_labevents["subject_id"] == patient]

    #####
            ###########################################
    df_labevents_subject_id_example_events=["df_labevents_subject_id_example_events"+str(i) for i in                                              range(len(constants.lab_event_list))]
    for i in range(len(df_labevents_subject_id_example_events)):
        exec("%s = %d" % (df_labevents_subject_id_example_events[i] ,0))

        #####################################

    lab_series=["lab_series"+str(i) for i in range(len(constants.lab_event_list))]
    for i in range(len(lab_series)):
        exec("%s = %d" % (lab_series[i] ,0))

        ########################################

    lab_extracted_features = ["lab_extracted_features"+str(i) for i in range(len(constants.lab_event_list))]
    for i in range(len(lab_extracted_features)):
        exec("%s = %d" % (lab_extracted_features[i] ,0))

    #####

    for i in range(len(df_labevents_subject_id_example_events)):
        df_labevents_subject_id_example_events[i] = df_labevents_subject_id_example[df_labevents_subject_id_example["itemid"].isin(df_d_labitems[df_d_labitems["label"] == constants.lab_event_list[i]]["itemid"])]


    for i in range(len(df_labevents_subject_id_example_events)):
        df_labevents_subject_id_example_events[i][constants.lab_event_list[i]] = df_labevents_subject_id_example_events[i]["valuenum"]


    for i in range(len(df_labevents_subject_id_example_events)):
        lab_series[i] = df_labevents_subject_id_example_events[i][["subject_id","charttime",constants.lab_event_list[i]]]

        lab_extracted_features[i] = extract_features(lab_series[i], column_id="subject_id", column_sort="charttime", default_fc_parameters = constants.fc_parameters)



    lab_extracted_features_concat = pd.concat(lab_extracted_features, axis=1)

    return lab_extracted_features_concat


# In[5]:


#extract_lab_events(constants.labevents, constants.subject_id_example)


# # Function extract_procedure_events that transforms procedure events to features

# In[ ]:


def extract_procedure_events(source, patient):
    
    df_procedureevents =read_csv(source)
    
    df_procedureevents.storetime = pd.to_datetime(df_procedureevents.storetime)
    
    df_procedureevents['value'] = df_procedureevents['value'].fillna(0)

    df_d_items = pd.read_csv(constants.d_items)

    df_procedureevents_subject_id_example = df_procedureevents[df_procedureevents["subject_id"] == patient]
    
    #####
            ###########################################

    df_procedureevents_subject_id_example_events=["df_procedureevents_subject_id_example_events"+str(i) for i in                                              range(len(constants.procedure_event_list))]
    for i in range(len(df_procedureevents_subject_id_example_events)):
        exec("%s = %d" % (df_procedureevents_subject_id_example_events[i] ,0))
        
    #####
            ###########################################   

    procedure_series=["procedure_series"+str(i) for i in range(len(constants.procedure_event_list))]
    for i in range(len(procedure_series)):
        exec("%s = %d" % (procedure_series[i] ,0))
        
    #####
            ###########################################   

    procedure_extracted_features = ["procedure_extracted_features"+str(i) for i in range(len(constants.procedure_event_list))]
    for i in range(len(procedure_extracted_features)):
        exec("%s = %d" % (procedure_extracted_features[i] ,0))

    #####

    for i in range(len(df_procedureevents_subject_id_example_events)):
        df_procedureevents_subject_id_example_events[i] = df_procedureevents_subject_id_example[df_procedureevents_subject_id_example["itemid"].isin(df_d_items[df_d_items["label"] == constants.procedure_event_list[i]]["itemid"])]


    for i in range(len(df_procedureevents_subject_id_example_events)):
        df_procedureevents_subject_id_example_events[i][constants.procedure_event_list[i]] = df_procedureevents_subject_id_example_events[i]["value"]


    for i in range(len(df_procedureevents_subject_id_example_events)):
        procedure_series[i] = df_procedureevents_subject_id_example_events[i][["subject_id","storetime",constants.procedure_event_list[i]]]

        procedure_extracted_features[i] = extract_features(procedure_series[i], column_id="subject_id", column_sort="storetime", default_fc_parameters = constants.fc_parameters)




    procedure_extracted_features_concat = pd.concat(procedure_extracted_features, axis=1)

    return procedure_extracted_features_concat


# In[ ]:


#extract_procedure_events(constants.procedureevents, constants.subject_id_example)

