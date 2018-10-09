from structure import dataset, manualMove, checkWin, checkTie, show
import random

winner_reward = 10
tie_reward = 10
lose_reward = -10

def smartMove(positions, x=True, randomize=True):
	if x:
		symbol = 1
	else:
		symbol = 2

	newpositions = list(positions)

	#define possibilities
	possibilities = []
	for i in range(len(positions)):
		if positions[i]==0:
			possibilities.append(i)

	if randomize:
		move = random.choice(possibilities)
	else:
		if tuple(positions) not in dataset:
			return smartMove(positions, x, randomize=True)
		else:
			data_output = dataset[tuple(positions)]
			sorted_output = sorted(data_output)[::-1]
			new_possibilities = []
			for l in range(9):
				bigger = sorted_output[l]

				for position in range(len(data_output)):
					if data_output[position]==bigger:
						new_possibilities.append(position)

				for new_possibility in new_possibilities:
					if positions[new_possibility]==0:
						move = new_possibility
						break

	dataset_add = [positions, move]
	newpositions[move] = symbol
	return (newpositions, dataset_add)

def updateDataset(dataset_adds, final):
	for dataset_add in dataset_adds:
		position_before_move = dataset_add[0]
		if tuple(position_before_move) not in dataset:
			dataset.update({tuple(position_before_move):[0,0,0,0,0,0,0,0,0]})
		if final=='win':
			dataset[tuple(position_before_move)][dataset_add[1]] += winner_reward
		elif final=='lose':
			dataset[tuple(position_before_move)][dataset_add[1]] += lose_reward
		else:
			dataset[tuple(position_before_move)][dataset_add[1]] += tie_reward

def chooseMove(positions, ceiling, randomize=False, x=False, playSerious=False):
	if randomize:
		newpositions, dataset_add = smartMove(positions, x=x, randomize=True)
		return (newpositions, dataset_add)
	elif playSerious:
		print('playing serious')
		newpositions, dataset_add = smartMove(positions, x=x, randomize=False)
		return (newpositions, dataset_add)
	randomic_choice = random.random()
	if randomic_choice>ceiling:
		lever = True
	else:
		lever = False
	newpositions, dataset_add = smartMove(positions, x=x, randomize=lever)
	return newpositions, dataset_add

def play(train=False, training_times = 100000, playSerious=False, randomizex=True):
	ceiling = 0.0
	change_tax = 0.000001

	if train:
		printfunction = False
	else:
		printfunction = True
	training_times = training_times+1
	while True:
		positions = [0,0,0,0,0,0,0,0,0]
		dataset_final_add = []

		moveorder = [1,2]
		random.shuffle(moveorder)

		training_times -=1
		ceiling+=change_tax

		if training_times%5000==0:
			print(training_times)
		if training_times==0:
			break


		if not train:
			show(positions)

		while True:
			#first move
			if moveorder[0]==1:
				if train:
					positions, dataset_add = chooseMove(positions, ceiling, randomize=randomizex, playSerious=playSerious, x=True)
				else:
					positions = manualMove(positions, 1)
			else:
				positions, dataset_add = chooseMove(positions, ceiling, playSerious=playSerious)
				dataset_final_add.append(dataset_add)

			if not train:
				show(positions)

			if checkWin(positions, printfunction):
				if moveorder[0]==2:
					updateDataset(dataset_final_add, final='win')
					break
				else:
					updateDataset(dataset_final_add, final='lose')
					break
			elif checkTie(positions, printfunction):
				updateDataset(dataset_final_add, final='tie')
				break

			#second move
			if moveorder[1]==1:
				if train:
					positions, dataset_add = chooseMove(positions, ceiling, randomize=randomizex, playSerious=playSerious, x=True)
				else:
					positions = manualMove(positions, 1)
			else:
				positions, dataset_add = chooseMove(positions, ceiling, playSerious=playSerious)
				dataset_final_add.append(dataset_add)

			if not train:
				show(positions)

			if checkWin(positions, printfunction):
				if moveorder[1]==2:
					updateDataset(dataset_final_add, final='win')
					break
				else:
					updateDataset(dataset_final_add, final='lose')
					break
			elif checkTie(positions, printfunction):
				updateDataset(dataset_final_add, final='tie')
				break

			
			#if training_times%5000==0:
			#	print(ceiling, training_times)


play(train=True, training_times=1000000, randomizex=True)

play(playSerious=True, randomizex=False)