def Sum( a , b):

    if (b>a):
        a+b
    elif(a>b):
        a-b
    return a+b
def Main():
    nb1 = int(input("Nomber one"))
    nb2 = int(input("Nombre two"))
    Sum(nb1,nb2)
    print(Sum())
