
# coding: utf-8

# In[1]:

#Function definition for recursive solution
def fibonacci(n):
    
    if n<=2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


n = int(input("Please Enter a number: "))
print(fibonacci(n))

