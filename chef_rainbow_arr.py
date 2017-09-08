



"""
Solving this problem :
https://www.codechef.com/problems/RAINBOWA
"""

" function to test rainbow array "
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


" geting the numbers and storing it in the matrix "
num = [[]]
t = int(raw_input())
if t >= 1 and t <= 100 :
    for a in range(0,t) :

        n = int(raw_input())

        if n >= 7 and n <= 100 :
            temp_n = []

            temp_n = map(int, raw_input().split())
            n = n + 1

            num.append(temp_n)
        a = a + 1

    del num[0]
    vx = 0

    " Testing the matrix  "

    for case in num :
        print isRainbow(case)

