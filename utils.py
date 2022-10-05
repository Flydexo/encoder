def reverse(list):
    rlist=[]
    for i in range(-1, -len(list)-1, -1):
        rlist.append(list[i])
    return rlist
