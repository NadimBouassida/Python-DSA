"""
2264. Largest 3-Same-Digit Number in String
"""

def largestGoodInteger(num: str) -> str:
    curr = num[0]
    rep = 1
    sub = ''
    for i in range(1,len(num)):
        if num[i] == curr:
            rep += 1
            if rep >= 3:
                if sub == '' or int(sub[0]) * 3 < int(curr) * 3:
                    sub = 3 * curr
        else:
            curr = num[i]
            rep = 1
    return sub


tests = ["222","6777133339","2300019","42352338"]
for test in tests:
    print(largestGoodInteger(test))
