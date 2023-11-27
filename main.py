# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Given data
labels = ['T', 'T', 'F', 'T', 'F', 'T', 'T', 'F', 'F', 'F', 'F', 'F', 'T', 'F', 'T', 'F', 'F', 'F', 'T', 'F']
scores = [0.95, 0.92, 0.85, 0.84, 0.81, 0.75, 0.71, 0.69, 0.62, 0.56, 0.51, 0.48, 0.43, 0.42, 0.32, 0.25, 0.21, 0.15, 0.08, 0.01]
thresholds = [0.90, 0.74, 0.70, 0.44, 0.22]

# Function to calculate TP, FP, and FN
def calculate_metrics(labels, scores, threshold):
    TP = FP = FN = 0
    for label, score in zip(labels, scores):
        if score >= threshold:
            if label == 'T':
                TP += 1
            else:
                FP += 1
        elif label == 'T':
            FN += 1
    return TP, FP, FN

# Calculating metrics for each threshold
results = {}
for threshold in thresholds:
    TP, FP, FN = calculate_metrics(labels, scores, threshold)
    precision = TP / (TP + FP) if (TP + FP) != 0 else 0
    recall = TP / (TP + FN) if (TP + FN) != 0 else 0
    f_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) != 0 else 0
    results[threshold] = {
        "Precision": precision,
        "Recall": recall,
        "F-score": f_score
    }
    # 遍历每个阈值和对应的结果
# 遍历每个阈值和对应的结果
for threshold, metrics in results.items():
    print(f"Threshold: {threshold}")
    print(f"  Precision: {metrics['Precision']:.2f}")
    print(f"  Recall: {metrics['Recall']:.2f}")
    print(f"  F-score: {metrics['F-score']:.2f}")
    print()

results


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
