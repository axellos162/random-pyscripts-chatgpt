import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Exploratory Data Analysis of the Iris Dataset", page_icon=":bar_chart:", layout="wide")

# Load the iris dataset
@st.cache_data()
def load_data():
    data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
    return data

data = load_data()

# Set up the sidebar
st.sidebar.title("Iris Data Visualization")
x_axis = st.sidebar.selectbox("X-axis", options=data.columns[:-1])
y_axis = st.sidebar.selectbox("Y-axis", options=data.columns[:-1])
plot_type = st.sidebar.selectbox("Plot Type", options=['Scatter', 'Box', 'Violin', 'Pairplot'])
plot_column = st.sidebar.selectbox("Column to visualize", options=data.columns[:-1])
classes_to_visualize = st.sidebar.multiselect("Classes to visualize", options=data['species'].unique(), default=data['species'].unique())

# Set up the main page
st.title("Exploratory Data Analysis of the Iris Dataset")
st.header("This app allows you to explore the Iris dataset and visualize the data using various plots")

# Display the data table
st.subheader("Data Table")
st.dataframe(data)

# Display the summary statistics
st.subheader("Summary Statistics")
st.write(data.describe())

# Compute the correlation matrix
corr_matrix = data.corr(numeric_only=True)

# Display the correlation matrix
st.subheader("Correlation Matrix")
fig, ax = plt.subplots(figsize=(5, 5))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

# Display the plot
st.subheader("Plot")
if plot_type == 'Scatter':
    fig = px.scatter(data[data['species'].isin(classes_to_visualize)], x=x_axis, y=y_axis, color='species')
    st.plotly_chart(fig)
elif plot_type == 'Box':
    fig, ax = plt.subplots(figsize=(5, 5))
    sns.boxplot(x='species', y=plot_column, data=data[data['species'].isin(classes_to_visualize)], ax=ax)
    ax.set_xlabel('Species', fontsize=10)
    ax.set_ylabel(plot_column.capitalize(), fontsize=10)
    st.pyplot(fig)
elif plot_type == 'Violin':
    fig, ax = plt.subplots(figsize=(5, 5))
    sns.violinplot(x='species', y=plot_column, data=data[data['species'].isin(classes_to_visualize)], ax=ax)
    ax.set_xlabel('Species', fontsize=10)
    ax.set_ylabel(plot_column.capitalize(), fontsize=10)
    st.pyplot(fig)
else:
    fig = sns.pairplot(data[data['species'].isin(classes_to_visualize)], hue='species', height=2)
    st.pyplot(fig.fig)

