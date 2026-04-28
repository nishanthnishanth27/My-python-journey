def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
        
        # If element is smaller than mid, it can only be in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        # Else the element can only be in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        # Element is not present in the array
        return -1

# Test the function
numbers = [2, 3, 4, 10, 40]
target = 10

result = binary_search(numbers, 0, len(numbers) - 1, target)

if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")
