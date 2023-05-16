def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def order(a, n):
    if gcd(a, n) != 1:
        return "a and n are not relatively prime"

    k = 1
    while True:
        if pow(a, k, n) == 1:
            return k
        k += 1
