def soma(x, y):
    return f'{x} + {y} = {x + y}'


def subtracao(x, y):
    return f'{x} - {y} = {x - y}'


def divisao(x, y):
    return f'{x} / {y} = {x / y}'


def multiplicacao(x, y):
    return f'{x} x {y} = {x * y}'


def percentual(x, y):
    perc = (y / 100) * x
    return f'{y}% de {x} é igual a {perc:.1f}'
