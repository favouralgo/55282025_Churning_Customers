# -*- coding: utf-8 -*-
"""
Edited on VS Code
@author: Favour Madubuko
"""
import pickle
import numpy as np
import streamlit as strl
import tensorflow
from tensorflow.keras.models import load_model
model = load_model('churn_customers_prediction.h5')



with open("customers.pkl", "rb") as f:
    scaler = pickle.load(f)
    
def scale_numericalvariables(tenure, MonthlyCharges, TotalCharges):
    """
    Scales the numerical variables using the scaler object.

    Parameters:
    tenure (float): The tenure of the customer.
    MonthlyCharges (float): The monthly charges of the customer.
    TotalCharges (float): The total charges of the customer.

    Returns:
    scaled_numericvariables (array-like): The scaled numerical variables.
    """
    scaled_numericvariables = scaler.transform([[tenure, MonthlyCharges, TotalCharges]])
    return scaled_numericvariables

# Opening the file 
with open("customerCategories.pkl", "rb") as file:
    label_encoder = pickle.load(file)

def churn_prediction(input_data):
    #input_data = [tenure,MonthlyCharges,TotalCharges,gender,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,Contract,PaperlessBilling,PaymentMethod]
    # Prediction
    predicted_churn = model.predict(input_data) #np.array([input_data])
    return predicted_churn[0][0]    
    



def main():
    col1, col2, col3,col4 = strl.columns(4)
    col1.metric("Test Accuracy", "81.8%","0.2%")
    col2.metric("Validation Accuracy", "80.11%","0.2%")
    col3.metric("Test AUC Score", "86.3%","0.2%")
    col4.metric("Validation AUC Score", "84.8%","0.2%")



    # giving a title to the app
    strl.title('CUSTOMER CHURN PREDICTION APP')
    
    # Numerical variables
    tenure = strl.number_input('How many months have you stayed with the company?') 
    MonthlyCharges = strl.number_input('How much do you pay monthly?')
    TotalCharges = strl.number_input('What is the total charges incurred in a month/year')
    
    # Categorical variables
    gender = strl.selectbox('Select your gender', ('Male', 'Female')) # 1, 0
    if gender=='Male':gender=1
    else: gender=0

    MultipleLines = strl.selectbox('Do you use multiple phone lines?',['No phone service','No','Yes']) # 1, 0, 2
    if MultipleLines == 'No phone service': MultipleLines=1
    elif MultipleLines == 'No':MultipleLines=0
    else: MultipleLines =2

    InternetService = strl.selectbox('Who is your internet service provider?',['DSL','Fiber optic','No Provider']) # 0, 1, 2
    if InternetService=='DSL':InternetService=0
    elif InternetService=='Fiber optic':InternetService=1
    else: InternetService=2

    OnlineSecurity = strl.selectbox('Do you have online security?',['No','No Internet Service', 'Yes']) # 0 , 1, 2
    if OnlineSecurity=='No':OnlineSecurity=0
    elif OnlineSecurity=='No Internet Service':OnlineSecurity=1
    else: OnlineSecurity=2
    
    OnlineBackup = strl.selectbox('Do you have online backup?',['No','No Internet Service','Yes']) # 0, 1 ,2
    if OnlineBackup=='No':OnlineBackup=0
    elif OnlineBackup=='No Internet Service': OnlineBackup=1
    else: OnlineBackup=2

    DeviceProtection = strl.selectbox('Does your device have protection?',['No','No Internet Service','Yes']) # 0, 1 , 2
    if DeviceProtection=='No':DeviceProtection=0
    elif DeviceProtection=='No Internet Service': DeviceProtection=1
    else: DeviceProtection=2
    
    TechSupport = strl.selectbox('Are you satisfied with the tech support?',['No','No Internet Service','Yes']) # 0, 1 , 2
    if TechSupport=='No':TechSupport=0
    elif TechSupport=='No Internet Service':TechSupport=0
    else: TechSupport=2
    
    Contract = strl.selectbox('Select your contract term',['Month-to-Month','One Year','Two Year'])    # 0, 1 , 2
    if Contract=='Month-to-Month':Contract=0
    elif Contract=='One Year':Contract=1
    else: Contract=2
    
    PaperlessBilling = strl.selectbox('Do you use paperless billing?',['No','Yes']) # 0, 1
    if PaperlessBilling=='No':PaperlessBilling=0
    else: PaperlessBilling=1
    
    PaymentMethod = strl.selectbox('Select payment method that you use?',['Bank Transfer (automatic)','Credit Card (automatic)','Electronic check','Mailed check']) #0, 1, 2, 3  
    if PaymentMethod=='Bank Transfer (automatic)':PaymentMethod=0
    elif PaymentMethod=='Credit Card (automatic)':PaymentMethod=1
    elif PaymentMethod=='Electronic check':PaymentMethod=2
    else: PaymentMethod=2

    
    input_data_numerical = scale_numericalvariables(tenure, MonthlyCharges, TotalCharges)
    input_data_categorical = np.array([gender, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, Contract, PaperlessBilling, PaymentMethod])

    input_data = np.concatenate([input_data_numerical, input_data_categorical.reshape(1, -1)], axis=1)

    # creating a button for prediction
    if strl.button('Predict Churn'):
        predicted_value = churn_prediction(input_data)
        threshold = 0.40
        if predicted_value >= threshold:
            strl.success("This customer is likely to churn")
        else:
            strl.error("This customer is not likely to churn")
        # Calculating the confidence factor formula is given as: 1 - abs(predicted_value - threshold)
        confidence_factor = 1 - abs(predicted_value - threshold)
        strl.success(f'The confidence factor of this prediction is: {round(confidence_factor,2) * 100}%')



# calling the main function to display the result    
if __name__ == '__main__':
    main()