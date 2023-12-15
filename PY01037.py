# limax = [0 for _ in range((10 ** 7) * 2 + 5)]
#
# li = [0] * 20000001
# li[0] = li[1] = 1
# for i in range(2, 10000):
#     if li[i] == 0:
#         for j in range(i * i, 20000001, i):
#             li[j] = i
# for i in range(2, (10 ** 7) * 2 + 1):
#     if li[i] == 0:
#         li[i] = i
#
#
# def cnt(n):
#     rs = 1
#     run = li[n]
#     while run != n:
#         cn = 1
#         while n % run == 0:
#             n = n // run
#             cn += 1
#         run = li[n]
#         rs *= cn
#     if n > 1:
#         rs *= 2
#     return rs
#
a = [1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360, 720, 840, 1260, 1680, 2520, 5040, 7560,
     10080, 15120, 20160, 25200, 27720, 45360, 50400, 55440, 83160, 110880, 166320, 221760, 277200,
     332640, 498960, 554400, 665280, 720720, 1081080, 1441440, 2162160, 2882880, 3603600, 4324320, 6486480,
     7207200, 8648640, 10810800, 14414400, 17297280]

arr = [1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360, 720, 840, 1260, 1680, 2520, 5040, 7560, 10080, 15120, 20160,
       25200, 27720, 45360, 50400, 55440, 83160, 110880, 166320, 221760, 277200, 332640, 498960, 554400, 665280, 720720,
       1081080, 1441440, 2162160, 2882880, 3603600, 4324320, 6486480, 7207200, 8648640, 10810800]


def binsearch(l, r, n):
    if l == r:
        return r
    mid = int((l + r) / 2)
    if arr[mid] == n:
        return mid
    if arr[mid] > n:
        return binsearch(l, mid, n)
    else:
        return binsearch(mid + 1, r, n)


N = arr[43] + 1
li = [1] * N
li[2] = 2
for i in range(43):
    for j in range(a[i] + 1, a[i + 1] + 1):
        li[j] = a[i + 1]

# for i in range(1, (10 ** 7) * 2 + 1):
#     limax[i] = cnt(i)
#     if limax[i] > limax[i - 1]:
#         arr.append(i)
#         print(i, end=" ")
#     else:
#         limax[i] = limax[i - 1]
# print(arr)
from sys import stdin

stdin.readline()
while True:
    try:
        z = int(stdin.readline())
        if z < N:
            print(li[z])
        else:
            for i in range(43, len(a)):
                if a[i] >= z:
                    print(a[i])
                    break
    except:
        break
