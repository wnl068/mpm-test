"""
question :
Palindrom adalah angka yang sama jika dibaca dari kiri atau kanan (misalnya 12321, 6226, dsb).
Saat ini diketahui bahwa hasil palindrom terbesar dari perkalian 2 bilangan 2 digit adalah 9009 =
91 * 99 Dengan berbekal input integer n sebagai jumlah digit (asumsikan n ≤ 4), carilah palindrom
terbesar dari perkalian angka n tersebut!

sample input : 2
sample output : 9009
"""
def is_palindrome(s):
    return s == s[::-1]

def perkalian_terbesar(b, s, n) :
	print(f"{b},{s}")
	h = b * s

	if isPalindrome(str(h)) :
		return f"{b}*{s} = {h}" 
	else :
		if b == s :
			b,s = b-1,n
		elif b > s :
			s = s-1
		else :
			b = b-1	
		return perkalian_terbesar(b,s,n)

if __name__ == "__main__":

	try:
	    value=int(input("Type a number:"))
	except ValueError:
	    print("This is not a whole number.")

	number = int('9'*value)

	print(perkalian_terbesar(number,number,number))
