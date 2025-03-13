def k_means_clustering(points: list[tuple[float, float]], k: int, initial_centroids: list[tuple[float, float]], max_iterations: int) -> list[tuple[float, float]]:
	
	centroids = initial_centroids

	def euclidean_distance(x, centroid):
		dist = 0
		for i in range(len(x)):
			dist += (x[i]-centroid[i])**2
		return dist**0.5

	
	def assign_clusters(points, centroids):
		clusters = []
		for point in points:
			distances = [euclidean_distance(point, centroid) for centroid in centroids]
			cluster_index = distances.index(min(distances))
			clusters.append(cluster_index)
		return clusters
			
	def new_centroid_assign(points, clusters, k):
		new_centroids = []

		for i in range(k):
			cluster_points = [points[j] for j in range(len(points)) if clusters[j]==i]
			new_centroid = ()
			for i in range(len(points[0])):
				new_centroid = new_centroid + ((sum(p[i] for p in cluster_points)/len(cluster_points)),)
			new_centroids.append(new_centroid)
		
		return new_centroids

	for _ in range(max_iterations):
		clusters = assign_clusters(points, centroids)
		new_centroids = new_centroid_assign(points, clusters, k)

		if centroids == new_centroids:
			break
		centroids = new_centroids

	return centroids
