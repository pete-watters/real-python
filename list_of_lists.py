universities = [
  ['CALI', 2175,37704],
  ['Harvard', 19627, 39849],
  ['Princeton', 10566, 40732],
  ['DCU', 7802, 37000],
  ['Trinity', 5879, 35551],
  ['Yale', 19535, 40569],
  ['Yale', 11701, 40500],
]

def mean(list):
	length = len(list)
	sum = 0
	for item in list:
		sum += item
	mean = sum / length
	return int(mean)	

def median(list):
	list.sort()
	print('sorted median', list)
	length = len(list)
	halfLength = length // 2
	return list[halfLength]

def enrollment_stats(uniList):
	enrollment = []
	fees = []
	for uni in uniList:
		enrollment.append(uni[1])
		fees.append(uni[2])
	print('**************************')
	print('Total students: ', enrollment)
	print('Total fees:', fees)
	print()
	print('Student mean', mean(enrollment))	
	print('Student median', median(enrollment))	
	print()
	print('Tuition mean', mean(fees))	
	print('Tuition median', median(fees))	
	print('**************************')




enrollment_stats(universities)
