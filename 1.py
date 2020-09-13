"""
Question :
Ada 1 list dictionary kata-kata, contoh: ["hot", "dot", "dog", "lot", "log"] User akan memberikan 2
input kata-kata (bisa saja tidak ada di dalam dictionary). Output adalah urutan untuk bisa mencari
cara paling singkat untuk mengubah kata pertama menjadi kata kedua, namun, tiap langkah
hanya bisa mengubah 1 huruf.

sample input  : hit lit
sample output : hit, hot, dot, dog, log, lig 
"""

def total_unmatch(word1, word2):
	return sum([1 for i in range(0,len(word1)) if word1[i] != word2[i]])


def find_step(dictionary,word1,word2):
	step = word1
	if len(word1) == len(word2) == len(dictionary[0]) :
		for x in dictionary:
			if total_unmatch(word1,x) == 1 :
				step += ', ' + x
				word1=x
			if total_unmatch(word1,word2) == 1 :
				step += ', '+ word2
				return step

	return "< no way >"


if __name__ == "__main__":
	dictionary = ["hot", "dot", "dog", "lot", "log"]
	print("sample input : hit lit")
	word = input("your turn: ").strip()

	print(find_step(dictionary,word.rsplit(' ',1)[0],word.rsplit(' ',1)[-1]))
