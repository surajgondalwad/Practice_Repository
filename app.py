import streamlit as st
import pandas as pd
import numpy as np
import pickle
import kagglehub

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="Car Price Predictor 🚗",
    page_icon="🚗",
    layout="wide"
)

# -------------------------------
# Load Model
# -------------------------------
@st.cache_resource
def load_model():
    with open("Practice_Model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

model = load_model()

# -------------------------------
# Load Dataset (for reference)
# -------------------------------
@st.cache_data
def load_data():
    path = kagglehub.dataset_download(
        "ihasan88/car-price-prediction-and-vehicle-specifications"
    )
    df = pd.read_csv(path + "/car_price_dataset.csv")  # adjust if filename differs
    return df

df = load_data()

# -------------------------------
# Title Section
# -------------------------------
st.title("🚗 Car Price Prediction App")
st.markdown("Predict the price of a car using Machine Learning")

st.divider()

# -------------------------------
# Sidebar Inputs
# -------------------------------
st.sidebar.header("⚙️ Enter Car Details")

# NOTE: adjust based on your model features
year = st.sidebar.slider("Year", 2000, 2025, 2015)
engine_size = st.sidebar.slider("Engine Size (L)", 1.0, 6.0, 2.0)
horsepower = st.sidebar.slider("Horsepower", 50, 500, 150)
mileage = st.sidebar.slider("Mileage (km/l)", 5, 40, 15)

fuel_type = st.sidebar.selectbox("Fuel Type", ["Petrol", "Diesel", "Electric"])
transmission = st.sidebar.selectbox("Transmission", ["Manual", "Automatic"])

# Encode categorical (simple example)
fuel_map = {"Petrol": 0, "Diesel": 1, "Electric": 2}
trans_map = {"Manual": 0, "Automatic": 1}

# -------------------------------
# Prepare Input Data
# -------------------------------
input_data = np.array([[
    year,
    engine_size,
    horsepower,
    mileage,
    fuel_map[fuel_type],
    trans_map[transmission]
]])

# -------------------------------
# Prediction Section
# -------------------------------
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📊 Prediction Result")

    if st.button("🚀 Predict Price"):
        prediction = model.predict(input_data)

        st.success(f"💰 Estimated Car Price: ₹ {prediction[0]:,.2f}")

with col2:
    st.subheader("ℹ️ Model Info")
    st.info("This model predicts car prices based on specifications like engine, mileage, and more.")

# -------------------------------
# Data Preview Section
# -------------------------------
with st.expander("📂 View Dataset"):
    st.dataframe(df.head())

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")
