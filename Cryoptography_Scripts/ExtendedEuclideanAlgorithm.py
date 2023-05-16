def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = gcd_extended(b % a, a)
        return gcd, y - (b // a) * x, x

def linear_combination(a, b):
    gcd, x, y = gcd_extended(a, b)
    return "%d(%d) + %d(%d) = %d" % (a, x, b, y, gcd)