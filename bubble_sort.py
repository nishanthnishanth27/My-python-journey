def bubble_sort(arr):
    n = len(arr)
    # List-la iruka ella elements-aiyum check panna
    for i in range(n):
        # Last elements already sorted-ah irukum, so n-i-1 varaikkum pona podhum
        for j in range(0, n - i - 1):
            # Pakkathu pakkathu numbers-ah compare pannanum
            if arr[j] > arr[j + 1]:
                # First number perusa iruntha, swap pannanum
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Test panna oru list
numbers = [64, 34, 25, 12, 22, 11, 90]
print("Original List:", numbers)

sorted_list = bubble_sort(numbers)
print("Sorted List:", sorted_list)

