def multInv(n, m):
    for a in range(1, m):
        if (n * a) % m == 1:
            return a
    return None

# Example usage
print(multInv(47, 1456)) 
