import random

nouns = ['fossil','horse','aardvark','judge', 'chef', 'mango', 'extrovert', 'gorilla']
verbs = ['kicks', 'jingles', 'bounces', 'slurps','meows', 'explodes', 'curdles']
adjectives = ['furry', 'balding', 'incredulous', 'fragrant', 'exuberent', 'glistening']
prepositions = ['against', 'after', 'into', 'beneath', 'upon', 'for', 'in', 'like', 'over', 'within']
adverbs = ['curiously', 'extravagently', 'tantalizingly', 'furiously', 'sensuously']

def calculatePrefix(adjective):
	firstLetter = adjective[0]
	firstLetterLower = firstLetter.lower()
	vowels = ['a', 'e', 'i', 'o', 'u']

	while firstLetterLower in vowels:
		return 'An'
	else:
		return 'A'

def poemTitle(prefix, adjective, noun):
	return "{} {} {}".format(prefix, adjective, noun)

def poemMain(title, adjectives, nouns, verbs, prepositions, adverbs):
	print("{} {} the {} {} {}, the {} {} the {} {} {} a {} {}".format(title, prepositions[0], adjectives[1], nouns[1], adverbs[0], nouns[0], verbs[1], nouns[1], verbs[3], prepositions[1], adjectives[4], nouns[2]))

def makePoem():
	adjectivesP = []
	nounsP = []
	verbsP = []
	prepositionsP = []
	adverbsP = []
	adjectivesP.append(random.choice(adjectives)) 
	nounsP.append(random.choice(nouns))

	prefix = calculatePrefix(adjectivesP[0])
	title = poemTitle(prefix,adjectivesP[0],nounsP[0])
	poem = poemMain(title,adjectivesP, nounsP, verbsP, prepositionsP, adverbsP)
	print(title)
	print("")
	print(poem)

makePoem()
