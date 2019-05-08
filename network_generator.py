import numpy as np
class network():
	#Possible types: random, preferential-age, preferential-connections
	A = np.empty((size, size), dtype=bool)
	def __init__(self, size, probability_of_connection, network_type="random", num_connections=0):
		self.size = size
		self.probability_of_connection = probability_of_connection
		self.network_type = network_type
		self.num_connections = num_connections

	def create_network():
		for i in range(size):
			for j in range(size):
				if(i != j):
					A[i][j] = np.random.random_sample() < self.probability_of_connection
		print(A)

if __name__ == '__main__':
	new_network = network(5, .5)
	create_network()