"""
Filename: Extract_features_all_events.py
Author : Brahim Fakri
Description: This file is used to define the function used for demographic embeddings extraction
Date of last modification : 2023/03/20
"""


from src.data import constants
import pandas as pd
from pandas import read_csv
import datetime as dt
import numpy as np

from sklearn.preprocessing import LabelEncoder 
le = LabelEncoder()



'''

Function extract_demographics that transforms demographic data to features

'''
    
    

def extract_demographics():
    ### Read data from local source
    #MIMIC-IV Dataset
    #Core
    df_admissions = read_csv(constants.admissions)
    df_patients = read_csv(constants.patients)
    df_transfers = read_csv(constants.transfers)


    #ICU

    df_icustays = read_csv(constants.icustays)


    #MIMIC-CXR

    df_mimic_cxr_chexpert = read_csv(constants.mimic_cxr_chexpert)
    df_mimic_cxr_metadata = read_csv(constants.mimic_cxr_metadata)


    #### CORE dataset fusion

    df_core_fusion = df_admissions.merge(df_patients, on=("subject_id")).merge(df_transfers, on=('subject_id', 'hadm_id'))



    df_core_icu_fusion = df_core_fusion.merge(df_icustays, on=('subject_id', 'hadm_id'))


    #### CXR dataset fusion

    df_cxr_merged = df_mimic_cxr_chexpert.merge(df_mimic_cxr_metadata, on= ('subject_id', 'study_id'))


    #### Core_ICU_CXR Fusion

    df_core_icu_cxr_fusion = df_core_icu_fusion.merge(df_cxr_merged, on=("subject_id"))


    # Demographics categorical features creation

    demo_embeddings = ['anchor_age', 'gender', 'ethnicity', 'marital_status', 'language', 'insurance']

    for i in range (len(demo_embeddings)):

        df_core_icu_cxr_fusion['de_'+str(i)] = df_core_icu_cxr_fusion[demo_embeddings[i]]

    # Demographics categorical features encoding

    for i in range(5):
              df_core_icu_cxr_fusion['de_'+str(i+1)] = le.fit_transform(df_core_icu_cxr_fusion['de_'+str(i+1)])


    df_core_icu_cxr_fusion = df_core_icu_cxr_fusion.drop(['anchor_age', 'gender', 'ethnicity', 'marital_status', 'language', 'insurance'], axis=1)


    df_core_icu_cxr_fusion['death_status'] = np.where(df_core_icu_cxr_fusion['discharge_location'] == 'DIED' ,1,0)


    df_core_icu_cxr_fusion = df_core_icu_cxr_fusion.drop(['discharge_location'], axis =1)


    df_core_icu_cxr_fusion = df_core_icu_cxr_fusion.loc[: , ['subject_id', 'hadm_id','stay_id',  'admittime','de_0', 'de_1', 'de_2',
           'de_3', 'de_4', 'de_5', 'death_status', 'study_id', 'Atelectasis', 'Cardiomegaly', 'Consolidation',
           'Edema', 'Enlarged Cardiomediastinum', 'Fracture', 'Lung Lesion',
           'Lung Opacity', 'No Finding', 'Pleural Effusion', 'Pleural Other',
           'Pneumonia', 'Pneumothorax', 'Support Devices', 'dicom_id',
           'PerformedProcedureStepDescription', 'ViewPosition', 'Rows', 'Columns',
           'StudyDate', 'StudyTime', 'ProcedureCodeSequence_CodeMeaning',
           'ViewCodeSequence_CodeMeaning',
           'PatientOrientationCodeSequence_CodeMeaning', ]]

    return df_core_icu_cxr_fusion

    




