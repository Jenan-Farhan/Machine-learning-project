# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np 
import pickle
import streamlit as st 
#from sklearn.tree import DecisionTreeRegressor

# loading the saved mode1
loaded_mode1 = pickle.load(open('C:/Users/LENOVO/Desktop/Price.sav','rb'))

# function 
def car (input_data): 
     input_data_as_numpy_array = np.asarray(input_data)
     
     input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
     
     prediction = loaded_mode1.predict(input_data_reshaped)
     return(prediction)
 
    
def main():
    
    st.title('Selling_Price_Car')
    
    Car_Name = st.text_input("Enter the name of car:")
    Year = st.text_input("Enter the year:")
    Present_Price = st.text_input("Enter the Present Price:")
    Kms_Driven = st.text_input("Enter the Kms Driven:")
    Fuel_Type = st.text_input("Enter the Fuel Type:")
    Seller_Type = st.text_input("Enter the  Seller Type: ")
    Transmission = st.text_input("Enter the  Transmission: ")
    Owner = st.text_input("Enter the Owner: ")
    
    dignosis = ""
    # creating a button for perdiction
    if st.button('Diabetes test Result'):
        dignosis = car([Car_Name,Year,Present_Price,Kms_Driven,Fuel_Type,Seller_Type,Transmission,Owner])

    st.success(dignosis)

if __name__ == '__main__':
    main()
