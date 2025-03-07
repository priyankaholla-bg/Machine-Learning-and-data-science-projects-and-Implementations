import numpy as np

def rnn_forward(input_sequence: list[list[float]], initial_hidden_state: list[float], Wx: list[list[float]], Wh: list[list[float]], b: list[float]) -> list[float]:
	ht = np.array(initial_hidden_state).reshape(-1,1)
	b = np.array(b).reshape(-1,1)
	Wx = np.array(Wx)
	Wh = np.array(Wh)
	for token in input_sequence:
		token = np.array(token).reshape(-1,1)
		ht = np.tanh(Wx @ token + Wh @ ht + b)
	final_hidden_state = ht
	return final_hidden_state
