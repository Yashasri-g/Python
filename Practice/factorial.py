# without recursion
def fact(n):
    if n == 0 :
        return 1 
    fact = 1
    while n > 0:
        fact *= n
        n -= 1
    return fact

# with recursion
def fact(n):
  if n == 1 or n==0 :
    return 1
  else:
    factorial = n* fact(n-1)
  return factorial
