import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
import joblib

# Load the dataset
df = pd.read_csv('StudentsPerformance.csv')

# Split the data into features and target
X = df[['gender', 'parental level of education', 'test preparation course']]
y = df[['math score', 'reading score', 'writing score']]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a ColumnTransformer to handle categorical features
transformer = ColumnTransformer(
    transformers=[
        ("onehot", OneHotEncoder(), ["gender", "parental level of education", "test preparation course"])
    ],
    remainder="passthrough"  # Pass through any remaining numerical columns
)

# Transform the features
X_train_transformed = transformer.fit_transform(X_train)
X_test_transformed = transformer.transform(X_test)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train_transformed, y_train)

# Save the model and transformer
joblib.dump(model, 'student_performance_model.pkl')
joblib.dump(transformer, 'transformer.pkl')

print("Model and transformer saved successfully!")
