# Kth Largest Subarray Approach-1... 

def get_kth_largest(arr, k):
    sum_store = []
    n = len(arr)

    for i in range(n):
        sum_val = 0
        for j in range(i, n):
            sum_val += arr[j]
            sum_store.append(sum_val)

    sum_store.sort(reverse=True)  # Sorting in descending order
    return sum_store[k - 1]  # Return the kth largest sum

# Testcase
arr = [1, -3, 4, -2, -1, 6]
k = 3

print("Array:", arr)
result = get_kth_largest(arr, k)
print("Kth largest sum of subarrays:", result)
