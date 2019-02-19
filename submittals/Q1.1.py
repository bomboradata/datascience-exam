#--------------------------------------------------------------------------------------
# This the solution to the Q1.1
# There are three functions that compute Fibonacci number
print('-----------------------------------------------------------------------------------------')
print('Q1.1.1')
print('The function Fibonacci1 generates the Fibonacci number using while loop')

def Fibonacci1(n):
	F1, F2 = 1, 1 # F1 & F2 are the inital numbers in the Fibonacci series
	counts = 2 # counter for the while loop
	if n <= 2:
		return F2
	else:
		while counts < n:
			Fn = F2+F1 # Fibonacci formula
			F1, F2 = F2, F2+F1 # updating the two previous Fibonacci numbers
			counts+=1 # updating the counter
		return Fn

# Here is an example of function Fibonacci1
print('Example for fucntion Fibonacci1\n')
print('Fibonacchi number for n=4 is equal to: ', Fibonacci1(4))
print('------------------------------------------------------------------------------------------')
print('Q1.1.2')
print('The order of complexity for the function Fibonacci1, which is using while loop is O(n)')


print('------------------------------------------------------------------------------------------')
print('Q1.1.3')
print('The function Fibonacci2 generates the Fibonacci number using recursive function')
# Recursive function to generate Fibonacci number
def Fibonacci2(n):
	if n <= 2:
		return 1
	else:
		return Fibonacci2(n-1)+Fibonacci2(n-2)

# Here is an example of function Fibonacci2
print('Example for fucntion Fibonacci2\n')
print('Fibonacchi number for n=5 is equal to: ',Fibonacci2(5))
print('------------------------------------------------------------------------------------------')
print('Q1.1.4')
print('The order of complexity for the function Fibonacci1, which is using recursion is O(2*n)')
print('------------------------------------------------------------------------------------------')
# more efficient way to generate Fibonnaci number using cache
print('Q1.1.5')
print('The function Fibonacci3 generates the Fibonacci number using memoization')
def Fibonacci3(n, _cache = {}):
	if n in _cache:
		return _cache[n]
	elif n<= 2:
		return _cache.setdefault(n, 1)
	else:
		return _cache.setdefault(n, Fibonacci3(n-1)+Fibonacci3(n-2))

# Here is an example of function Fibonacci2
print('Example for fucntion Fibonacci3\n')
print('Fibonacchi number for n=8 is equal to: ',Fibonacci3(8))
print('------------------------------------------------------------------------------------------')
print('Q1.1.5')
print('By using memoization with the recursive function the order of complexity now is O(n) ')
