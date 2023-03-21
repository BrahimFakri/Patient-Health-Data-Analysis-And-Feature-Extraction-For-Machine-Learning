## Introduction

This is an open-source python repository that is based on the the [HAIM GitHub package](https://github.com/lrsoenksen/HAIM.git) study. 
We here try to replicate the embeddings generation from the [HAIM multimodal dataset](https://physionet.org/content/haim-multimodal/1.0.1/) containing data of 4 modalities (tabular, time-series, text and images) and 11 unique sources.

## Instructions on how to use the repository

The datasets used to replicate the embeddings generation are publicly available at: [physionet](https://physionet.org/content/haim-multimodal/1.0.1/). 

Download:
- MIMIC-CXR-JPG - chest radiographs with structured labels v2.0.0 (https://physionet.org/content/mimic-cxr-jpg/2.0.0/)
- MIMIC-IV v1.0 (https://physionet.org/content/mimiciv/1.0/

Copy the unzipped folders  to [csvs](csvs)

In order to generate embeddings, we based our codes on subject_id. The user can also opt for stay_id embeddings generation. However, this can generate 
multiple rows for the same patient in terms of time series analysis. 
Data related to time of events will be spread on multiple rows, and machine learning algorithms might generate erroneous predictions.


## Steps of our work

In this repository, we intent to gradually provide five jupyter notebooks. Each of the first four will be for a data modality and the last one will be for all modalities.

## Datasources description

For more details about the different tables and column names, please refere to MIMIC video tutorials at : [MIMIC Tutorial](https://mimic.mit.edu/docs/iv/tutorials/video/)


Below is an overview of the different MIMIC modules and their link to different patient movements through the hospital: 

![image](https://user-images.githubusercontent.com/119059452/218730593-784ea8a1-cc9c-440e-a30f-9595b2be212b.png)

(Johnson, A., Bulgarelli, L., Pollard, T., Horng, S., Celi, L. A., & Mark, R. (2021). MIMIC-IV (version 1.0).PhysioNet. https://doi.org/10.13026/s6n6-xd98.).

## Relationship between different mimiv core and icu tables


![Relationship diagram](https://user-images.githubusercontent.com/119059452/222306118-e92ee85d-18e3-4eaa-99dd-d252dc876735.png)



## Some important data facts

Below is table in which we summarize important information about the most important tables used in the embeddings generation.

To produce these number, we used the notebook ```general dataset exploration.ipynb``` in the folder [notebooks](notebooks)

![image](https://user-images.githubusercontent.com/119059452/218784248-d562515f-7e85-49d7-a359-285e63093aea.png)


The summary table shows for example that we have 382278 unique subject_id in the table patient (created from the csv file patients.csv). However, in the icustays table, we only have 53150 unique subject_id, meaning that not all patients in the database have icu stays.

Also, we notice that not all patients have chest radiology images: only 65379 unique subject_id in the mimic_cxr_chexpert table.

So in order to find the patients who have both icu stays and chest radiology images, we ran the notebook ```icu_cxr_patients.ipynb``` and find that the number of patients with both a chest radiology image and an icu stay is:  ```20245```





