import streamlit as st
import pandas as pd
import seaborn as sns

# set the style for seaborn
sns.set_style('darkgrid')

# Title of the dashboard
st.title('Dashboard for Autompg dataset.')


@st.cache
def load_data():
    """ Utility function for loading the autompg dataset as a dataframe."""
    df = pd.read_csv("data/clean_auto_mpg.csv")

    return df


# load dataset
data = load_data()
numeric_columns = data.select_dtypes(['float64', 'float32', 'int32', 'int64']).columns

# checkbox widget
checkbox = st.sidebar.checkbox("Reveal data.")

if checkbox:
    # st.write(data)
    st.dataframe(data=data)

# create scatterplots
st.sidebar.subheader("Scatter plot setup")
# add select widget
select_box1 = st.sidebar.selectbox(label='X axis', options=numeric_columns)
select_box2 = st.sidebar.selectbox(label="Y axis", options=numeric_columns)
sns.relplot(x=select_box1, y=select_box2, data=data)
st.pyplot()

# create histograms
st.sidebar.subheader("Histogram")
select_box3 = st.sidebar.selectbox(label="Feature", options=numeric_columns)
histogram_slider = st.sidebar.slider(label="Number of Bins",min_value=5, max_value=100, value=30)
sns.distplot(data[select_box3], bins=histogram_slider)
st.pyplot()

# create jointplot
st.sidebar.subheader("Joint plot")
select_box3 = st.sidebar.selectbox(label='x', options=numeric_columns)
select_box4 = st.sidebar.selectbox(label="y", options=numeric_columns)
sns.jointplot(x=select_box3, y=select_box4, data=data)
st.pyplot()