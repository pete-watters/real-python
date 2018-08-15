from capitals import capitals_dict
import random

while True:
	capitalList = list(capitals_dict.keys())
	state = random.choice(capitalList)
	
	while True:
		print('Please enter the capital of: ', state)
		userInput = input().lower()
		capital = capitals_dict[state].lower()

		if(userInput == capital):
			print("Correct")
			break
		elif(userInput == 'exit'):
			print("Goodbye!")
			exit()
