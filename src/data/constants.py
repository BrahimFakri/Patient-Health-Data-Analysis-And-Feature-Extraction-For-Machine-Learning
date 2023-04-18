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
chart_event_list = ['Heart Rate','Non Invasive Blood Pressure systolic',
                    'Non Invasive Blood Pressure diastolic', 'Non Invasive Blood Pressure mean', 
                    'Respiratory Rate','O2 saturation pulseoxymetry', 
                    'GCS - Verbal Response', 'GCS - Eye Opening', 'GCS - Motor Response'] 

# Chart events of interest
lab_event_list = ['Glucose', 'Potassium', 'Sodium', 'Chloride', 'Creatinine',
           'Urea Nitrogen', 'Bicarbonate', 'Anion Gap', 'Hemoglobin', 'Hematocrit',
           'Magnesium', 'Platelet Count', 'Phosphate', 'White Blood Cells',
           'Calcium, Total', 'MCH', 'Red Blood Cells', 'MCHC', 'MCV', 'RDW', 
                      'Platelet Count', 'Neutrophils', 'Vancomycin']

# Procedure events of interest
procedure_event_list = ['Foley Catheter', 'PICC Line', 'Intubation', 'Peritoneal Dialysis', 
                            'Bronchoscopy', 'EEG', 'Dialysis - CRRT', 'Dialysis Catheter', 
                            'Chest Tube Removed', 'Hemodialysis']

# TSFRESH FC PARAMETERS
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


