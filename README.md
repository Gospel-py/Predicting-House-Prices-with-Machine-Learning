# Predicting-House-Prices-with-Machine-Learning

![House_Pic](https://github.com/user-attachments/assets/f1d45412-0dae-4f6d-bc1e-c92b22380030)

This project aims to predict house prices using various machine learning algorithms. The dataset used includes features such as house size, number of rooms, presence of amenities, and more. The project involves data preprocessing, exploratory data analysis, feature engineering, model training, and evaluation.

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Data Preprocessing](#data-preprocessing)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Feature Engineering](#feature-engineering)
- [Model Selection](#model-selection)
- [Model Performance and Evaluation](#model-performance-and-evaluation)
- [How to Run](#how-to-run)

## Introduction

The goal of this project is to build a predictive model for house prices using machine learning. By analyzing various features of houses, the model can provide price predictions, which can be useful for real estate agents, buyers, and sellers.

## Dataset

The dataset used in this project was gotten from Kaggle. You can download the dataset [here](https://www.kaggle.com/datasets/mssmartypants/paris-housing-price-prediction). It includes the following features:

- `squareMeters`
- `numberOfRooms`
- `hasYard`
- `hasPool`
- `floors`
- `cityCode`
- `cityPartRange`
- `numPrevOwners`
- `made`
- `isNewBuilt`
- `hasStormProtector`
- `basement`
- `attic`
- `garage`
- `hasStorageRoom`
- `hasGuestRoom`
- `price`

## Data Preprocessing

The data downloaded from Kaggle was already in a clean state. There were no outliers, missing values, structural errors, or irrelevant data.

## Exploratory Data Analysis

Exploratory data analysis (EDA) was conducted to understand the relationships between features and the target variable (`price`). Key insights included:

- Correlation analysis
- Distribution plots (boxplots, histograms)
- Scatter plots and heatmaps

## Feature Engineering

Feature engineering steps included:

1. Creating interaction features
2. Scaling numerical features
3. Applying box-cox transformation to skewed features

## Model Selection

Several machine learning models were evaluated:

1. Linear Regression
2. Random Forest Regressor
3. Gradient Boosting Regressor
4. XGBoost Regressor

## Model Performance and Evaluation

The models were evaluated using the following metrics:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R-squared (R²)

The Random Forest Regressor achieved the best performance with an RMSE of 57 and an R² score of 0.999997. It was  therefore identified as the best model for predicting house prices in this dataset. It effectively captured the complex relationships in the data, providing highly accurate predictions.

![House_MAEpointplot](https://github.com/user-attachments/assets/0150312b-5f20-48ec-b835-c356a18cc8fc)

![House_MSEpointplot](https://github.com/user-attachments/assets/2b6ef180-7a94-443f-bd24-e0424d0bec09)

## Feature Importance
The results of the feature importance analysis indicated that the `squareMeters` feature was the most important predictor of house prices for this dataset. The horizontal bar plot of feature importance showed that the `squareMeters` feature had a significantly longer bar compared to other features, which had little contributions.

![House_rforestReg_feature_Importances](https://github.com/user-attachments/assets/3cc009a1-fb3b-4f8b-a95a-5235573b4261)

![House_LinReg_FeatureImportances](https://github.com/user-attachments/assets/20e13bb3-bb74-46e2-8291-e8a5a435b768)

## Data Distribution and Correlations
The various visualizations, including bar plots, count plots, histograms, and Kernel Density Estimate (KDE) plots, demonstrated that the data was evenly distributed across the different features. Notably, the heatmap and scatter plot revealed a near-perfect correlation (0.999) between the `squaremeters` feature and the target variable 'price' indicating that `squaremeters` is the main factor for determining house price for this dataset.

## Key Insights 
- The `squareMeters`  feature is the most critical factor in predicting house prices.
- Visualizations indicated that the dataset was well-balanced and uniformly distributed.
- The nearly perfect correlation between `squareMeters` and prices suggests that the size of the house is the primary driver of its price.
- The Box-Cox transformation effectively handled the skewness in the price feature, making the data more suitable for modeling



## How to Run

1. **Accessing the Notebook**:
   - Click [here](https://colab.research.google.com/drive/1FC27kAr9PnNgBwkypdU2B6EnaWq24j1H?usp=sharing) to open the project notebook in Google Colab.
   - Upload the `ParisHousing` dataset

2. **Running the Notebook**:
   - Once the notebook is open, you can run each cell sequentially by pressing `Shift + Enter`.

3. **Interacting with the Code**:
   - Feel free to modify the code and experiment with different parameters, algorithms, or preprocessing techniques.

4. **Saving Results**:
   - Any outputs, including plots, tables, or trained models, will be saved automatically within the notebook. Ensure you're signed in to your Google account though.
   - You can also download the notebook for future reference or sharing purposes.


Feel free to explore the code and provide feedback. Contributions are welcome!
