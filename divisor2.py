def factor(n):
    if n > 1: return n * factor(n - 1)
    elif n >= 0: return 1
    else: return -1

def Multiple(x, n):
    for i in range(1, n):
        if x % i != 0:
            return False
    return True

def largest_prime(n):
    i = n
    while i < factor(n):
        if Multiple(i, n):
            return i
        i += n
    return -1

print (largest_prime(20))
