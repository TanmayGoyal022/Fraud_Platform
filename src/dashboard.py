
import streamlit as st
import requests

st.title("Fraud Detection Admin")
st.sidebar.header("Settings")
threshold = st.sidebar.slider("Block threshold", 0.0, 1.0, 0.9)

st.header("Single transaction test")
user_id = st.text_input("user_id","u123")
amount = st.number_input("amount", value=100.0)
lat = st.number_input("lat", value=28.7)
lon = st.number_input("lon", value=77.1)
if st.button("Score"):
    tx = {"user_id": user_id, "amount": amount, "timestamp": "2025-01-01T00:00:00", "merchant_id":"m1", "lat":lat, "lon":lon, "device_id":"d1"}
    r = requests.post("http://localhost:8000/score", json=tx).json()
    st.write(r)
    if r['score'] >= threshold:
        st.error("Block")
    elif r['score'] >= 0.7:
        st.warning("Review")
    else:
        st.success("Allow")
