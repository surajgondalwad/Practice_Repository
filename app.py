import streamlit as st
import pandas as pd
import numpy as np
import time

# --- PAGE CONFIG ---
st.set_page_config(page_title="AutoPrice Predictor", page_icon="🚗", layout="centered")

# --- CUSTOM CSS FOR SMOOTH UI ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #FF4B4B;
        color: white;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #ff3333;
        border: none;
    }
    .prediction-card {
        padding: 20px;
        background-color: white;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
    }
    </style>
    """, unsafe_allow_stdio=True)

# --- HEADER ---
st.title("🚗 Vehicle Price Predictor")
st.write("Enter the vehicle specifications below to estimate the market value.")

# --- SIDEBAR / INPUTS ---
with st.container():
    st.subheader("Vehicle Specifications")
    col1, col2 = st.columns(2)
    
    with col1:
        make = st.selectbox("Brand", ["Toyota", "Honda", "Ford", "BMW", "Audi", "Tesla"])
        year = st.slider("Year of Manufacture", 2000, 2026, 2020)
        engine_size = st.number_input("Engine Size (L)", 0.5, 8.0, 2.0)

    with col2:
        mileage = st.number_input("Mileage (km)", 0, 500000, 50000)
        fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "Electric", "Hybrid"])
        transmission = st.radio("Transmission", ["Manual", "Automatic"])

# --- PREDICTION LOGIC ---
if st.button("Calculate Estimated Price"):
    with st.spinner('Analyzing market trends...'):
        time.sleep(1.5)  # Simulate a smooth transition/loading
        
        # Mapping inputs for the model (Example logic)
        # input_data = np.array([[year, mileage, engine_size, ...]])
        # prediction = model.predict(input_data)
        
        # Placeholder calculation
        base_price = 20000
        result = base_price + (year - 2000) * 500 - (mileage * 0.05)
        
        st.balloons()
        
        # --- DISPLAY RESULT ---
        st.markdown(f"""
            <div class="prediction-card">
                <h3 style='color: #31333F;'>Estimated Valuation</h3>
                <h1 style='color: #FF4B4B;'>${max(0, int(result)):,}</h1>
                <p style='color: #777;'>Based on current dataset specifications</p>
            </div>
            """, unsafe_allow_stdio=True)

# --- FOOTER ---
st.markdown("---")
st.caption("Data source: ihasan88/car-price-prediction (Kaggle)")
