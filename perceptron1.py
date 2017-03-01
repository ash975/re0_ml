import numpy as np

def check(item):
	is_correct = False
	while not is_correct:
		if(cal(item) <= 0):
			is_correct = False
			update(item)
		else:
			is_correct = True

def cal(item):
	return item[1] * np.dot(W, item[0])

def update(item):
	global W, history
	W = W + [[alpha * item[0][0] * item[1], alpha * item[0][1] * item[1], alpha * item[1]]]
	history = np.vstack((history, W))

def train(dataset, step):
	for _ in range(step):
		for item in dataset:
			check(item)

	print("history: \n", history)
	print("result: ", W)

train_set = [[(3,3,1), 1],[(4,3,1), 1],[(1,1,1),-1]]
W = np.array([[0,0,0]])
history = np.zeros((W.shape))
alpha = 1
num_step = 1000

train(train_set, num_step)
