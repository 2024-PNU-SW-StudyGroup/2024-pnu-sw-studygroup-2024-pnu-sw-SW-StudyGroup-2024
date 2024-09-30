A,B = map(int, input().split())


x, y = A, B
while y != 0:
    x, y = y, x % y

    gcd = x

lcm = (A * B) // gcd


print(gcd)
print(lcm)
