## Introduction

This is an open-source python repository that is based on the the [HAIM GitHub package](https://github.com/lrsoenksen/HAIM.git) study. 
We here try to replicate the embeddings generation from the [HAIM multimodal dataset](https://physionet.org/content/haim-multimodal/1.0.1/) containing data of 4 modalities (tabular, time-series, text and images) and 11 unique sources.

For more details about the different tables and column names, please refere to MIMIC video tutorials at : (https://mimic.mit.edu/docs/iv/tutorials/video/)

(Johnson, A., Bulgarelli, L., Pollard, T., Horng, S., Celi, L. A., & Mark, R. (2021). MIMIC-IV (version 1.0). PhysioNet. https://doi.org/10.13026/s6n6-xd98.)


Below is an overview of the different MIMIC modules and their link to different patient movements throught the hospital: 

![image](https://user-images.githubusercontent.com/119059452/218730593-784ea8a1-cc9c-440e-a30f-9595b2be212b.png)


## General data exploratory analysis


![image](https://user-images.githubusercontent.com/119059452/218734792-5f59156f-e808-483f-8cdb-f22b1b7909d9.png)



## Instructions on how to use the codes in the repository

The datasets used to replicate the embeddings generation are publicly available at: [physionet](https://physionet.org/content/haim-multimodal/1.0.1/). 

Download:
- MIMIC-CXR-JPG - chest radiographs with structured labels v2.0.0 (https://physionet.org/content/mimic-cxr-jpg/2.0.0/)
- MIMIC-IV v1.0 (https://physionet.org/content/mimiciv/1.0/

Copy the unzipped folders  to [csvs](csvs)
