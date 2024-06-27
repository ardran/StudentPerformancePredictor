# StudentPerformancePredictor

This project predicts student performance based on various factors using a linear regression model. The prediction includes scores in Math, Reading, and Writing.

## Project Structure

- `train_model.py`: Script to train and save the machine learning model.
- `app.py`: Flask application to serve the model and provide predictions.
- `templates/index.html`: HTML template for the web interface.
- `StudentsPerformance.csv`: Dataset used for training the model.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- Flask
- scikit-learn
- pandas
- joblib

### Installing

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/StudentPerformancePredictor.git
   cd StudentPerformancePredictor
   ```

2. **Install Required Packages:**
   ```bash
   pip install Flask joblib pandas scikit-learn
   ```

### Training the Model

1. **Place the Dataset:**
   Ensure the `StudentsPerformance.csv` file is in the project directory.

2. **Run the Training Script:**
   ```bash
   python train_model.py
   ```
   This will train the model and save the trained model and transformer as `student_performance_model.pkl` and `transformer.pkl` respectively.

### Running the Flask Application

1. **Run the Flask App:**
   ```bash
   python app.py
   ```

2. **Access the Web Interface:**
   Open your web browser and go to `http://127.0.0.1:5000/`.

## Using the Web Interface

1. **Fill Out the Form:**
   Provide the following details:
   - Gender
   - Parental Level of Education
   - Test Preparation Course

2. **Get Predictions:**
   Click the `Predict` button to get the predicted scores for Math, Reading, and Writing.

## Contributing

If you wish to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the authors of the dataset and all the contributors of the libraries used in this project.
-The dataset used here has been downloaded from Kaggle.
-The project has been developed by me as a part of exploring the various ML algorithms.