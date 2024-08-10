# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 22:37:02 2024

@author: Chaitanya
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Loading the Model
Gold_price_pred_model = pickle.load(open("C:/Users/Chaitanya/Data Science and AI/Data Science Projects/Gold price prediction model using ML/gold_price_prediction.sav", "rb"))

# Gold price prediction page

st.title("Gold Price Prediction using ML")

# Getting input from the user

SPX = st.text_input("SPX")

USO = st.text_input("USO")

SLV = st.text_input("SLV")

EUR_or_USD = st.text_input("EUR/USD")

# Button for seeing the result
gold_out = ""
if st.button("Gold Price Prediction Result"):
    
   gold_pred = Gold_price_pred_model.predict([[SPX,USO,SLV,EUR_or_USD]])
   gold_out = gold_pred
    
st.success(gold_out)  

