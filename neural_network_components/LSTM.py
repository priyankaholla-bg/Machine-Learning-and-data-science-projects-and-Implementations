import numpy as np

class LSTM:
	def __init__(self, input_size, hidden_size):
		self.input_size = input_size
		self.hidden_size = hidden_size

		# Initialize weights and biases
		self.Wf = np.random.randn(hidden_size, input_size + hidden_size)
		self.Wi = np.random.randn(hidden_size, input_size + hidden_size)
		self.Wc = np.random.randn(hidden_size, input_size + hidden_size)
		self.Wo = np.random.randn(hidden_size, input_size + hidden_size)

		self.bf = np.zeros((hidden_size, 1))
		self.bi = np.zeros((hidden_size, 1))
		self.bc = np.zeros((hidden_size, 1))
		self.bo = np.zeros((hidden_size, 1))

	def forward(self, x, initial_hidden_state, initial_cell_state):
		outputs = [];
		C_t = initial_cell_state
		ht = initial_hidden_state

		def sigmoid(x):
			return 1 / (1 + np.exp(-x) )

		for token in x:
			token = token.reshape(-1,1)
			concat_input = np.vstack((ht, token))
			ft = sigmoid(self.Wf @ concat_input + self.bf)
			it =  sigmoid(self.Wi @ concat_input + self.bi)
			Ct_new = np.tanh(self.Wc @ concat_input + self.bc)
			C_t = ft * C_t + it * Ct_new
			ot = sigmoid(self.Wo @ concat_input + self.bo)
			ht = ot * np.tanh(C_t)
			outputs.append(ht)


		return outputs, ht, C_t

