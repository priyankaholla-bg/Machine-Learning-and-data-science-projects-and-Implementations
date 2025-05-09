import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	means = np.array([sum(list(col))/len(col) for col in zip(*(data))])
	var = np.array([sum((x - mean) ** 2 for x in feature) / (len(feature)) for feature, mean in zip(zip(*data), means)])
    # means = np.mean(data, axis=0)
	# var = np.std(data, axis=0)
	standardized_data = (data-means)/var**0.5

	min_val = np.min(data, axis=0)
	max_val = np.max(data, axis=0)
	normalized_data = (data - min_val) / (max_val - min_val)

	return np.round(standardized_data, 4).tolist(), np.round(normalized_data, 4).tolist()
