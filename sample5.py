def print_ascending(n):
    if n > 0:
        print_ascending(n - 1)
        print(n, end=' ')

n = int(input("Enter a number: "))

print_ascending(n)
