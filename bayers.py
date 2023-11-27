# Revised version of the calculation to include print statements at each step
# Data extracted from the image based on the visual inspection
# Each entry is a tuple (X, Y, Z, C, count)
data = [
    (1, 1, 1, 1, 10),
    (1, 1, 1, 2, 8),
    (1, 1, None, 3, 6),
    (1, 1, 2, 1, 5),
    (1, 1, 2, 3, 15),
    (2, 1, 2, 2, 12),
    (2, 1, 2, 3, 5),
    (2, 2, 1, 2, 8),
    (2, 2, 1, 3, 10),
    (2, 2, 2, 1, 6),
    (None, 2, 2, 3, 10)
]

# Instance to classify
instance = (1, 2, 1)

# Laplace smoothing factor
delta = 1
# Refactored code to print each step for Naive Bayes classification with Laplacian correction

# Calculate total occurrences for each class C
total_counts = sum(row[4] for row in data)
print(f"Total count of instances: {total_counts}")

class_counts = {1: 0, 2: 0, 3: 0}
for row in data:
    if row[3] is not None:
        class_counts[row[3]] += row[4]
print(f"Counts for each class: {class_counts}")

# Calculate priors P(C)
priors = {c: (class_counts[c] + delta) / (total_counts + len(class_counts) * delta) for c in class_counts}
print(f"Prior probabilities: {priors}")

# Calculate likelihoods P(X|C), P(Y|C), P(Z|C) with Laplace smoothing
likelihoods = {c: 1 for c in class_counts}
for feature_index in range(3):
    feature_value = instance[feature_index]
    for c in class_counts:
        # Count occurrences where the feature and class match the instance
        feature_count = sum(row[4] for row in data if row[feature_index] == feature_value and row[3] == c)
        # Apply Laplace smoothing
        likelihood = (feature_count + delta) / (class_counts[c] + 2 * delta)
        likelihoods[c] *= likelihood
        print(f"P({['X','Y','Z'][feature_index]}={feature_value}|C={c}) = {likelihood}")

# Calculate unnormalized posteriors P(C|X,Y,Z) = P(X|C) * P(Y|C) * P(Z|C) * P(C)
posteriors = {c: likelihoods[c] * priors[c] for c in class_counts}
print(f"Calculate Unnormalized posterior probabilities P(C|X,Y,Z) = P(X|C) * P(Y|C) * P(Z|C) * P(C) : {posteriors}")

# Normalize the posterior probabilities and pick the class with the highest probability
normalized_posteriors = {c: p / sum(posteriors.values()) for c, p in posteriors.items()}
print(f"Calculate Normalized posterior probabilities  : {normalized_posteriors}")

predicted_class = max(normalized_posteriors, key=normalized_posteriors.get)
print(f"Predicted class: {predicted_class}")
