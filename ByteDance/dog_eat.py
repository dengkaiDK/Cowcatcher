# Code Solution for ByteDance


a = list(map(int, input().split()))
M = int(input())

steps = 0

def eat_food(remain, num):
    if remain < min(a):
        return 1
    step = 0
    for item in a:
        if item <= num and item <= remain:
            step += eat_food(remain - item, item)

    return step

print(eat_food(M, max(a)))