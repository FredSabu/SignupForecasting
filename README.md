# Signup Forecasting using Machine Learning


![image](https://github.com/FredSabu/SignupForecasting/assets/130511381/1100cc3d-0364-4da9-85a6-4f3ba6338a6e)

## Overview
This web-based platform uses a ridge regression model to predict the final number of signs-ups for an event, assisting event organisers in making well-informed decisions regarding the necessity of additional marketing to achieve target attendance figures. 
Data set was provided by the virtual conference company Xiatagy, in partnership with Keele University. 


## Features
- **Predictive Analytics:** Users can input current registration numbers, planned advertising campaigns, and select the target audience from a  dropdown to estimate final event signups.
- **5-Week Forecast Window:** Due to limitations in available data for model training, predictions are currently constrained to a 5-week period before the event date.

## Technical Stack
- **Frontend:** HTML, CSS, JavaScript for dynamic and responsive user interfaces.
- **Backend:** Python with Flask for server-side operations and RESTful API management.
- **Machine Learning Model:** Ridge Regression, implemented using the scikit-learn library, for robust and reliable predictive analytics.

## Data Processing
The model is trained on data from seven events with varying campaign lengths and years. This was then standardised to align timelines and aggregate weekly signup figures, creating a consistent dataset for model training and evaluation.

## Model Evaluation
- **R² Scores:** Achieved 0.94 for the training set and 0.90 for the testing set, indicating a high level of variance explanation by the model.
- **Mean Absolute Error (MAE):** Recorded at 77.92 for the training set and 65.36 for the testing set, reflecting the model's accuracy.
- **Mean Squared Error (MSE):** Measured at 9210.44 for the training set and 4353.01 for the testing set, demonstrating the model's predictive performance.

## Model Visualisation
Below is a 3D scatter plot visualisation showing how the model predicts final event sign-ups based on early registration data and advertising efforts (target audience weighting is not included here):

<img width="387" alt="Screenshot 2024-02-28 231558" src="https://github.com/FredSabu/SignupForecasting/assets/130511381/72df2307-6409-4145-b4b8-51bed58e2820">

## Installation
1. **Repository Cloning:** Clone the GitHub repository or download the project ZIP file.
2. **Dependency Installation:** Use pip to install Python 3.6 or later, Flask, and scikit-learn dependencies.
3. **Service Activation:** Run the Flask application to initiate the web service.



