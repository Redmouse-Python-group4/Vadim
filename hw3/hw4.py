def mult(*args):
    tmp = 1
    for i in args:
        x = i**tmp
        tmp = i
        print x

mult(1, 10, 2, 4, 3, 5, 2, 8)
