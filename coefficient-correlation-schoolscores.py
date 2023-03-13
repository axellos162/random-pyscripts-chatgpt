import math

# Define the given data
physics_scores = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
history_scores = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

# Compute the mean of the physics scores
physics_mean = sum(physics_scores) / len(physics_scores)

# Compute the mean of the history scores
history_mean = sum(history_scores) / len(history_scores)

# Compute the numerator of the correlation coefficient
numerator = sum((physics_scores[i] - physics_mean) * (history_scores[i] - history_mean) for i in range(len(physics_scores)))

# Compute the denominator of the correlation coefficient
denominator = math.sqrt(sum((physics_scores[i] - physics_mean) ** 2 for i in range(len(physics_scores)))) * math.sqrt(sum((history_scores[i] - history_mean) ** 2 for i in range(len(history_scores))))

# Compute the correlation coefficient
correlation_coefficient = numerator / denominator

# Print the result with 3 decimal places
print("{:.3f}".format(correlation_coefficient))
