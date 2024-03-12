def conversor(valorp, quantidade, moeda='real', **kwargs ):
    valortotal = valorp * quantidade

if 'desconto' in kwargs:
    desconto = kwargs['desconto']

    resultado = valortotal - ( valortotal * (desconto/100))

    