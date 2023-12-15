for _ in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
    st = []
    for i in range(len(li)):
        if len(st) == 0:
            st.append(i)
            print(i + 1, end=" ")
        else:
            while len(st) > 0 and li[i] >= li[st[-1]]:
                st.pop()
                # print(st)
            if len(st) == 0:
                print(i + 1, end=" ")
            else:
                print(i - st[-1], end=" ")
            st.append(i)
    print()
