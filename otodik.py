def otodikFor():
    for i in range(60,-71,-1):
        if i < -69:
            print(str(i))
        else:
            print(str(i)+",",end="")

def otodikWhile():
    i = 60
    while i > -71:
        if i < -69:
            print(str(i))
        else:
            print(str(i)+",",end="")
        i -= 1