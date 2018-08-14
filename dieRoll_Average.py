from random import randint

print("Rolling the dice....")

result = 0

for trial in range(1,10000):
	result += randint(1,6)

print(str(result / 10000))
