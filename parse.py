import codecs
import re


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

	return words

def find(word, suffix = 3):
	collector = []
	last = word[-suffix:]
	for w in parse():
		m = re.search(r'{0}$'.format(last), w)
		if m is not None:
			collector.append(w)

	return {
			'word': word,
			'suffix': last,
			'words': list(set(collector)),
			'len': len(list(set(collector)))
		}



find = find('მარადიული', 4)

print("სულ {0} გაერითმა სიტყვას :{1}: :{2}:-ზე".format(find['len'],find['word'],find['suffix']))
print(find['words'])
