"""
File: boggle.py
Name: Joseph Liu
----------------------------------------
The program present the classic board game called boggle.
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# global
dictionary = []
user_input = []
found = []
answer = []


def main():
	"""
	This is a board game called boggle, it begin with user input 4X4 of alphabet, 16 in total.
	The program then store those letters and try to connect each letter into a word that exist in the dictionary.txt.
	The length of each word should be at least 4.
	"""
	for i in range(4):
		row = input(str(i+1) + ' row of letters: ')
		row = row.lower()
		if not illegal_input(row):
			break
		else:
			row_lst = row.split()
			user_input.append(row_lst)
			read_dictionary()
	if len(user_input) == 4:
		for k in range(4):
			for j in range(4):
				find_words([], k, j, '', [])
	print('There are ' + str(len(answer)) + ' words in total.')


def find_words(find_lst, index, index2, word, index_lst):
	"""
	:param find_lst: lst, current status to search
	:param index: int, rows index
	:param index2: int, index in each rows
	:param word: str, find_lst convert into str type
	:param index_lst: lst, chosen index number
	:return: print out the word be found
	"""
	if len(find_lst) > 3 and word not in found:
		# Storing the word that search before, even it is not an actual word.
		found.append(word)
		if word in dictionary:
			answer.append(word)
			print('Found "' + word + '"')
	# avoiding out of bound
	elif index >= 4 or index < 0 or index2 >= 4 or index2 < 0:
		return
	else:
		# choose
		if (index, index2) not in index_lst:
			index_lst.append((index, index2))
			find_lst.append(user_input[index][index2])
			# turn into string type
			word = ''
			for k in range(len(find_lst)):
				word += find_lst[k]
		else:
			return
		# explore
		if has_prefix(word):
			find_words(find_lst, index + 1, index2, word, index_lst)			# lower
			find_words(find_lst, index + 1, index2 + 1, word, index_lst) 		# lower right
			find_words(find_lst, index + 1, index2 - 1, word, index_lst)		# lower left
			find_words(find_lst, index, index2 + 1, word, index_lst)			# right
			find_words(find_lst, index, index2 - 1, word, index_lst)			# left
			find_words(find_lst, index - 1, index2 - 1, word, index_lst)   		# upper left
			find_words(find_lst, index - 1, index2 + 1, word, index_lst)		# upper right
			find_words(find_lst, index - 1, index2, word, index_lst)			# upper
		# un-choose
		find_lst.pop()
		index_lst.pop()


def illegal_input(row):
	"""
	:param row: str, user input
	:return: boolean
	"""
	for i in range(len(row)):
		if i % 2 == 1:
			if row[i] != ' ':
				print('Illegal input')
				return False
		elif len(row) > 7:
			print('Illegal input')
			return False
		else:
			if row[i].isalpha is False:
				print('Illegal input')
				return False
	return True


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		for line in f:
			word = line.strip()
			if len(line) > 4:
				dictionary.append(word)


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	count = 0

	word = ''
	for j in sub_s:
		word += j

	for i in dictionary:
		check = i.startswith(word)
		if check:
			count += 1

			if count > 0:
				return True
	if count == 0:
		return False


if __name__ == '__main__':
	main()
