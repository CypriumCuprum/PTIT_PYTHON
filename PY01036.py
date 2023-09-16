for _ in range(int(input())):
    n = int(input())
    rs = 0
    for i in range(n, 0,-2):
        rs += 1/i
    print("%0.6f"%(rs))