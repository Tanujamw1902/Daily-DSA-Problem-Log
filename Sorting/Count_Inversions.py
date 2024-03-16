# Counting Inversions in an Array... 

def count_inversions(arr):
    """
    Function to count the number of inversions in an array using the merge sort algorithm.

    Args:
    - arr: The input array.

    Returns:
    - inversion_count: The number of inversions in the array.
    """
    # Initialize inversion count
    inversion_count = 0

    # Merge sort function to count inversions
    def merge_sort(arr):
        nonlocal inversion_count

        # Base case: If the array has only one element, it is already sorted
        if len(arr) <= 1:
            return arr

        # Split the array into two halves
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort the left and right halves
        left_half = merge_sort(left_half)
        right_half = merge_sort(right_half)

        # Merge the sorted halves and count inversions
        merged_arr = []
        i = j = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                merged_arr.append(left_half[i])
                i += 1
            else:
                merged_arr.append(right_half[j])
                j += 1
                inversion_count += len(left_half) - i  # Increment inversion count
        merged_arr.extend(left_half[i:])
        merged_arr.extend(right_half[j:])
        return merged_arr

    # Call the merge sort function
    merge_sort(arr)

    # Return the inversion count
    return inversion_count

# Main function to test the count_inversions function
if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]
    print(count_inversions(arr))
