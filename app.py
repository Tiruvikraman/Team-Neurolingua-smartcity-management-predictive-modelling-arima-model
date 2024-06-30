from flask import Flask, render_template, jsonify
import datetime
import numpy as np

app = Flask(__name__)

# Generate sample data for the resources
def generate_sample_data():
    resources = {
        "Electricity": [(str(datetime.date.today() - datetime.timedelta(days=i)), np.random.uniform(100, 200)) for i in range(30)],
        "Water": [(str(datetime.date.today() - datetime.timedelta(days=i)), np.random.uniform(50, 150)) for i in range(30)],
        "Gas": [(str(datetime.date.today() - datetime.timedelta(days=i)), np.random.uniform(20, 80)) for i in range(30)],
        "Internet": [(str(datetime.date.today() - datetime.timedelta(days=i)), np.random.uniform(10, 30)) for i in range(30)],
        "Waste": [(str(datetime.date.today() - datetime.timedelta(days=i)), np.random.uniform(5, 15)) for i in range(30)]
    }
    return resources

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/consumption')
def consumption():
    return render_template('consumption.html')

@app.route('/crime')
def crime():
    return render_template('crime.html')

@app.route('/predictions', methods=['GET'])
def get_predictions():
    data = generate_sample_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
