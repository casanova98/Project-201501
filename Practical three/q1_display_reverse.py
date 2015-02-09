def reverse_int(n):
    list = []
    n = str(n)
    for c in n:
        list.append(c)
    list.reverse()
    reversed = "".join(list)
    print(reversed)
reverse_int(2345)