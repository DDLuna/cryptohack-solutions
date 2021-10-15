# GCD

def gcd(a, b):
    larger = max(a, b)
    smaller = min(a, b)
    quotient = larger // smaller
    remainder = larger % smaller
    if remainder == 0:
        return quotient
    return gcd(quotient, remainder)


def gcd_extended(a, b):
    # Base Case
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = gcd_extended(b % a, a)

    # Update x and y using results of recursive
    # call
    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y


print(gcd(66528, 52920))
print(gcd_extended(66528, 52920))
print(gcd_extended(26513, 32321))
print(gcd_extended(13, 3))
# Extended GCD

# Modular Arithmetic

# Modular Arithmetic 2

# Modular Inverting
