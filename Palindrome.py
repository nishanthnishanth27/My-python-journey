def is_palindrome(text):
    """Check if text is palindrome (ignoring spaces & case)"""
    clean = text.lower().replace(" ", "")
    return clean == clean[::-1]
