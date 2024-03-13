# Counting frequencies of anarray elements...

def countFrequency(arr):
    # Initializing a dictionary to store element frequencies
    frequency_map = {}
    
    # Counting the frequency of each element in the array
    for num in arr:
        if num in frequency_map:
            frequency_map[num] += 1
        else:
            frequency_map[num] = 1
    
    # Printing the elements along with their frequencies
    for key, value in frequency_map.items():
        print(key, "-->", value)

# Main function
if __name__ == "__main__":
    arr = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3]
    countFrequency(arr)
