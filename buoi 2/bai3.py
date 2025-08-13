def fibonacci(n):
    if n <= 0:
        return None
    elif n == 1 or n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b
indices = [2, 3, 4, 6]
for i in indices:
    print(f"Fibonacci thứ {i} = {fibonacci(i)}")
print("\nDãy Fibonacci chuẩn 10 số đầu:")
fib_sequence = [fibonacci(i) for i in range(1, 11)]
print(fib_sequence)
