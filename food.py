import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier



with open('model.pkl','rb+') as file:
    model= pickle.load(file)

def predict(age, gender, marital_status, occupation, monthly_income, family_size, feedback):
    
    user_input = np.array([[age, gender, marital_status, occupation, monthly_income, family_size, feedback]])
    
    
    prediction = model.predict(age, gender, marital_status, occupation, monthly_income, family_size, feedback)

    
    prediction = prediction[0]

    return prediction
