
# coding: utf-8

# In[12]:

#Alternative implementation - non recursive solution
#Function definition
def fibonacci2(n):   
    current = 1
    previous = 0
    initial = 1
    while (initial < n):
            current, previous, initial = current+previous, current, initial+1
    return current
    
n = int(input("Please Enter a number: "))
print(fibonacci2(n))

