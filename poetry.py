import random

nouns = [
	'fossil',
	'horse',
	'aardvark',
	'judge', 
	'chef', 
	'mango', 
	'extrovert', 
	'gorilla'
	]
verbs = [
	'kicks',
	'jingles',
	'bounces',
	'slurps',
	'meows',
	'explodes',
	'curdles'
	]
adjectives = [
	'furry', 
	'balding', 
	'incredulous', 
	'fragrant', 
	'exuberent', 
	'glistening'
	]
prepositions = [
	'against',
	'after',
	'into',
	'beneath',
	'upon',
	'for',
	'in',
	'like',
	'over',
	'within'
	]
adverbs = [
	'curiously', 
	'extravagently',
	'tantalizingly',
	'furiously',
	'sensuously'
	]

poem_structure = """
    {prefix} {adj1} {noun1}
    {prefix} {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}
    {adverb}, the {noun1} {verb2}
    the {noun2} {verb3} {prep2} a {adj3} {noun3}
    """

def select_noun():
	noun1 = random.choice(nouns)
	noun2 = random.choice(nouns)
	noun3 = random.choice(nouns)
	while noun1 == noun2 or noun2 == noun3 or noun3 == noun1:
		noun2 = random.choice(nouns)
		noun3 = random.choice(nouns)
	return noun1, noun2, noun3

def select_verb():
	verb1 = random.choice(verbs)
	verb2 = random.choice(verbs)
	verb3 = random.choice(verbs)
	while verb1 == verb2 or verb2 == verb3 or verb3 == verb1:
		verb2 = random.choice(verbs)
		verb3 = random.choice(verbs)
	return verb1, verb2, verb3

def select_adj():
	adj1 = random.choice(adjectives)
	adj2 = random.choice(adjectives)
	adj3 = random.choice(adjectives)
	while adj1 == adj2 or adj2 == adj3 or adj3 == adj1:
		adj2 = random.choice(adjectives)
		adj3 = random.choice(adjectives)
	return adj1, adj2, adj3

def select_adverb():
	adverb = random.choice(adverbs)
	return adverb

def select_prep():
	prep1 = random.choice(prepositions)
	prep2 = random.choice(prepositions)
	while prep1 == prep2:
		prep2 = random.choice(prepositions)
	return prep1, prep2


def calculatePrefix(adjective):
	firstLetter = adjective[0]
	firstLetterLower = firstLetter.lower()
	vowels = ['a', 'e', 'i', 'o', 'u']

	while firstLetterLower in vowels:
		return 'An'
	else:
		return 'A'

def makePoem():
	noun1, noun2, noun3 = select_noun()
	verb1, verb2, verb3 = select_verb()
	adj1, adj2, adj3 = select_adj()
	prefix = calculatePrefix(adj1)
	prep1, prep2 = select_prep()
	adverb = select_adverb()

	return poem_structure.format(
		prefix = prefix,
		noun1 = noun1, noun2 = noun2, noun3 = noun3,
		verb1 = verb1, verb2 = verb2, verb3 = verb3,
		adj1 = adj1, adj2 = adj2, adj3 = adj3,
		prep1 = prep1, prep2 = prep2,
		adverb = adverb)
print(makePoem())
