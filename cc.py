def isRainbow(r):
    current = 0
    for i in range((len(r) + 1) / 2):
        x, y = r[i], r[len(r) - 1 - i]
        if x != y or x > 7:
            return "no"
        elif x == current + 1:
            current = x
        elif x != current:
            return "no"

    if current == 7:
        return "yes"
    else:
        return "no"


T = int(raw_input().rstrip())
cases = [[] for i in range(T)]
for i in range(T):
    raw_input()
    cases[i] = [int(x) for x in raw_input().rstrip().split()]
for case in cases:
    print isRainbow(case)