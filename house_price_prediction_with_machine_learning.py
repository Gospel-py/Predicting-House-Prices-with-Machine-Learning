# -*- coding: utf-8 -*-
"""House Price Prediction with Machine Learning

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FC27kAr9PnNgBwkypdU2B6EnaWq24j1H

# **Exploratory Data Analysis**
"""

# Importing the necessary libraries for data analysis and visualization.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/ParisHousing.csv")
df.head()

df.shape

df.info()

df.describe().T

df.isna().sum()

df.columns

# Obtain the unique values in each categorical features in the dataset
obj = [col for col in df.columns if df[col].nunique() <= 15 and df[col].dtype in ['int64']]
for col in obj:
  print(f"====={col}=====")
  unique_values = df[col].unique()
  n_unique_values = df[col].nunique()

  print(f"Unique values in {col}: {unique_values}")
  print(f"Number of unique values in {col}: {n_unique_values}\n")

"""## Data Visualization"""

# Histogram for each feature
df.hist(bins=30, figsize=(15, 10))
plt.tight_layout()
plt.show()

# Identify continuous variables with 15 or more unique values
continuous_vars = [col for col in df.columns if df[col].nunique() >= 15]

# Create histograms with KDE for each continuous variable
plt.figure(figsize=(20, 15))

for i, var in enumerate(continuous_vars, 1):
    plt.subplot(3, 3, i)
    sns.histplot(df[var], kde=True)
    plt.title(f'Distribution of {var}')
    plt.xlabel(var)
    plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

# Countplot for the categorical features with two unique values (0 and 1)

# Creating countplot for the categorical features with two unique values (0 and 1)
count_var = ['hasYard', 'hasPool', 'hasStormProtector', 'hasStorageRoom']

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 6))
axes = axes.flatten()

for i, col in enumerate(count_var):
    ax = sns.countplot(x=df[col], ax=axes[i])
    for j in ax.patches:
        ax.text(j.get_x() + j.get_width() / 2., j.get_height(),
                f'{int(j.get_height())}',
                ha="center", va="bottom")

plt.tight_layout()
plt.show()

# Binning the price feature
plt.figure(figsize=(8,6))
df_c = df.copy()
bins = [0, 100000, 500000, 1000000, df_c['price'].max()]
labels = ['0-100k', '100k-500k', '500k-1M', '1M+']
df_c['price_range'] = pd.cut(df_c['price'], bins=bins, labels=labels, right=False)
sns.countplot(x='price_range', data=df_c)

# Create the countplot
ax = sns.countplot(x='price_range', data=df_c)
plt.figure(figsize=(8,6))
df_c = df.copy()
bins = [0, 100000, 500000, 1000000, df_c['price'].max()]
labels = ['0-100k', '100k-500k', '500k-1M', '1M+']
df_c['price_range'] = pd.cut(df_c['price'], bins=bins, labels=labels, right=False)
sns.countplot(x='price_range', data=df_c)

# Create the countplot
ax = sns.countplot(x='price_range', data=df_c)

# Calculate the percentage and annotate
total = len(df_c)
for p in ax.patches:
    height = p.get_height()
    percentage = f'{100 * height / total:.1f}%'
    ax.annotate(percentage, (p.get_x() + p.get_width() / 2., height),
                ha='center', va='center', fontsize=12, color='black', xytext=(0, 5),
                textcoords='offset points')


plt.show()

from scipy import stats
# Apply Box-Cox transformation to the price column
df_c['boxcox_price'], fitted_lambda = stats.boxcox(df_c['price'])

# Plot the Box-Cox transformed price
plt.figure(figsize=(10, 6))
sns.histplot(df_c['boxcox_price'], kde=True)
plt.title('Distribution of Box-Cox Transformed House Prices')
plt.xlabel('Box-Cox Price')
plt.ylabel('Frequency')
plt.show()

df_c.drop(columns=['price_range', 'price'], inplace=True)
df.head()

# Identify continuous variables with 15 or more unique values
continuous_vars = [col for col in df_c.columns if df_c[col].nunique() >= 15]

# Create histograms with KDE for each continuous variable
plt.figure(figsize=(20, 15))

for i, var in enumerate(continuous_vars, 1):
    plt.subplot(3, 3, i)
    sns.scatterplot(x=df_c[var], y=df_c['boxcox_price'])
    plt.title(f'boxcox_price vs {var}')
    plt.xlabel(var)
    plt.ylabel('Price')

plt.tight_layout()
plt.show()

# List of categorical variables
categorical_vars = ['hasYard', 'hasPool', 'isNewBuilt', 'hasStormProtector', 'hasStorageRoom', 'hasGuestRoom']

# Create boxplots for each categorical variable
plt.figure(figsize=(20, 12))

for i, var in enumerate(categorical_vars, 1):
    plt.subplot(2, 3, i)
    sns.boxplot(x=var, y='boxcox_price', data=df_c)
    plt.title(f'Price Distribution by {var}')
    plt.xlabel(var)
    plt.ylabel('Price')

plt.tight_layout()
plt.show()

# Creating heatmap for the dataset
plt.figure(figsize=(15, 15))
sns.heatmap(df_c.corr(), annot=True, cmap='coolwarm')
plt.title('Dataset Correlation Matrix')
plt.tight_layout()
plt.show()

"""#MACHINE LEARNING"""

# Importing the necessary libraries needed for machine learing
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from xgboost import XGBRegressor

"""## Feature Engineering"""

import datetime
#Feature Engineering
current_year = datetime.datetime.now().year
df_c['property_age'] = current_year - df_c['made']
df_c['house_to_room_ratio'] = df_c['squareMeters'] / df_c['numberOfRooms']
df_c['area_rooms_interaction'] = df_c['squareMeters'] * df_c['numberOfRooms']
df_c['basement_attic_interaction'] = df_c['basement'] * df_c['attic']
df_c['garage_floors_interaction'] = df_c['garage'] * df_c['floors']

df_c.head()

"""## Train-test Split"""



#Create features and targets
target = df_c['boxcox_price']
features = df_c.drop(columns=['boxcox_price'], axis=1)

#Split data
train_features, test_features, train_target, test_target = train_test_split(features, target, test_size=0.2, random_state=26)

"""## Feature Scaling"""

#Feature Scaling
scaler = StandardScaler()

train_features_scaled = scaler.fit_transform(train_features)
test_features_scaled = scaler.transform(test_features)

# Visualize the scaled dataframe
train_features_scaled_df = pd.DataFrame(train_features_scaled, columns=features.columns)
train_features_scaled_df.head()

train_features_scaled_df.columns

"""## Model Training"""

# Linear Regression Algorithm
lin_reg = LinearRegression()
lin_reg.fit(train_features_scaled, train_target)
pred_target = lin_reg.predict(test_features_scaled)
lin_reg_RMSE = np.sqrt(mean_squared_error(test_target, pred_target))
lin_reg_MAE = mean_absolute_error(test_target, pred_target)
print("Linear Regression RMSE:", lin_reg_RMSE)
print("Linear Regression MAE:", lin_reg_MAE)
print("Linear Regression R^2:", r2_score(test_target, pred_target))

# Evaluating the Linear Regression alorithm
scores = cross_val_score(lin_reg, features, target, scoring='neg_mean_squared_error', cv=10)
rmse_scores = np.sqrt(-scores)
print("Cross-validated RMSE scores:", rmse_scores)
print("Mean RMSE:", rmse_scores.mean())
print("Standard Deviation of RMSE:", rmse_scores.std())

lin_reg.intercept_

#Converting the coefficient values to a dataframe
coeffcients = pd.DataFrame([train_features.columns, lin_reg.coef_]).T
coeffcients = coeffcients.rename(columns={0: 'Attribute', 1: 'Coefficients'})
coeffcients

# Plot feature importances (coefficients)
def plot_linear_feature_importances(model, feature_names):
    coefficients = model.coef_
    importance = np.abs(coefficients)
    indices = np.argsort(importance)

    plt.figure(figsize=(10, 6))
    plt.title("Feature Importances for Linear Regression")
    plt.barh(range(len(indices)), importance[indices], align='center')
    plt.yticks(range(len(indices)), [feature_names[i] for i in indices])
    plt.xlabel('Absolute Coefficient Value')
    plt.show()

# Assuming X_train is a DataFrame with named columns
feature_names = train_features.columns if isinstance(train_features, pd.DataFrame) else [f'Feature {i}' for i in range(X_train.shape[1])]
plot_linear_feature_importances(lin_reg, feature_names)

# Gradient Boosting Regressor
gbr_reg = GradientBoostingRegressor(n_estimators=100, random_state=26)
gbr_reg.fit(train_features_scaled, train_target)
pred_target = gbr_reg.predict(test_features_scaled)
gbr_reg_RMSE = np.sqrt(mean_squared_error(test_target, pred_target))
gbr_reg_MAE = mean_absolute_error(test_target, pred_target)
print("Gradient Boosting RMSE:", gbr_reg_RMSE)
print("Gradient Boosting MAE:", gbr_reg_MAE)
print("Gradient Boosting R^2:", r2_score(test_target, pred_target))

# XGB Regressor
xgb_reg = XGBRegressor(n_estimators=100, random_state=26)
xgb_reg.fit(train_features_scaled, train_target)
pred_target = xgb_reg.predict(test_features_scaled)
xgb_reg_RMSE = np.sqrt(mean_squared_error(test_target, pred_target))
xgb_reg_MAE = mean_absolute_error(test_target, pred_target)
print("XGBoost RMSE:", xgb_reg_RMSE)
print("XGBoost MAE:", xgb_reg_MAE)
print("XGBoost R^2:", r2_score(test_target, pred_target))

#RandomForest Regressor
forest_reg = RandomForestRegressor(n_estimators=100, random_state=26)
forest_reg.fit(train_features_scaled, train_target)
pred_target = forest_reg.predict(test_features_scaled)
rforest_RMSE = np.sqrt(mean_squared_error(test_target, pred_target))
rforest_MAE = mean_absolute_error(test_target, pred_target)
print("Random Forest RMSE:", rforest_RMSE)
print("Random Forest MAE:", rforest_MAE)
print("Random Forest R^2:", r2_score(test_target, pred_target))

"""## Model Evaluation"""

# Plotting the RMSE of the various models
models_rmse = [lin_reg_RMSE, gbr_reg_RMSE, xgb_reg_RMSE, rforest_RMSE]
models_name = ['Linear Regression', 'Gradient Boosting', 'XGBoost', 'Random Forest']
plt.figure(figsize=(10, 6))
plt.plot(models_name, models_rmse, marker='o')
plt.xlabel('Models')
plt.ylabel('RMSE')
plt.title('RMSE for the Different Models')
plt.grid(True)
plt.show()

# Plotting the MAE of the various models
models_mae = [lin_reg_MAE, gbr_reg_MAE, xgb_reg_MAE, rforest_MAE]
models_name = ['Linear Regression', 'Gradient Boosting', 'XGBoost', 'Random Forest']
plt.figure(figsize=(10, 6))
plt.plot(models_name, models_mae, marker='o')
plt.xlabel('Models')
plt.ylabel('MAE')
plt.title('MAE for the Different Models')
plt.grid(True)
plt.show()

# Feature Importance
importances = forest_reg.feature_importances_
importances_df = pd.DataFrame({"features": train_features.columns, "importances": importances})
importances_df = importances_df.sort_values(by="importances", ascending=False)
importances_df

#Plot the feature importances
plt.figure(figsize=(10, 6))
plt.barh(importances_df["features"], importances_df["importances"])
plt.xlabel("Features")
plt.ylabel("Importance")
plt.title("Feature Importances for RandomForest Regressor")
plt.xticks(rotation=90)
plt.show()

"""## Hyper Parameter Tuning


"""

# Define the parameter grids for each model
param_grids = {
    'GradientBoostingRegressor': {
        'model': GradientBoostingRegressor(random_state=26),
        'params': {
            'n_estimators': [100, 200, 300],
            'max_depth': [3, 4, 5],
            'learning_rate': [0.01, 0.1, 0.2]
        }
    },
    'RandomForestRegressor': {
        'model': RandomForestRegressor(random_state=26),
        'params': {
            'n_estimators': [100, 200, 300],
            'max_depth': [10, 20, 30]
        }
    },
    'XGBRegressor': {
        'model': XGBRegressor(random_state=26),
        'params': {
            'n_estimators': [100, 200, 300],
            'max_depth': [3, 4, 5],
            'learning_rate': [0.01, 0.1, 0.2]
        }
    }
}

# Iterate over the models and their parameter grids
for model_name, model_info in param_grids.items():
    print(f"Training {model_name}...")

    grid_search = GridSearchCV(
        estimator=model_info['model'],
        param_grid=model_info['params'],
        cv=5,
        scoring='neg_mean_squared_error',
        n_jobs=-1
    )

    grid_search.fit(train_features, train_target)

    best_model = grid_search.best_estimator_
    pred_target = best_model.predict(test_features)

    print(f"Best parameters for {model_name}:", grid_search.best_params_)
    print(f"Tuned {model_name} RMSE:", np.sqrt(mean_squared_error(test_target, pred_target)))
    print(f"Tuned {model_name} MAE:", mean_absolute_error(test_target, pred_target))
    print(f"Tuned {model_name} R^2:", r2_score(test_target, pred_target))
    print("\n")

"""# CONCLUSION

The Random Forest Regressor is the most suitable for predicting house prices in this dataset
"""