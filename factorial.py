def factorial(n):
    x = 1
    for i in range(1,n+1):
        x *= i
    print("The factorial of {} is {}". format(n, x))

def sum_greater_than(numbers, n):
    x = 0
    for i in numbers:
        if i > n:
            x += i
    print("The sum of numbers greater than {} is {}". format(n, x))

#factorial(10)
#sum_greater_than([1, 2, 3, 4, 5], 1)