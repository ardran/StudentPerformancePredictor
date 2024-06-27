# Student Performance Predictor

This project predicts student performance based on various factors using a linear regression model. It includes a Flask web application to serve the model and provide predictions via a simple web interface.

## Project Structure

- `train_model.py`: Script to train and save the model.
- `app.py`: Flask application to serve the model and provide predictions.
- `templates/index.html`: HTML template for the web interface.
- `StudentsPerformance.csv`: Dataset used for training the model.

## Dataset

The dataset used for this project is `StudentsPerformance.csv`, which includes the following columns:

- `gender`: Gender of the student (`male` or `female`).
- `parental level of education`: The highest level of education achieved by the student's parents.
- `test preparation course`: Whether the student completed a test preparation course (`none` or `completed`).
- `math score`: The student's score in math.
- `reading score`: The student's score in reading.
- `writing score`: The student's score in writing.

## Requirements

- Python 3.x
- Flask
- Joblib
- Pandas
- Scikit-learn

## How to Run

### Step 1: Install Required Packages

Install the required Python packages using pip:

```bash
pip install Flask joblib pandas scikit-learn

### Step 2: Train the Model
Run the train_model.py script to train the model and save it along with the transformer:

```bash
python train_model.py

### Step 3: Run the Flask App
Run the app.py script to start the Flask application:

```bash
python app.py

### Step 4: Access the Web Application
Open your web browser and navigate to http://127.0.0.1:5000/. You should see the form where you can input the student's information and get the predicted scores.