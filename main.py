# IMPORT LIB
import streamlit as st
from config import load_data
from Tabs import home, predict, visualize

Tabs = {
    "Home": home,
    "Prediction": predict,
    "Visualization": visualize
}

# SIDEBAR
st.sidebar.title("Navigation")

# RADIO OPTION
page = st.sidebar.radio("Pages", list(Tabs.keys()))

# LOAD DATAFRAME
df, x, y = load_data()

# CALL PAGES
if page in ["Prediction", "Visualization"]:
    Tabs[page].app(df,x,y)
else:
    Tabs[page].app()