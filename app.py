import streamlit as st
import pandas as pd
import pickle
loaded_model = pickle.load(open('model.pkl', 'rb'))
col1, col2, col3 = st.columns(3)
with col1:
    age = st.number_input('enter age')

with col2:
    sex = st.number_input('enter sex')

with col3:
     ct = st.number_input('enter chestpain type')

col4, col5, col6 = st.columns(3)
with col4:
    cl = st.number_input('cholestrol')

with col5:
    fb = st.number_input('fasting bs')

with col6:
    mh = st.number_input('maxHR')

col7, col8, col9 = st.columns(3)
with col7:
    ea = st.number_input('exercise angina')

with col8:
    op = st.number_input('oldpeak')

with col9:
    ss = st.number_input('st_slope')


if st.button('Predict Score'):
    input_df = pd.DataFrame(
        {'Age': [age], 'Sex': [sex], 'ChestPainType': [ct], 'Cholesterol': [cl],
         'FastingBS': [fb], 'MaxHR': [mh], 'ExerciseAngina': [ea], 'Oldpeak': [op], 'ST_Slope': [ss]})
    input_model = input_df.values
    result = loaded_model.predict(input_model)
    if result == 1:
        st.header("result positive ")
    else:
        st.header("negative")
    