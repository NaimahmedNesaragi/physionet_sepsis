#!/usr/bin/env python

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib

def create_features(data):
    columns = ['HR', 'O2Sat', 'Temp', 'SBP', 'MAP', 'DBP', 'Resp', 'EtCO2',
       'BaseExcess', 'HCO3', 'FiO2', 'pH', 'PaCO2', 'SaO2', 'AST', 'BUN',
       'Alkalinephos', 'Calcium', 'Chloride', 'Creatinine', 'Bilirubin_direct',
       'Glucose', 'Lactate', 'Magnesium', 'Phosphate', 'Potassium',
       'Bilirubin_total', 'TroponinI', 'Hct', 'Hgb', 'PTT', 'WBC',
       'Fibrinogen', 'Platelets', 'Age', 'Gender', 'Unit1', 'Unit2',
       'HospAdmTime', 'ICULOS']

    df = pd.DataFrame(data=data, columns=columns)
    df.drop('EtCO2', axis=1, inplace=True)
#     print(df)
    df = df.ffill().bfill()
#     print(np.nan_to_num(df))
#     df['shock_index'] = df['HR'] / df['SBP']
#     df['BUN/CR'] = df['BUN'] / df['Creatinine']
#     print(df.values)
    return np.nan_to_num(df)

def get_sepsis_score(data, model):

    data = create_features(data)
    score = model.predict_proba(data)
    probability = score[-1][-1]
    label = np.argmax(score[-1])
    return probability, label

def load_sepsis_model():
    loaded_model = joblib.load('RF_model.sav')
    return loaded_model