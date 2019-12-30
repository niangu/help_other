val_lines = [[[0,0],[21,21]],
        [[21,21],[-120,163]],
        [[-120,163],[-141,141]],
        [[-141,141],[0,0]],
        [[0,0],[163,163]],
        [[163,163],[148,177]],
        [[148,177],[-14,14]],
        [[-14,14],[0,0]],
        [[350,340],[500,340]],
        [[500,340],[500,355]],
        [[500,355],[350,355]],
        [[350,355],[350,340]],
[[500,355],[488,355]],
[[488,355],[488,155]],
[[488,155],[500,155]],
[[500,155],[500,355]],
[[488,155],[588,155]],
[[588,155],[588,175]],
[[588,175],[488,175]],
[[488,175],[488,155]]]


def search_dot(val_lines):
    abc = []
    var = 0
    abc_2 = []

    for i in val_lines:
        for j in i:
            var+=1
            abc_2.append(j)
            if var==8:
                abc.append(abc_2)
                abc_2 = []
                var=0
    #print(abc)

    abc_5 = []
    for j in abc:
        abc_3 = []
        abc_6 = []
        [abc_3.append(i) for i in j if not i in abc_3]
        abc_4 = sorted(abc_3)
        #print(abc_4)
        #print(abc_4[0], abc_4[3])
        abc_6.append(abc_4[0])
        abc_6.append(abc_4[3])
        abc_5.append(abc_6)
    #print(abc_5)
    return abc, abc_5

#dot内分别返回左下点和右上点
#rect返回分割的矩形，这个例子未考虑矩形相套，依次找8个点就可以返回一个矩形
#opencv里有遍历轮廓的方法，然后可以输出轮廓中所有矩形
rect, dot = search_dot(val_lines)
print(rect)
print(dot)