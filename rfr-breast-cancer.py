'''This script first loads the breast cancer dataset from scikit-learn and splits it into training and test sets. 
It then defines a pipeline that standardizes the data and trains a random forest regressor. 
It also defines a hyperparameter grid to search over during grid search. 
The script then performs grid search using cross-validation and prints the best hyperparameters found. 
Finally, it evaluates the best model's performance on the test set by computing mean squared error and the 
coefficient of determination (R^2).'''

import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

# Load the breast cancer dataset
data = load_breast_cancer()
X = pd.DataFrame(data['data'], columns=data['feature_names'])
y = pd.Series(data['target'])

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Define the pipeline
pipeline = make_pipeline(
    StandardScaler(),
    RandomForestRegressor(random_state=42)
)

# Define the hyperparameter grid to search over
param_grid = {
    "randomforestregressor__n_estimators": [50, 100, 200],
    "randomforestregressor__max_depth": [None, 5, 10],
    "randomforestregressor__min_samples_split": [2, 5, 10],
    "randomforestregressor__min_samples_leaf": [1, 2, 4]
}

# Perform the grid search
grid_search = GridSearchCV(pipeline, param_grid=param_grid, cv=5, n_jobs=-1)
grid_search.fit(X_train, y_train)

# Print the best hyperparameters
print("Best hyperparameters: ", grid_search.best_params_)

# Make predictions on the test set using the best model
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)

# Evaluate the model's performance
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:{:.2f}".format(mse))
print("Coefficient of determination (R^2):{:.2f}".format(r2))
