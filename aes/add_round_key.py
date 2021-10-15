from matrix import matrix2bytes

state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

def add_round_key(s: list[list[int]], k: list[list[int]]):
    for row in range(len(s)):
        for col in range(len(s[0])):
            s[row][col] = s[row][col] ^ k[row][col]


if __name__ == '__main__':
    add_round_key(state, round_key)
    print(matrix2bytes(state))
