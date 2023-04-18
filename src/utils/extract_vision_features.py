"""
Filename: extract_vision_features.py
Author : 

Joseph Paul Cohen, Joseph D. Viviano, Paul Bertin, Paul Morrison, Parsa Torabian, Matteo Guarrera, Matthew P Lungren, Akshay Chaudhari, Rupert Brooks, Mohammad Hashir, Hadrien Bertrand
TorchXRayVision: A library of chest X-ray datasets and models. 
Medical Imaging with Deep Learning
https://github.com/mlmed/torchxrayvision, 2020

Description: This file is an adaptation from torchxrayvision used to vision image embeddings  extraction
Date of last modification : 2023/04/18
"""

import torchxrayvision as xrv

import skimage
import cv2
import torch

import torch.nn.functional as F

import pandas as pd
import numpy as np

import os
from os import listdir

import os
os.chdir('../')

from src.data import constants
from src.utils import extract_vision_features


def extract_vision_features(img):

  #Initialize the densefeature_embeddings with an empty list:
  densefeature_embeddings = []

  #Initialize the prediction_embeddings with an empty list:
  prediction_embeddings = []

  # Select model 
  model = xrv.models.DenseNet(weights = "densenet121-res224-chex")

  #process image
  #https://github.com/mlmed/torchxrayvision/blob/0eafebf36a3f5f30302dff0faaacef5e52243e87/scripts/process_image.py
  
  img = xrv.datasets.normalize(img, 255)
  img = cv2.resize(img, (224, 224), interpolation = cv2.INTER_AREA)   
  img = img[None, :, :]
  
  with torch.no_grad():
    img = torch.from_numpy(img).unsqueeze(0)
          
    # Extract dense features
    feats = model.features(img)
    feats = F.relu(feats, inplace=True)
    feats = F.adaptive_avg_pool2d(feats, (1, 1))
    densefeatures = feats.cpu().detach().numpy().reshape(-1)
    densefeature_embeddings = densefeatures

    # Extract predicted probabilities of considered 18 classes:
    preds = model(img).cpu()
    predictions = preds[0].detach().numpy()
    prediction_embeddings = predictions    

    df_vision_dense_embeddings_fusion = pd.DataFrame(densefeature_embeddings.reshape(1,-1), columns=['vd_'+str(i) for i in range(densefeature_embeddings.shape[0])])


    df_vision_predictions_embeddings_fusion = pd.DataFrame(prediction_embeddings.reshape(1,-1), columns=['vp_'+str(i) for i in range(prediction_embeddings.shape[0])])


    return df_vision_predictions_embeddings_fusion , df_vision_dense_embeddings_fusion
