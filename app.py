import streamlit as st
import joblib
import pandas as pd
import numpy as np


# Eğitilmiş modeli yükle
model = joblib.load("resolve_model.pkl")


# --------------------------------------------------
# Dataset'teki gerçek değerler
# --------------------------------------------------

categories = [
    "Waste, Street Cleaning and Litter",
    "Graffiti",
    "Parks and Trees",
    "Roads and Traffic",
    "Parking",
    "Asset maintenance"
]

service_types = [
    "Graffiti Removal",
    "Missed Bin Collection",
    "Dumped Rubbish",
    "Tree Maintenance Services",
    "Road and Footpath Maintenance",
    "Waste collection services",
    "Damaged Bins",
    "Missing Bin",
    "Traffic Management",
    "Condition of Assets in Parks",
    "Public Litter Bin",
    "Street Cleaning services",
    "Park Cleaning",
    "Parking Meter Service",
    "Syringe pick-up services",
    "Parking Compliance Services",
    "Street Maintenance",
    "Lawns and Irrigation",
    "Drain Maintenance",
    "Street Lighting Maintenance",
    "Sport and Playground Facilities",
    "Public Toilets",
    "Bridge Maintenance",
    "Bike pod services",
    "Waste Compactor",
    "Organic Waste",
    "Waterways"
]

suburbs = [
    "Melbourne",
    "Carlton",
    "North Melbourne",
    "Kensington",
    "East Melbourne",
    "Parkville",
    "West Melbourne",
    "South Yarra",
    "Southbank",
    "Docklands",
    "Carlton North",
    "Port Melbourne",
    "Flemington",
    "South Wharf",
    "Unknown"
]

years = [2014, 2015, 2016]

days_of_week = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6
}


# --------------------------------------------------
# Arayüz
# --------------------------------------------------

st.title("Resolve")

st.write(
    "Customer Service Resolution Time Prediction"
)

st.subheader("Enter Request Information")


category = st.selectbox(
    "Category",
    categories
)


service_desc = st.selectbox(
    "Service Type",
    service_types
)


suburb = st.selectbox(
    "Suburb",
    suburbs
)


received_year = st.selectbox(
    "Received Year",
    years
)


received_month = st.selectbox(
    "Received Month",
    range(1, 13)
)


selected_day = st.selectbox(
    "Day of Week",
    list(days_of_week.keys())
)


received_day_of_week = days_of_week[selected_day]


# --------------------------------------------------
# Tahmin
# --------------------------------------------------

if st.button("Predict Resolution Time"):

    if suburb == "Unknown":
        suburb = None

    input_data = pd.DataFrame({
        "category": [category],
        "service_desc": [service_desc],
        "suburb": [suburb],
        "received_year": [received_year],
        "received_month": [received_month],
        "received_day_of_week": [received_day_of_week]
    })

    prediction_log = model.predict(input_data)

    prediction = np.expm1(prediction_log)[0]

    st.success(
        f"Estimated resolution time: {prediction:.1f} days"
    )