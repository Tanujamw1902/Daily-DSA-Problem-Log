# Min Cost To Make String Valid... 

def min_cost(str):
    stack = []
    if len(str) % 2 == 1:
        return -1

    for ch in str:
        if ch == '{':
            stack.append(ch)
        else:
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(ch)

    a = 0
    b = 0
    while stack:
        if stack[-1] == '{':
            b += 1
        else:
            a += 1
        stack.pop()

    ans = (a + 1) // 2 + (b + 1) // 2
    return ans

if __name__ == "__main__":
    str = "{{"
    result = min_cost(str)
    print(result)
