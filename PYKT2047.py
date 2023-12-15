def binary_search(li, left, right, need):
    if left+1 == right:
        if li[left] > need:
            return left-1
        if li[right] <= need:
            return right
        return left
    if left == right:
        if li[left] > need:
            return -1
        return left
    mid = (left+right)>>1
    if li[mid] == need:
        return mid
    elif li[mid] < need:
        return binary_search(li, mid, right, need)
    else:
        return binary_search(li, left, mid-1, need)

test = int(input())
e = []
while True:
    try: e.extend(map(int, input().split()))
    except: break
I = 0
for _ in range(test):
    n = e[I]
    I += 1
    ox = e[I:I+n]
    I+=n
    h = e[I:I+n]
    I+=n

    prefix_sum = [0 for l in range(len(h))]
    prefix_sum[0] = h[0]
    for i in range(1, len(h)):
        prefix_sum[i] = prefix_sum[i-1]+h[i]

    st = []
    more = [-1 for l in range(len(ox))]
    for i in range(0, len(h)):
        while len(st) > 0 and h[st[-1]] <= h[i]:
            st.pop()
        if len(st) == 0:
            more[i] = -1
        else:
            more[i] = st[-1]
        st.append(i)
    # print(more)
    max_lit = [0 for l in range(len(ox))]
    for i in range(len(ox)):
        if more[i] == -1:
            max_lit[i] = h[i]*ox[i] - (prefix_sum[i]-h[i])
        else:
            max_lit[i] = max_lit[more[i]] + h[i]*(ox[i]-ox[more[i]]-1) - (prefix_sum[i]-prefix_sum[more[i]]-h[i])
    for i in range(len(max_lit)):
        max_lit[i] += 1
    num = e[I]
    I+=1
    for q in range(num):
        w = e[I]
        I+=1
        pos = binary_search(max_lit, 0, len(max_lit)-1, w)
        print(pos+1)