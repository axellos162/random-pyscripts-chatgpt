from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Load the breast cancer dataset
@st.cache
def load_data():
    data = load_breast_cancer(as_frame=True)
    return data.data, data.target

X, y = load_data()

# Set up the sidebar
st.sidebar.title("Breast Cancer Classification")
x_axis = st.sidebar.selectbox("X-axis", options=X.columns)
y_axis = st.sidebar.selectbox("Y-axis", options=X.columns)
plot_type = st.sidebar.selectbox("Plot Type", options=['Scatter', 'Box', 'Violin', 'Pairplot'])
classifier = st.sidebar.selectbox("Classifier", options=["Logistic Regression"])

# Set up the main page
st.title("Breast Cancer Classification")
st.header("This app allows you to classify breast tumors as benign or malignant and visualize the data using various plots")

# Display the data table
st.subheader("Data Table")
st.dataframe(X)

# Display the summary statistics
st.subheader("Summary Statistics")
st.write(X.describe())

# Display the correlation matrix
st.subheader("Correlation Matrix")
corr_matrix = X.corr()
fig, ax = plt.subplots(figsize=(7, 7))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the classifier
if classifier == "Logistic Regression":
    clf = LogisticRegression(random_state=42)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    # Display the evaluation metrics
    st.subheader("Classification Report")
    st.write(classification_report(y_test, y_pred))

    st.subheader("Confusion Matrix")
    plot_confusion_matrix(clf, X_test, y_test, cmap=plt.cm.Blues)
    st.pyplot()

    st.subheader("Accuracy Score")
    st.write(accuracy_score(y_test, y_pred))

# Display the plot
st.subheader("Plot")
if plot_type == 'Scatter':
    fig = px.scatter(X, x=x_axis, y=y_axis, color=y)
    st.plotly_chart(fig)
elif plot_type == 'Box':
    fig = px.box(X, x=y, y=x_axis)
    st.plotly_chart(fig)
elif plot_type == 'Violin':
    fig = px.violin(X, x=y, y=x_axis, box=True, points='all')
    st.plotly_chart(fig)
else:
    fig = px.scatter_matrix(X, dimensions=X.columns, color=y)
    st.plotly_chart(fig)
