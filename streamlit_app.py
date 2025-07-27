import streamlit as st
import pandas as pd

st.title("🚀 My First Streamlit App")
st.write("LETSSS GOOO...")

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
df