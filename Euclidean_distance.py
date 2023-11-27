import numpy as np
from collections import Counter

# Correcting the data types issue

# Separate features and labels in the training data
training_features = np.array([[3, 3], [4, 5], [2, 2], [10, 9], [14, 12], [17, 19], [8, 13]])
training_labels = np.array(['A', 'B', 'A', 'A', 'B', 'B', 'B'])
test_data = np.array([
    [3, 6],
    [20, 5],
    [6, 6],
    [19, 9],
    [17, 19]
])


# Function to perform KNN prediction
def knn_predict(test, features, labels, k=3):
    predictions = []
    for test_point in test:
        # Calculate distances between test point and all training points
        distances = np.sqrt(np.sum((features - test_point) ** 2, axis=1))

        # Find the k nearest neighbors
        nearest_neighbor_indices = np.argsort(distances)[:k]
        nearest_neighbor_labels = labels[nearest_neighbor_indices]

        # Majority vote for the label
        vote = Counter(nearest_neighbor_labels)
        predicted_label = vote.most_common(1)[0][0]
        predictions.append(predicted_label)

    return predictions


# Predict labels for the test set
predicted_labels = knn_predict(test_data, training_features, training_labels, k=3)


test_points = [(3, 6), (20, 5), (6, 6), (19, 9), (17, 19)]

# 输出每个测试点及其预测的标签
for test_point, label in zip(test_points, predicted_labels):
    print(f"Test Point: {test_point} -> Predicted Label: {label}")



