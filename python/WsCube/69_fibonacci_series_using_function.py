"""
Write a python recursion function to print fibonacci series
"""
ls = []
def fibonacci(n, a=0, b=1):
    if n == 0:
        return
    else:
        ls.append(a)
        fibonacci(n-1, b, a+b)


# Example usage:
n = 10  # Number of terms in the Fibonacci series
fibonacci(n)
print(ls)
