#Count ways to reach the nth stair using step

'''
There are n stairs, a person standing at the bottom wants to reach the top.
The person can climb either 1 stair or 2 stairs at a time.
Count the number of ways, the person can reach the top.
'''


# A program to count the number of ways to reach n'th stair

# Recurssive program to find n'th fibonacci number
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


# returns no. of ways to reach s'th stair
def countWays(s):
    return fib(s + 1)


# Driver program

s = 6
print("Number of ways = ",)
print(countWays(s))

'''
We can easily find recursive nature in above problem. 
The person can reach n’th stair from either (n-1)’th stair or from (n-2)’th stair. 
Let the total number of ways to reach n’t stair be ‘ways(n)’. 
The value of ‘ways(n)’ can be written as following.

    ways(n) = ways(n-1) + ways(n-2)
The above expression is actually the expression for Fibonacci numbers, 
but there is one thing to notice, the value of ways(n) is equal to fibonacci(n+1).

ways(1) = fib(2) = 1
ways(2) = fib(3) = 2
ways(3) = fib(4) = 3

feb series :-
0 1 1 2 3 5 8 13 21 . . 
'''