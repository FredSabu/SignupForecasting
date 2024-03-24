from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.linear_model import Ridge
import joblib

app = Flask(__name__)

# Weights for different target audiences
weights = {
    'IT Managers': 1.875,
    'Property Managers': 1,
    'Education Property Managers': 3,
    'Education Managers': 1.25,
    'Generic': 1  
}

# Loading the trained model
ridge_reg = joblib.load('ridge_regression.joblib')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Extract JSON data from the request
        data = request.get_json(force=True)

        # Extract input features from the data
        current_five_week_signups = int(data['fiveWeekSignups'])
        current_advertisements = int(data['advertisements'])
        target_audience = data.get('targetAudience', 'Generic')  # Default to 'Generic' if not provided

        # Look up the audience weight, defaulting to 1.0 if not found
        audience_weight = weights.get(target_audience, 1.0)

        # Prepare the input features including the audience weight
        input_features = pd.DataFrame([[current_five_week_signups, current_advertisements, audience_weight]],
                                      columns=['Five_Week_Signups', 'Advertisements', 'Audience_Weight'])

        # Making the prediction
        predicted_final_signups = ridge_reg.predict(input_features)
        prediction = round(predicted_final_signups[0])

        # Return a JSON response containing the prediction
        return jsonify(prediction=str(prediction))

    # For GET requests, render the template as before
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False, use_reloader=False)
