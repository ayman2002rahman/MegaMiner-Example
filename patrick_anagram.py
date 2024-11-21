from itertools import permutations

def solve(s):
    constants = {}
    count = 0
    letters = ''
    for i, c in enumerate(s):
        if ord(c) not in range(ord('a'), ord('z')+1):
            constants[i-count] = c
            count += 1
        else:
            letters += c

    result = []
    for p in permutations(letters):
        word = ''
        for i, c in enumerate(p):
            if i in constants:
                word += constants[i]
            word += c
        result.append(word)
    return result

s = input()
for p in solve(s):
    print(p)