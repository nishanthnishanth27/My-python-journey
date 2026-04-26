def count_characters(text):
    """Count frequency of each character"""
    freq = {}
    for char in text.lower():
        if char.isalnum():
            freq[char] = freq.get(char, 0) + 1
    return sorted(freq.items(), key=lambda x: x[1], reverse=True)

# Test
print(count_characters("Python"))  # [('p', 1), ('y', 1), ('t', 1), ('h', 1), ('o', 1), ('n', 1)]
