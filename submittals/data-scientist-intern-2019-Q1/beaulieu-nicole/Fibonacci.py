

# For the fibonacci sequence, each number is the sum of the two
# proceeding numbers: Fn = Fn−1 + Fn−2.

# Define a simple version of the algorithm.  Starting simple helps make sure that
# we've got the algorithm defined and working correctly.
def fibonacci(n):

    # Note that the loop below will execute if the value received is not greater than 1.
    # However, defining explicit error checking is still a good idea.
    if (n <= 0):
        print ("Invalid value received.  Sequence is calcuated for values greater than 1.")

    # For this implementation, the starting condiditions are: F1 = 1,F2 = 1
    f1 = 1
    f2 = 1

    # Keep track of the running total based on the rules: Fn = Fn−1 + Fn−2
    # By default, make the total 1.  This will accomodate n = 1.
    f_total = 1

    # In a simple implementation, we can use a loop to keep track of the
    # number of times we've calculated the current value of the sequence.
    for x in range (1, n):

        # This sequence is calculated for x > 1.
        if x > 1:
            f_total = f1 + f2
            f1 = f2
            f2 = f_total
        else:
            # The current total is 1 if there are not two values to add together.
            f_total = 1

        # Show progress.
        #print (f_total, flush=True)
    
    # Return the running total.
    return f_total

# Find the value in the fibonacci sequence.
nth_value = 10
# Use algorithm 1.
fib_total = fibonacci(nth_value)
print ("Algorithm 1 for value %d: %d" % (nth_value, fib_total))
print ("---")

# Find the first 20 values.
for x in range (1, 21):
    # Use algorithm 1.
    fib_total = fibonacci(x)
    print ("Algorithm 1 for value %d: %d" % (x, fib_total))

print ("---")

# Define a second version of the algorithm.  One approach is to use recursion.
def fibonacci2(n):

    # Keep track of the running total based on the rules: Fn = Fn−1 + Fn−2
    # It's reasonable to also return each value inline rather than assigning
    # to a variable, however, using the variable makes it easier to debug.
    f_total = 0
    if n <= 0:
        f_total = 0
    elif n > 1:
        # If there are at least 2 values to add together, call this function again
        # with the preceeding two values in the sequence.
        f_total = fibonacci2(n - 1) + fibonacci2(n - 2)
    else:
        return 1

    # Show progress.
    # print (f_total, flush=True)
    
    # Return the running total.
    return f_total

# Find the value in the fibonacci sequence.
nth_value = 10
# Use algorithm 1.
fib_total = fibonacci2(nth_value)
print ("Algorithm 2 for value %d: %d" % (nth_value, fib_total))

print ("---")

# Find the first 20 values.
for x in range (1, 21):
    # Use algorithm 1.
    fib_total = fibonacci2(x)
    print ("Algorithm 2 for value %d: %d" % (x, fib_total))

print ("---")
