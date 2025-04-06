import numpy as np
import pandas as pd
import streamlit as st
from ydata_profiling import ProfileReport
from streamlit.components.v1 import html

# Page configuration
st.set_page_config(page_title="Auto EDA")

# Title and Description
st.markdown('''
# 🚀 Automated EDA with YData SDK
Quickly explore and profile your CSV dataset using **YData's profiling** engine.
''')

# Sidebar for file upload
with st.sidebar:
    st.header("📁 Upload your CSV")
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

# Function to load CSV
@st.cache_data
def load_csv(file):
    return pd.read_csv(file)

# Function to create profiling report
@st.cache_resource
def generate_profile(df):
    return ProfileReport(df, title="📊 Data Profile Report", explorative=True)

# Main logic
if uploaded_file is not None:
    df = load_csv(uploaded_file)
    profile = generate_profile(df)

    st.subheader("📄 Input DataFrame")
    st.dataframe(df)
    st.markdown("---")

    st.subheader("📈 YData Profile Report")
    st.components.v1.html(profile.to_html(), height=1000, scrolling=True)

else:
    st.info("Upload a CSV file from the sidebar to begin.")
    if st.button("Use Sample Data Instead"):
        @st.cache_data
        def generate_sample():
            return pd.DataFrame(np.random.rand(100, 5), columns=['A', 'B', 'C', 'D', 'E'])

        df = generate_sample()
        profile = generate_profile(df)

        st.subheader("📄 Sample Input DataFrame")
        st.dataframe(df)
        st.markdown("---")

        st.subheader("📈 Sample YData Profile Report")
        st.components.v1.html(profile.to_html(), height=1000, scrolling=True)