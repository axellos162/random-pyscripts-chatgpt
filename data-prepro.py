'''This code fits the scaler on the training data, 
applies the scaler to the training and test sets, and prints the mean and standard deviation of the training set. 
It then trains a random forest regressor, makes predictions on the test set, evaluates the model's performance, 
and saves the model to a file.'''

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
import joblib


def load_and_clean_red_wine_data():
    # Load the wine dataset from scikit-learn
    wine_dataset = load_wine()

    # Convert the dataset to a pandas DataFrame
    wine_df = pd.DataFrame(data=np.c_[wine_dataset['data'], wine_dataset['target']],
                           columns=wine_dataset['feature_names'] + ['target'])

    # Separate the dataset into input features and target variable
    X = wine_df.iloc[:, :-1]
    y = wine_df.iloc[:, -1]

    # Print the first five rows of the cleaned up dataset
    print("First 5 rows of input features:\n", X.head())

    # Print a summary of the dataset
    print("Summary statistics of input features:\n", X.describe())

    return X, y


def preprocess_data(X_train, X_test):
    # Initialize a StandardScaler object
    scaler = StandardScaler()

    # Fit the scaler on the training data
    scaler.fit(X_train)

    # Apply the scaler to the training and test sets
    X_train_scaled = scaler.transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Print the mean and standard deviation of the training set
    print("Mean of X_train_scaled:", np.mean(X_train_scaled))
    print("Standard deviation of X_train_scaled:", np.std(X_train_scaled))

    return X_train_scaled, X_test_scaled


# Load and clean the red wine dataset
X, y = load_and_clean_red_wine_data()

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Preprocess the data using Scikit-Learn's transformer API
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Print the mean and standard deviation of the training set
print("Mean of X_train_scaled:", np.mean(X_train_scaled))
print("Standard deviation of X_train_scaled:", np.std(X_train_scaled))

# Train a random forest regressor
rf_regressor = RandomForestRegressor(random_state=42)
rf_regressor.fit(X_train_scaled, y_train)

# Make predictions on the test set
y_pred = rf_regressor.predict(X_test_scaled)

# Evaluate the model's performance
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean squared error: {:.2f}".format(mse))
print("Coefficient of determination (R^2): {:.2f}".format(r2))

# Save the model to a file
joblib.dump(rf_regressor, "rf_regressor.joblib")

