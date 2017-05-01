
# coding: utf-8

# In[10]:

#Q1.1.1
def fibonacci(n):
    if n <= 0:
        print ("incorrect input")
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci (n-2)
print (fibonacci(8))

#Q1.1.2
# time complexity : T(n) = T(n-1)+T(n-2) which is exponetial
# Space complexity O(1)


# In[11]:


#Q1.1.3
def fibonacci2(n):
    a = 1
    b = 1
    if n <= 0:
        print ("incorrect input")
    elif n == 1 or n == 2:
        return 1
    else:
        for i in range(3, n):
            c = a + b
            a = b
            b = c
        return b
    
print (fibonacci2(7))

#Q1.1.4
# time complexity : O(n)
# Space complexity : O(1)



# In[12]:

#Q1.1.5
# We can improve computational performance by storing fibonacci numbers calculated to an array
# We can optimize time complexity to O(log n) by recursive multiplication by representing fibonacci expression in matrix form


# In[ ]:

# Q2.2

To generate a random munber between 1 to 7 using a single 6-side die, we have to flip the die twice.
Then the nubers of each flip wil be (x,y).
usng equation (6(x-1)+y)/7 gives a number between 0 and 6.

