def transform(M: int) -> int:

    bits = list(map(int, bin(M)[2:][::-1]))

    while len(bits) < 5:
        bits.append(0)
    if sum(bits) % 2 == 0:

        for i in range(4):
            bits[i] = 1 - bits[i]
    else:

        for i in range(1, 5):
            bits[i] = 1 - bits[i]

    R = 0
    for i, b in enumerate(bits):
        R |= (b << i)
    return R


min_R = None
min_N = None
for N in range(64, 128):
    R = transform(N)
    if min_R is None or R < min_R:
        min_R = R
        min_N = N

print("Минимальное R =", min_R)
print("N (>63), дающее это R =", min_N)
