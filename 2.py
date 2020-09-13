"""
Question : 
We are given a string input and a array of dictionary. Example dictionary: ['pro', 'gram', 'merit',
'program', 'it', 'programmer'] Find all method we can break the input string into strings inside
dictionary!

sample input : program
sample output: 
'pro', 'gram'
'program'
"""

def find_prefix(dictionary, word, temp = []):
	for x in dictionary:
		if word.startswith(x) :
			temp.append(x)
			word = word.split(x)[1]
			return find_prefix(dictionary, word, temp)

	return temp if not word else False

if __name__ == "__main__":
	dictionary = ['pro', 'gram', 'merit', 'program', 'it', 'programmer']
	word = input("Enter your value: ") 

	if word.startswith(tuple(dictionary)) :
		for x in dictionary :
			if word.startswith(x) :
				if word == x :
					print(x)
				else : 
					res = find_prefix(dictionary, word.split(x)[1],[x])
					if res : 
						print(', '.join(res))


	else : 
		print("< no way >")
