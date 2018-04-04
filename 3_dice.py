import random
from collections import Counter


def flip():
	return random.randint(0,1)


def dice_roll():
	result = -1
	if flip():
		if flip():
			if flip():
				result = 1 
			else:
				result = 2
		else:
			if flip():
				result = 3 
			else:
				result = 4
	else:
		if flip():
			if flip():
				result = 5
			else:
				result = 6
		else:
			return dice_roll()
	return result


if __name__ == '__main__':
	thousand_rolls = Counter([dice_roll() for _ in range(1000)])
	print(thousand_rolls)

