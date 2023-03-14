## Introduction

This is an open-source python repository that is based on the the [HAIM GitHub package](https://github.com/lrsoenksen/HAIM.git) study. 
We here try to replicate the embeddings generation from the [HAIM multimodal dataset](https://physionet.org/content/haim-multimodal/1.0.1/) containing data of 4 modalities (tabular, time-series, text and images) and 11 unique sources.

For more details about the different tables and column names, please refere to MIMIC video tutorials at : [MIMIC Tutorial](https://mimic.mit.edu/docs/iv/tutorials/video/)


Below is an overview of the different MIMIC modules and their link to different patient movements throught the hospital: 

![image](https://user-images.githubusercontent.com/119059452/218730593-784ea8a1-cc9c-440e-a30f-9595b2be212b.png)

(Johnson, A., Bulgarelli, L., Pollard, T., Horng, S., Celi, L. A., & Mark, R. (2021). MIMIC-IV (version 1.0).PhysioNet. https://doi.org/10.13026/s6n6-xd98.).

## Relationship between different mimiv core and icu tables


![Relationship diagram](https://user-images.githubusercontent.com/119059452/222306118-e92ee85d-18e3-4eaa-99dd-d252dc876735.png)



## Some important data facts



![image](https://user-images.githubusercontent.com/119059452/218784248-d562515f-7e85-49d7-a359-285e63093aea.png)




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
For the predictions based on the original HAIM embeddings, please refer to the work of Hakima Laribi [HAIM](https://github.com/MEDomics-UdeS/HAIM).

