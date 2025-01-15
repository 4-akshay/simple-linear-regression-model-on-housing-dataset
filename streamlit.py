import pandas as pd
import streamlit as st
import seaborn as sns
housing = pd.read_csv("data.csv")
housing_corr = housing.corr
st.title("Creating a :blue[heatmap]")
st.dataframe(housing)