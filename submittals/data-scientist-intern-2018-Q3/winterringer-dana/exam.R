export GH_USERNAME='dwinterringer'
export DS_POSITION='data-scientist-intern-2018-Q3'
export DS_EXAM_NAME='winterringer-dana'

#Q 1.1.1
fibonacci <- function(n)
{
  if (n == 0 || n == 1)
  {
    return(n)
  }
  else
  {
    return (fibonacci(n - 1) + fibonacci(n - 2))
  }
  for(i in 3:n)
  {
    fibonacci[1] <- 1
    fibonacci[2] <- 1
    fibonacci[i]
  }
}


#Q 1.1.2
#The efficiency of this implementation is O(2^n).

#Q 1.1.3
fibonacci2 <- function(n)
{
a <- c(1,1)
while(length(a) < n)
{
  temp <- length(a)
  temp2 <- a[temp] + a[temp - 1]
  a <- c(a, temp2)
}
return(a)
}

#Q 1.1.4
#The complexity of this implementation is O(n)

#Q 1.1.5
#An example to optimize performance would be to generally
#avoid additional steps of recursion with these functions.
#Additionally, using array/vector methods as opposed to
#the recursion fallback as a whole will improve performance.


#Q 2.2
dice <- sample(1:6, size = 2, replace = TRUE)
dice
sum(dice)
#we can 'roll a 7' simply by rolling the dice twice and computing
#the sum of both terms, giving us a chance at obtaining a '7'.

