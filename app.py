from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load the model and transformer
model = joblib.load('student_performance_model.pkl')
transformer = joblib.load('transformer.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    # Extract data
    gender = data['gender']
    parental_education = data['parental level of education']
    test_preparation = data['test preparation course']
    
    # Transform the data
    input_data = pd.DataFrame([[gender, parental_education, test_preparation]], 
                              columns=['gender', 'parental level of education', 'test preparation course'])
    transformed_data = transformer.transform(input_data)
    
    # Make prediction
    prediction = model.predict(transformed_data)
    
    # Return the result
    return jsonify({
        'math_score': prediction[0][0],
        'reading_score': prediction[0][1],
        'writing_score': prediction[0][2]
    })

if __name__ == '__main__':
    app.run(debug=True)
