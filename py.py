def calcular(*args):
    r = sum(args)
    for i in args:
        r += i
    return r

calcular(1, 4, 5)