import numpy as np
import pandas as pd
import streamlit as st
from ydata_profiling import ProfileReport
from streamlit.components.v1 import html

st.set_page_config(  
    page_title="Auto EDA" 
)  
st.markdown('''
# **Exploratory Data Analysis Automation**
**Explore your CSV data quality and get quick insights!!!**
''')

#Upload CSV data feature
with st.sidebar.header('Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("**Upload your CSV file here**", type=["csv"])

if uploaded_file is not None:
    @st.cache_data
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    html_report = pr.to_html()
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Report of Your CSV File using Pandas Profiling**')
    st.components.v1.html(html_report, height=1000, scrolling=True)
else:
    st.info("Click on **>** top left corner to upload your csv file")
    if st.button('Press to use Example Dataset'):
        @st.cache_data
        def load_data():
            a = pd.DataFrame(np.random.rand(100, 5),columns=['A', 'B', 'C', 'D', 'E'])
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        html_report = pr.to_html()
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Report of the CSV data using Pandas Profiling')
        st.components.v1.html(html_report, height=1000, scrolling=True)