# Generating the Subarrays using Recurrsion Method...

def generate_subarrays(arr, start, end, result):
    if start > end:
        return
    
    # Include the current element and generate subarrays
    for i in range(start, end + 1):
        subarray = arr[start:i + 1]
        result.append(subarray)
        generate_subarrays(arr, i + 1, end, result)
        
    # Exclude the current element and generate subarrays
    generate_subarrays(arr, start + 1, end, result)

# Function to print all subarrays
def print_subarrays(arr):
    result = []
    generate_subarrays(arr, 0, len(arr) - 1, result)
    return result

# Example Usage
if __name__ == "__main__":
    arr = [1, 2, 3]
    subarrays = print_subarrays(arr)
    print("All subarrays of", arr, "are:")
    for subarray in subarrays:
        print(subarray)
