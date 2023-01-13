import sys

def factorial(n):
	if n == 0: return 1
	return n * factorial(n-1)

try:
	n = int(sys.argv[1])
	if n < 0: sys.exit('Please enter a positive integer')
except ValueError: sys.exit('Please enter an integer')

print(factorial(n))
