def fibonacci(n):
    """Generate Fibonacci series up to n terms"""
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

