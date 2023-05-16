
# Online Python - IDE, Editor, Compiler, Interpreter

def phi(n):
    """
    Computes the Euler's totient/phi function of a given number n.
    """
    phi_value = n
    i = 2
    while i * i <= n:
        if n % i == 0:
            phi_value -= phi_value // i
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        phi_value -= phi_value // n
    return phi_value
print(phi(70))