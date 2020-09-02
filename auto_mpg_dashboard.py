import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns

# set the style for seaborn
sns.set_style('darkgrid')

st.title('Dashboard for Autompg dataset.')


def load_data():
    """ Utility function for loading the autompg dataset as a dataframe."""
    df = pd.read_csv("data/clean_auto_mpg.csv")

    return df


# load dataset
data = load_data()
numeric_columns = data.select_dtypes(['float64', 'float32', 'int32', 'int64']).columns
print(numeric_columns)

# checkbox widget
checkbox = st.sidebar.checkbox("Reveal data.")
print(checkbox)

if checkbox:
    # st.write(data)
    st.dataframe(data=data)

# create scatterplots
st.sidebar.subheader("Scatter plot setup")
# add select widget
select_box1 = st.sidebar.selectbox(label='X axis', options=numeric_columns)
print(select_box1)
select_box2 = st.sidebar.selectbox(label="Y axis", options=numeric_columns)

# create scatterplot
sns.relplot(x=select_box1, y=select_box2, data=data)
st.pyplot()


# create histograms
st.sidebar.subheader("Histogram")
select_box3 = st.sidebar.selectbox(label="Feature", options=numeric_columns)
sns.distplot(data[select_box3])
st.pyplot()