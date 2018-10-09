#TIC TAC TOE STRUCTURE


positions = [0,0,0,0,0,0,0,0,0]
dataset = {}

#parameters

#FUNCTIONS:

def show(positions):
	translator = {0: ' ', 1:'X', 2:'O'}
	print('''
		|{}|{}|{}|
		|{}|{}|{}|
		|{}|{}|{}|'''.format(*(translator[i] for i in positions)))

def updatePositions(positions, index, symbol):
	newpositions = list(positions)
	newpositions[index-1] = symbol
	return newpositions

def checkWin(positions, printfeature=True):
	for z in range(2):
		symbol = 1+z
		for a in range(3):
			if positions[3*a:(3*a)+3].count(symbol)==3:
				if printfeature:
					if symbol==1:
						print('PLAYER WINS')
					else:
						print("PC WINS")
				return True
		for b in range(3):
			if [positions[b], positions[b+3], positions[b+6]].count(symbol)==3:
				if printfeature:
					if symbol==1:
						print('PLAYER WINS')
					else:
						print("PC WINS")
				return True
		if [positions[0], positions[4], positions[8]].count(symbol)==3 or [positions[2], positions[4], positions[6]].count(symbol)==3:
			if printfeature:
				if symbol==1:
					print('PLAYER WINS')
				else:
					print("PC WINS")
			return True

def checkTie(positions, printfeature):
	if positions.count(0)==0:
		if printfeature:
			print('TIE')
		return True

def manualMove(positions, symbol=1):
	while True:
		try:
			move = int(input())
			if move not in list(range(10)) or positions[move-1]!=0:
				print('Choose an available place')
			else:
				return updatePositions(positions, move, symbol)
		except ValueError:
			print('Choose a number from 1 to 9')

