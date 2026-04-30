def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return f"Element found at index {index}"
    return "Element not found"

# Example usage:
numbers = [10, 23, 45, 70, 11, 15]
print(linear_search(numbers, 70))
