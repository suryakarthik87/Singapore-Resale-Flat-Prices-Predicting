# Import necessary libraries
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeRegressor
import streamlit as st
import joblib
from streamlit_option_menu import option_menu


# Streamlit Application
st.set_page_config(page_title='Singapore Flat Resale Price Predictor', layout='wide',
                   initial_sidebar_state='expanded')

st.markdown("<h1 style='text-align: center; color: green;'>Singapore Flat Resale Price Predicton</h1>",unsafe_allow_html=True)

with st.sidebar:
    selected = option_menu("Menu",["Home", "Prediction"])


if selected == "Home":


    st.write('## :red[Problem Statement]')
    st.write('''The resale flat market in Singapore is highly competitive, and it can be challenging to accurately estimate the resale value of a flat.
                There are many factors that can affect resale prices, such as location, flat type, floor area, and lease duration.''')
    st.write(''' This predictive model will be based on historical data of resale flat transactions, and it aims to assist both potential buyers and sellers
              in estimating the resale value of a flat.''')
    st.write('## :red[Objective]')
    st.write('The objective of this project is to develop a machine learning model and deploy it as a user-friendly web application that predicts the resale prices of flats in Singapore. ')

    st.write('## :red[Tools and Technologies used]')
    st.write(' Python, Pandas, numpy, matplotlib, seaborn, Plotly, Streamlit, sklearn')
    st.write('## :red[Machine Learning Model]')
    st.write('The Machine Learning Model used in this project is :blue[Decision Tree Regressor].')
    st.write(' Comparing other regressors, Decision Tree Regressor had a high :red[R-squared score], which means it has performed best. ')


if selected == "Prediction":

    # Define unique values for select boxes
    flat_model_options = ['IMPROVED', 'NEW GENERATION', 'MODEL A', 'STANDARD', 'SIMPLIFIED',
                        'MODEL A-MAISONETTE', 'APARTMENT', 'MAISONETTE', 'TERRACE', '2-ROOM',
                        'IMPROVED-MAISONETTE', 'MULTI GENERATION', 'PREMIUM APARTMENT',
                        'ADJOINED FLAT', 'PREMIUM MAISONETTE', 'MODEL A2', 'DBSS', 'TYPE S1',
                        'TYPE S2', 'PREMIUM APARTMENT LOFT', '3GEN']
    flat_type_options = ['1 ROOM', '3 ROOM', '4 ROOM', '5 ROOM', '2 ROOM', 'EXECUTIVE', 'MULTI GENERATION']
    town_options = ['ANG MO KIO', 'BEDOK', 'BISHAN', 'BUKIT BATOK', 'BUKIT MERAH', 'BUKIT TIMAH',
                    'CENTRAL AREA', 'CHOA CHU KANG', 'CLEMENTI', 'GEYLANG', 'HOUGANG',
                    'JURONG EAST', 'JURONG WEST', 'KALLANG/WHAMPOA', 'MARINE PARADE',
                    'QUEENSTOWN', 'SENGKANG', 'SERANGOON', 'TAMPINES', 'TOA PAYOH', 'WOODLANDS',
                    'YISHUN', 'LIM CHU KANG', 'SEMBAWANG', 'BUKIT PANJANG', 'PASIR RIS', 'PUNGGOL']
    storey_range_options = ['10 TO 12', '04 TO 06', '07 TO 09', '01 TO 03', '13 TO 15', '19 TO 21',
                            '16 TO 18', '25 TO 27', '22 TO 24', '28 TO 30', '31 TO 33', '40 TO 42',
                            '37 TO 39', '34 TO 36', '46 TO 48', '43 TO 45', '49 TO 51']
    
    # Load the saved model
    model_filename = r'singapore_flats_decision_tree.joblib'
    pipeline = joblib.load(model_filename)

    # Create a Streamlit sidebar with input fields
  
    town = st.selectbox("Town", options=town_options)
    flat_type = st.selectbox("Flat Type", options=flat_type_options)
    flat_model = st.selectbox("Flat Model", options=flat_model_options)
    storey_range = st.selectbox("Storey Range", options=storey_range_options)
    floor_area_sqm = st.number_input("Floor Area (sqm)", min_value=0.0, max_value=500.0, value=100.0)
    lease_commence_date = st.number_input("Lease Commence Data", min_value=1966.0, max_value=2024.0, value=1990.0)
    year = 2024
    current_remaining_lease_count = lease_commence_date + 99 - year
    current_remaining_lease = st.number_input("Current Remaining Lease",current_remaining_lease_count)

    lease_commence_date = current_remaining_lease + year - 99
    years_holding = 99 - current_remaining_lease


    # Create a button to trigger the prediction
    if st.button("Predict Resale Price"):
    # Prepare input data for prediction
        input_data = pd.DataFrame({
            'town': [town],
            'flat_type': [flat_type],
            'flat_model': [flat_model],
            'storey_range': [storey_range],
            'floor_area_sqm': [floor_area_sqm],
            'current_remaining_lease': [current_remaining_lease],
            'lease_commence_date': [lease_commence_date],
            'years_holding': [years_holding],
            'remaining_lease': [current_remaining_lease],
            'year': [year]
        })

        # Make a prediction using the model
        prediction = pipeline.predict(input_data)

        # Display the prediction
        st.success(f"Resale Price: :red[SGD] :green[{prediction}]")  

