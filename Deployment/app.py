import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Concrete CS Estimator",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://google.com',
        'Report a bug': "https://github.com/4dhil",
        'About': " App for predicting Concrete Strength"
    }
)

st.header('Concrete Compressive Strength Predictor')
st.write("""
Created by Fadhil Muhammad Irfan FTDS-10
""")

def user_input():
    cement = st.number_input('Cement (component 1)(kg in a m^3 mixture)', value=67.00)
    slag = st.number_input('Blast Furnace Slag (component 2)(kg in a m^3 mixture)', 0.0, value=91.0)
    flyash = st.number_input('Fly Ash (component 3)(kg in a m^3 mixture)', 0.0, value=91.0)
    water = st.number_input('Water  (component 4)(kg in a m^3 mixture)', 0.0, value=58.0)
    superplasticizer = st.number_input('Superplasticizer (component 5)(kg in a m^3 mixture)',  0.0, value=58.0)
    coarseaggregate = st.number_input('Coarse Aggregate  (component 6)(kg in a m^3 mixture)',  0.0, value=58.0)
    fineaggregate = st.number_input('Fine Aggregate (component 7)(kg in a m^3 mixture)', 0.0, value=78.00)
    age = st.number_input('age (days) ',  0.0, value=58.0)

    data = {
        'cement': cement,
        'slag': slag,
        'flyash': flyash,
        'water': water,
        'superplasticizer': superplasticizer,
        'coarseaggregate': coarseaggregate,
        'fineaggregate': fineaggregate,
        'age': age,
    }
    features = pd.DataFrame(data, index=[0])
    return features


input = user_input()

st.subheader('User Input')
st.write(input)

load_model = joblib.load("model.pkl")

prediction = load_model.predict(input)

st.write('Based on user input, the model predicted that the concrete will have a quality of: ')
st.write(prediction)

st.write('Result is in MegaPascal (MPa)')

st.write("""
**Data used to train the predicting model:**

https://archive.ics.uci.edu/ml/datasets/concrete+compressive+strength
""")