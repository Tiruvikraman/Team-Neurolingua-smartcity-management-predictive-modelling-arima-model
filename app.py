from flask import Flask, render_template, jsonify
import datetime
import numpy as np
import joblib  # Assuming you're using joblib to save/load models
from data_source import resource
app = Flask(__name__)

# Example model loading functions (replace with your actual model loading code)
def load_consumption_model():
    try:
        # Load your trained consumption model from a file
        model = joblib.load('consumption_model.pkl')
        return model
    except FileNotFoundError:
        print("Consumption model file not found.")
        return None
    except Exception as e:
        print(f"Error loading consumption model: {str(e)}")
        return None

def load_crime_model():
    try:
        # Load your trained crime model from a file
        model = joblib.load('crime_model.pkl')
        return model
    except FileNotFoundError:
        print("Crime model file not found.")
        return None
    except Exception as e:
        print(f"Error loading crime model: {str(e)}")
        return None

# Generate sample data for the resources
def generate_sample_data():
    
    return resources

# Example route to load consumption data
@app.route('/consumption')
def consumption():
    model = load_consumption_model()
    if model:
        # Example: Use model to predict consumption
        predictions = generate_sample_data()  # Replace with actual prediction logic
        return render_template('consumption.html', predictions=predictions)
    else:
        return "Error loading consumption model"

# Example route to load crime data
@app.route('/crime')
def crime():
    model = load_crime_model()
    if model:
        # Example: Use model to predict crime rates or analyze data
        predictions = generate_sample_data()  # Replace with actual prediction or analysis logic
        return render_template('crime.html', predictions=predictions)
    else:
        return "Error loading crime model"

# Example route for the main dashboard
@app.route('/')
def index():
    return render_template('dashboard.html')

# Route to serve static images (replace with your actual image paths)
@app.route('/static/images/<path:path>')
def serve_static_images(path):
    return app.send_static_file(f'images/{path}')

# Example route to get predictions (sample data)
@app.route('/predictions', methods=['GET'])
def get_predictions():
    data = generate_sample_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
