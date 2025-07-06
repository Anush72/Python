from flask import Flask,render_template,request,jsonify
import pickle
import numpy as np
app = Flask(__name__)

# Loading the model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Encoding the smoking history
def encode_smoking_history(smoking_history):
    mapping = {
        'never': 0,
        'No Info': 1,
        'current': 2,
        'former': 3,
        'ever': 4,
        'not current': 5
    }
    return mapping.get(smoking_history, 0)


#Rendering the template
@app.route('/')
def index():
    return render_template('index.html')
# Making the prediction
@app.route('/predict',methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = [1 if data['gender']=='Male' else 0,
        int(data['age']),
        int(data['hypertension']),
        int(data['heart_disease']),
        encode_smoking_history(data['smoking_history']),
        float(data['bmi']),
        float(data['hba1c']),
        float(data['blood_glucose'])
        ]
        # Convert to numpy array
        features_array = np.array(features).reshape(1,-1)
        prediction = int(model.predict(features_array)[0])
        proba = model.predict_proba(features_array)[0]
        probability = float(proba[1])
        return jsonify(
            {
                'prediction': prediction,
                'probability': probability
            }
        )
    except Exception as e:
        print(f'Error: {e}')
        return jsonify({'error': str(e)}),500

if __name__ == '__main__':
    app.run()
