while True:
	userInput = input("Please enter an integer:")
	try:
		integerValue = int(userInput)
		break
	except ValueError:
		print("Error ahoy")
