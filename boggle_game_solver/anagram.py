"""
File: anagram.py
Name: Joseph Liu
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# global variable
dictionary = []
anagrams = []


def main():
    """
    This program recursively finds all the anagram(s) for the word input by users.
    """
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    read_dictionary()
    while True:
        word = input('Find anagrams for: ')
        if word == '-1':
            break
        print('Searching...')
        global anagrams
        anagrams = []
        find_anagrams(word)
        print(str(len(anagrams))+' anagrams: '+str(anagrams))


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE and appends words in each line into a Python list.
    """
    with open(FILE, 'r') as f:
        for line in f:
            word = line.strip()
            dictionary.append(word)


def find_anagrams(s):
    """
    :param s: str, user input a word
    :return: function find_anagrams_helper
    """
    find_anagrams_helper(s, [], [], len(s))


def find_anagrams_helper(word, current_lst, index_lst, length):
    """
    :param word: str, users input
    :param current_lst: lst, storing each string of letter
    :param index_lst: lst, storing each index number
    :param length: int, length of word that input by users
    :return: print out the word be found
    """
    if len(current_lst) == length:
        found = ''
        for i in current_lst:
            found += i
        if found not in anagrams and found in dictionary:
            anagrams.append(found)
            print('found: ' + found)
            print('Searching...')
    else:
        for i in range(length):
            if i not in index_lst:
                # choose
                index_lst.append(i)
                current_lst.append(word[i])

                # explore
                if has_prefix(current_lst):
                    find_anagrams_helper(word, current_lst, index_lst, length)

                # un-choose
                index_lst.pop()
                current_lst.pop()


def has_prefix(sub_s):
    """
    :param sub_s: lst, current status.
    :return: boolean, if there is any words with prefix stored in sub_s.
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
