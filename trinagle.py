for i in range(5):
    print(' ' * (2 * i) + ' '.join(str(5 - j) for j in range(i, 5)))
