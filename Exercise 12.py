def head_and_tail(l):
    res=[]
    res.append(l[0])
    res.append(l[len(l)-1])
    return res


a = [5, 10, 15, 20, 25]
print(head_and_tail(a))