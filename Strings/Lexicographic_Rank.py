# Program for Lexicographic Rank of String..

from math import factorial

MAX_CHAR = 256

def fact(n):
    return 1 if n <= 1 else n * fact(n - 1)

def populate_and_increase(count, s):
    for char in s:
        count[ord(char)] += 1
    for i in range(1, MAX_CHAR):
        count[i] += count[i - 1]

def update_count(count, ch):
    for i in range(ord(ch), MAX_CHAR):
        count[i] -= 1

def find_rank(s):
    length = len(s)
    mul = factorial(length)
    rank = 1
    count = [0] * MAX_CHAR
    populate_and_increase(count, s)
    for i in range(length):
        mul //= length - i
        rank += count[ord(s[i]) - 1] * mul
        update_count(count, s[i])
    return rank

# Example usage:
string = "Tanuja"
print(find_rank(string))
