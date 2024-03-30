# Space Optimization In Dynamic Programming... 

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    prev1 = 1
    prev2 = 0

    for i in range(2, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr

    return prev1

if __name__ == "__main__":
    n = int(input("Enter the position of Fibonacci number: "))

    fib_n = fibonacci(n)

    print(f"Fibonacci number at position {n}: {fib_n}")
