def print_triangular_numbers(n):
    for i in range(1, n + 1):
        w = ((i * (i + 1)) / 2)
        print(i, "   ", int(w))


print_triangular_numbers(10)
