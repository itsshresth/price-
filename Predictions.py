import streamlit as st
import pandas as pd
import numpy as np
import joblib
from cars_notebook import cars_price_predictor
from banglore_home_prices_final import predict_house_price

st.set_page_config(page_title="Commodity Price Predictor", page_icon=None, layout="centered", initial_sidebar_state="auto")

st.title("Commodity Price Predictor")

commodity = st.selectbox("Select Commodity", ["Car", "House", "Laptop"])

@st.cache_data
def load_laptop_data():
    df = joblib.load('df.pkl')
    pipe = joblib.load('pipe.pkl')
    return df, pipe

if commodity == "Car":
    company = st.selectbox("Car company", ["Maruti", "Hyundai", "Mahindra", "Tata", "Honda", "Toyota", "Chevrolet", "Renault", "Ford", "Volkswagen", "Skoda", "Audi", "Mini", "BMW", "Datsun", "Mitsubishi", "Nissan", "Mercedes", "Fiat", "Force", "Hindustan", "Jaguar", "Land", "Jeep", "Volvo"])
    year = st.number_input("Year of manufacture", min_value=2005, max_value=2024, value=2015)
    kms = st.number_input("Kilometers driven", min_value=0, value=10000)
    car_type = st.selectbox("Fuel type", ["Petrol", "Diesel", "LPG"])
    if st.button("Predict Price"):
        predicted_price = cars_price_predictor(company, year, kms, car_type)
        predicted_price = round(int(predicted_price))
        st.success(f"Predicted Car Price: ₹{predicted_price}")

elif commodity == "House":
    locations_df = pd.read_csv("locations.csv")
    location_columns = locations_df['Location'].tolist()
    location = st.selectbox("Location (Bangalore)", location_columns)
    sqft = st.number_input("Area (sqft)", min_value=1, value=1000)
    bath = st.number_input("Bathrooms", min_value=1, value=2)
    bhk = st.number_input("BHK (Bedrooms)", min_value=1, value=2)
    if st.button("Predict Price"):
        predicted_price = predict_house_price(location, sqft, bath, bhk)
        predicted_price = round(int(predicted_price))
        st.success(f"Predicted House Price: ₹{predicted_price}")

elif commodity == "Laptop":
    df, pipe = load_laptop_data()
    company = st.selectbox("Brand", df['Company'].unique())
    typename = st.selectbox("Type", df['TypeName'].unique())
    ram = st.selectbox("RAM (GB)", [2, 4, 6, 8, 12, 16, 24, 32, 64])
    weight = st.number_input("Weight (kg)", value=2.0)
    touchscreen = st.selectbox('TouchScreen', ['No', 'Yes'])
    ips = st.selectbox('IPS', ['No', 'Yes'])
    screen_size = st.number_input('Screen Size (inches)', value=15.6)
    resolution = st.selectbox('Screen Resolution', ['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', '2880x1800', '2560x1600', '2560x1440', '2304x1440'])
    cpu = st.selectbox('CPU Brand', df['Cpu brand'].unique())
    hdd = st.selectbox('HDD (GB)', [0, 128, 256, 512, 1024, 2048])
    ssd = st.selectbox('SSD (GB)', [0, 8, 128, 256, 512, 1024])
    gpu = st.selectbox('GPU', df['Gpu brand'].unique())
    os = st.selectbox('OS', df['os'].unique())
    if st.button("Predict Price"):
        t = 1 if touchscreen == 'Yes' else 0
        i = 1 if ips == 'Yes' else 0
        X_res = int(resolution.split('x')[0])
        Y_res = int(resolution.split('x')[1])
        ppi = ((X_res**2) + (Y_res**2))**0.5 / screen_size
        query = np.array([company, typename, ram, weight, t, i, ppi, cpu, hdd, ssd, gpu, os])
        query = query.reshape(1, 12)
        predicted_price = np.exp(pipe.predict(query))
        predicted_price = round(int(predicted_price))
        st.success(f"Predicted Laptop Price: ₹{predicted_price}")





