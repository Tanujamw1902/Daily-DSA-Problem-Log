# First Negative Integer In K Window Size... 

from collections import deque


def print_first_negative(arr, n, k):
    dq = deque()
    ans = []

    # Process the first window
    for i in range(k):
        if arr[i] < 0:
            dq.append(i)

    # Append the first negative integer in the window or 0 if no negative integer found
    if dq:
        ans.append(arr[dq[0]])
    else:
        ans.append(0)

    # Process remaining windows
    for i in range(k, n):
        # Remove elements from the front of the deque if they are out of the current window
        if dq and i - dq[0] >= k:
            dq.popleft()

        # Add the index of the negative integer to the deque
        if arr[i] < 0:
            dq.append(i)

        # Append the first negative integer in the window or 0 if no negative integer found
        if dq:
            ans.append(arr[dq[0]])
        else:
            ans.append(0)

    return ans

# Main function
if __name__ == "__main__":
    arr = [-8, 2, 3, -6, 10]
    k = 2
    n = len(arr)
    result = print_first_negative(arr, n, k)
    print(*result)
