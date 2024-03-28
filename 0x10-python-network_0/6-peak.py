#!/usr/bin/python3

def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Args:
    - list_of_integers: A list of unsorted integers.

    Returns:
    - The peak element found in the list.
      If there are multiple peaks, return any one of them.
      If the list is empty, return None.
    """
    # Check if the list is empty
    if not list_of_integers:
        return None

    # Initialize pointers for binary search
    low = 0
    high = len(list_of_integers) - 1

    # Perform binary search to find the peak
    while low < high:
        mid = (low + high) // 2  # Calculate the middle index
        # Compare the middle element with its right neighbor
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            high = mid  # Move towards the left side of the list
        else:
            low = mid + 1  # Move towards the right side of the list

    return list_of_integers[low]  # Return the peak element found
