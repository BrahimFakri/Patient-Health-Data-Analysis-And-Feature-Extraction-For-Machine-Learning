"""
Filename: constants.py
Author : Brahim Fakri
Description: This file is used to store constants
Date of last modification : 2023/04/18
"""
  

'''Links to datasets'''
    
# CORE
admissions = 'csvs/mimic-iv-1.0/core/admissions.csv'
patients = 'csvs/mimic-iv-1.0/core/patients.csv'
transfers = 'csvs/mimic-iv-1.0/core/transfers.csv'

#HOSP
d_labitems = 'csvs/mimic-iv-1.0/hosp/d_labitems.csv'
d_icd_procedures = 'csvs/mimic-iv-1.0/hosp/d_icd_procedures.csv'
d_icd_diagnoses = 'csvs/mimic-iv-1.0/hosp/d_icd_diagnoses.csv'
d_hcpcs = 'csvs/mimic-iv-1.0/hosp/d_hcpcs.csv'
diagnoses_icd = 'csvs/mimic-iv-1.0/hosp/diagnoses_icd.csv'
drgcodes = 'csvs/mimic-iv-1.0/hosp/drgcodes.csv'
emar = 'csvs/mimic-iv-1.0/hosp/emar.csv'
emar_detail = 'csvs/mimic-iv-1.0/hosp/emar_detail.csv'
hcpcsevents = 'csvs/mimic-iv-1.0/hosp/hcpcsevents.csv'
labevents = 'csvs/mimic-iv-1.0/hosp/labevents.csv'
microbiologyevents = 'csvs/mimic-iv-1.0/hosp/microbiologyevents.csv'
poe = 'csvs/mimic-iv-1.0/hosp/poe.csv'
poe_detail = 'csvs/mimic-iv-1.0/hosp/poe_detail.csv'
prescriptions = 'csvs/mimic-iv-1.0/hosp/prescriptions.csv'
pharmacy = 'csvs/mimic-iv-1.0/hosp/pharmacy.csv'
procedures_icd = 'csvs/mimic-iv-1.0/hosp/procedures_icd.csv'
services = 'csvs/mimic-iv-1.0/hosp/services.csv'

#ICU
d_items = 'csvs/mimic-iv-1.0/icu/d_items.csv'
procedureevents = 'csvs/mimic-iv-1.0/icu/procedureevents.csv'
outputevents = 'csvs/mimic-iv-1.0/icu/outputevents.csv'
inputevents = 'csvs/mimic-iv-1.0/icu/inputevents.csv'
icustays = 'csvs/mimic-iv-1.0/icu/icustays.csv'
datetimeevents = 'csvs/mimic-iv-1.0/icu/datetimeevents.csv'
chartevents = 'csvs/mimic-iv-1.0/icu/chartevents.csv'

#CXR

mimic_cxr_chexpert = 'csvs/mimic-cxr-jpg-chest-radiographs-with-structured-labels-2.0.0/mimic-cxr-2.0.0-chexpert.csv'
mimic_cxr_metadata = 'csvs/mimic-cxr-jpg-chest-radiographs-with-structured-labels-2.0.0/mimic-cxr-2.0.0-metadata.csv'
mimic_cxr_negbio = 'csvs/mimic-cxr-jpg-chest-radiographs-with-structured-labels-2.0.0/mimic-cxr-2.0.0-negbio.csv'
mimic_cxr_split = 'csvs/mimic-cxr-jpg-chest-radiographs-with-structured-labels-2.0.0/mimic-cxr-2.0.0-split.csv'

#Tables

tables = [admissions,patients,transfers]


#Sample10 patients
cohort = [10004235, 10004720, 10019003, 10020852, 10023708, 10031358, 10035631, 10046166, 10047172, 10051990]


icu_cxr_patients_sample10 = 'csvs/icu_cxr_patients_sample10.csv'

# Example of subject_id in icu and cxr:

subject_id_example = 10216097

# Chart events of interest
# This is the original list from the HAIM study. To make the calculations lighter for a tutorial or demo, use the reduced list
"""
chart_event_list = ['Heart Rate','Non Invasive Blood Pressure systolic',
                    'Non Invasive Blood Pressure diastolic', 'Non Invasive Blood Pressure mean', 
                    'Respiratory Rate','O2 saturation pulseoxymetry', 
                    'GCS - Verbal Response', 'GCS - Eye Opening', 'GCS - Motor Response'] 
"""

# Reduced list of Chart events of interest
chart_event_list = ['Heart Rate','Non Invasive Blood Pressure systolic'] 


# Lab events of interest
# This is the original list from the HAIM study. To make the calculations lighter for a tutorial or demo, use the reduced list
"""
lab_event_list = ['Glucose', 'Potassium', 'Sodium', 'Chloride', 'Creatinine',
           'Urea Nitrogen', 'Bicarbonate', 'Anion Gap', 'Hemoglobin', 'Hematocrit',
           'Magnesium', 'Platelet Count', 'Phosphate', 'White Blood Cells',
           'Calcium, Total', 'MCH', 'Red Blood Cells', 'MCHC', 'MCV', 'RDW', 
                      'Platelet Count', 'Neutrophils', 'Vancomycin']
"""
# Reduced list of Lab events of interest
lab_event_list = ['Glucose', 'Potassium', 'Sodium']



# Procedure events of interest
# This is the original list from the HAIM study. To make the calculations lighter for a tutorial or demo, use the reduced list
"""
procedure_event_list = ['Foley Catheter', 'PICC Line', 'Intubation', 'Peritoneal Dialysis', 
                            'Bronchoscopy', 'EEG', 'Dialysis - CRRT', 'Dialysis Catheter', 
                            'Chest Tube Removed', 'Hemodialysis']
"""

# Reduced list of procedure events of interest
procedure_event_list = ['Foley Catheter', 'PICC Line', 'Intubation']



# TSFRESH FC PARAMETERS
# The number of these parameters can be reduced depending on the user's goals
fc_parameters = {"length": None,
                    "absolute_sum_of_changes": None, 
                    "maximum": None, 
                    "mean": None,
                    "mean_abs_change": None,
                    "mean_change": None,
                    "median": None,
                    "minimum": None,
                    "standard_deviation": None,
                    "variance": None,
                    "large_standard_deviation": [{"r": r * 0.2} for r in range(1, 5)],
                    "quantile": [{"q": q} for q in [.25, .5, .75, 1]],
                    "linear_trend": [{"attr": "pvalue"}, {"attr": "rvalue"}, {"attr": "intercept"},{"attr": "slope"}, {"attr": "stderr"}]}

# NROWS to avoid memory issues in jupyter notebook
NROWS = 50000000


## Dicom sample images 
image_path_folder = 'dicom sample images/'
df_10_dicoms = 'csvs/df_mimic_cxr_metadata_sample_10_dicoms.csv'
sample_images = ["074987b9-26c19a32-5d80ebab-28a2fb1c-6191b91f",\
"53a0e91c-79580b39-f184232b-f105311f-eb2e51d2",\
"60f2347b-99b4129d-95de2c7b-ee5cb73c-806efa60",\
"e89d7fd0-52d0afc7-097fc4dc-3b7342d3-14b97733",\
"2026c1e8-873a009a-a6c9549d-a2e8e77f-5266ac77",\
"1dfc725a-fb67044b-37c88c4e-e4a80288-18a92be0",\
"0f33d2cc-cba96c64-8d40983e-4b2a2264-6ff6d3a5",\
"abea5eb9-b7c32823-3a14c5ca-77868030-69c83139",\
"43d968ea-b9b838af-5e4a8bef-c5a4808b-04aa4e2c",\
"457bdad8-c45edc64-452fde8e-f5adda5c-f386693e"]

##fusion_ts_dem_dataframe.csv that contains features from demographics, chart events, lab events and procedure events
fusion_ts_dem_dataframe = 'csvs/fusion_ts_dem_dataframe.csv'

##fusion_vision.csv that contains features from images
fusion_vision_dataframe = 'csvs/fusion_vision.csv'


