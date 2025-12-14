# Simple Linear Regression using scikit-learn

from sklearn.linear_model import LinearRegression
import numpy as np

# Example data: hours studied vs scores
X = np.array([[1], [2], [3], [4], [5]])  # hours studied
y = np.array([2, 4, 6, 8, 10])          # scores

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Predict score for 6 hours of study
predicted_score = model.predict([[6]])
print("Predicted score for 6 hours of study:", predicted_score[0])
