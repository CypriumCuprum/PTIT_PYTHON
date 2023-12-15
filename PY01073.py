s = input()
visited = [0 for _ in range(11)]


def gen(x):
    if len(x) == len(s):
        print(x)
        return
    for i in range(len(s)):
        if visited[i] == 0:
            visited[i] = 1
            gen(x + s[i])
            visited[i] = 0


gen("")
