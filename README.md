# Singapore Resale Flat Prices Predicting

### **DOMAIN**: Real Estate

## **Problem Statement:**
    
  The objective of this project is to develop a machine learning model and deploy it as a user-friendly web application that predicts the resale prices of flats in Singapore. This predictive model will be based on historical data of resale flat transactions, and it aims to assist both potential buyers and sellers in estimating the resale value of a flat.

## **Motivation:**

The resale flat market in Singapore is highly competitive, and it can be challenging to accurately estimate the resale value of a flat. There are many factors that can affect resale prices, such as location, flat type, floor area, and lease duration. A predictive model can help to overcome these challenges by providing users with an estimated resale price based on these factors.

## **Skills:**
- Data Wrangling
- EDA
- Model building
- Model Deployment

## **Scope:**
- Data Collection and Preprocessing
- Feature Engineering
- Model selection and Training
- Model Evaluation
- Streamlit web Application
- Deployment on Render
- Testing and validation

## Prerequisites
1. **Python** -- Programming Language
2. **pandas** -- Python Library for Data Visualization
3. **numpy** --  Fundamental Python package for scientific computing in Python
4. **streamlit** -- Python framework to rapidly build and share beautiful machine learning and data science web apps
5. **scikit-learn** -- Machine Learning library for the Python programming language

### Data Source
**Link** : https://beta.data.gov.sg/collections/189/view
<br/>

## Project Workflow
The following is a fundamental outline of the project:
  - The Resale Flat Prices dataset has five distinct CSV files, each representing a specific time period. These time periods are 1990 to 1999, 2000 to 2012, 2012 to 2014, 2015 to 2016, and 2017 onwards. Therefore, it is essential to merge the five distinct CSV files into a unified dataset.
    
  - The data will be converted into a format that is appropriate for analysis, and any required cleaning and pre-processing procedures will be carried out. Relevant features from the dataset, including town, flat type, storey range, floor area, flat model, and lease commence date will be extracted. Any additional features that may enhance prediction accuracy will also be created.
    
  - The objective of this study is to construct a machine learning regression model that utilizes the decision tree regressor to accurately forecast the continuous variable 'resale_price'.
    
  - The objective is to develop a Streamlit webpage that enables users to input values for each column and get the expected resale_price value for the flats in Singapore.
