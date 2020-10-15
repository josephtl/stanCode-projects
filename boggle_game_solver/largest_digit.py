"""
File: largest_digit.py
Name: Joseph Liu
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	"""
	The program print the biggest digit in 5 different intergers.
	"""
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int, given number
	:return: int, the largest digit among the number
	"""
	if n < 0:
		n *= -1
	return find_largest_digit_helper(n, 0)


def find_largest_digit_helper(n, biggest):
	"""
	:param n: int, given number
	:param biggest: int, current biggest digit
	:return: int, the biggest digit
	"""
	if n == 0:
		return biggest
	else:
		current = n % 10
		if current > biggest:
			biggest = current
		return find_largest_digit_helper(n // 10, biggest)


if __name__ == '__main__':
	main()
