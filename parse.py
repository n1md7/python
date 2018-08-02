import codecs
import re
import random

def parse():
	file = codecs.open('book.txt', encoding='utf-8')

	words = []
	for line in file:

		line = line.rstrip()
		wordLines = re.split(r'\,|\.|\s', line)

		for wrd in wordLines:
			parsed = re.sub(r'[^ა-ჰ]+','', wrd)
			if len(parsed) > 0:
				words.append(parsed)

	return {
			'words': words,
			'size' : len(words)
		}

def find(word, suffix = 3):
	collector = []
	last = word[-suffix:]
	parsed = parse()
	# print("სულ სიტყვები: {0}".format(parsed['size']))
	for w in parsed['words']:
		m = re.search(r'{0}$'.format(last), w)
		if m is not None:
			collector.append(w)

	return {
			'word': word,
			'suffix': last,
			'words': list(set(collector)),
			'len': len(list(set(collector)))
		}

def countVowel(word):
	vowels = re.findall(r'[აეიოუ]{1}', word)

	return 	{
		'vowels': vowels,
		'size' : len(vowels)
	}


def makePoem(lines = 2, lineVowels = 12, suffix = 4):
	allWords = []
	parsed = parse()
	rythmWords = []
	for line in range(0, lines ):
		currentVowels = 0
		lineWords = []
		while currentVowels < 12:
			if len(parsed['words']) == 0:
				print('Out of words')
				return;
			rndIndex = random.randint(0, parsed['size'] - 1)
			currentWord = parsed['words'][rndIndex]
			vwl = countVowel(currentWord)
			if currentVowels + vwl['size'] <= lineVowels: 
				if line != 0 and currentVowels > 8:
					# take from last array the last word to find a rythm
					prevRythm = allWords[line-1][-1]
					# print('Rythmword is: {0}'.format(prevRythm))
					rythmWords = find(prevRythm, suffix) if len(rythmWords) == 0 else rythmWords
					# print(rythmWords)
					if len(rythmWords['words']) > 0:
						# print('rythm words are: {0}'.format(rythmWords['words']))
						# append first match
						lineWords.append(rythmWords['words'][0])
						rythmWords['words'].pop(0)
					else:
						print('Cannot find proper rythm word. Try again')
						return
				elif line != 0:		
					lineWords.append(currentWord)
				else:
					# first line generate
					lineWords.append(currentWord)

				currentVowels += vwl['size']
			#remove in all cases
			parsed['words'].remove(currentWord)
		# print('len: {0}'.format(currentVowels))
		allWords.append(lineWords)

	return allWords


poem = makePoem(4, 16, 3)
for line in poem:
	print(' '.join(line))

# print(countVowel('რომანებიისტორიული')['vowels'])



# find = find('მარადიული', 4)

# print("სულ {0} გაერითმა სიტყვას :{1}: :{2}:-ზე".format(find['len'],find['word'],find['suffix']))
# print(find['words'])
# ***************************************************************




# for x in find('მარადიული', 3):
# 	print(x)



# for w in words:
	# print(re.sub(r'[^ა-ჰ]+','+', w))

# you may also want to remove whitespace characters like `\n` at the end of each line
# content = [x.strip().encode('utf8') for x in content] 

# print(content)
