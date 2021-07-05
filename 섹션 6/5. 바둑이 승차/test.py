def dfs1():
    global a
    a = a + [4]
    print(a)
    cnt = 10
    print(cnt)


if __name__ == "__main__":
    a = [1, 2, 3]
    cnt = 3
    dfs1()
    print(a)
    print(cnt)
