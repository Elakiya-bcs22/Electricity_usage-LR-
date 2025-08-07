from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        residents = float(request.form['residents'])
        avg_daily_hours = float(request.form['avg_daily_hours'])
        num_appliances = float(request.form['num_appliances'])
        avg_unit_rate = float(request.form['avg_unit_rate'])

        input_data = np.array([[residents, avg_daily_hours, num_appliances, avg_unit_rate]])
        input_scaled = scaler.transform(input_data)
        prediction = model.predict(input_scaled)[0]

        return render_template('index.html', prediction=f"Predicted Monthly Electricity Cost: ₹{round(prediction, 2)}")
    except Exception as e:
        return render_template('index.html', prediction="Error in prediction: " + str(e))

if __name__ == '__main__':
    app.run(debug=True)
