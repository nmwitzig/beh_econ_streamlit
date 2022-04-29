import constants
from utils.html_factory import CSSStyle, make_div, make_img, st_write_bs4
import streamlit as st
import pandas as pd

@st.cache(allow_output_mutation=True)
def get_data():
    return []

def convert_df(df):
   return df.to_csv().encode('utf-8')

# main
def st_write_feedback():
    st.markdown("""
    # Feedback


    Let me know if you have any questions or suggestions. *These will be fully anonymous*!
    """, unsafe_allow_html=True)
    user_input = st.text_input("Use this textbox",)
    # save user_input to a file on google drive
    get_data().append({"Comment": user_input})
    
    df = pd.DataFrame(get_data())

    df = convert_df(df)
    # convert dataframe to binary

    
    st.download_button("Download Feedback",df,"file.csv","text/csv",key='download-csv')


