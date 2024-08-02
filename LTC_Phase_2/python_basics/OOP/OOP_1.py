#Functions with parameters, placeholders and return function

def hell_fun(greeting, name):
    return '{} {} Bob '.format(greeting, name)

print(hell_fun('Hi', 'Bettle').upper())

def hell_fun(greeting, name='someone'):
    return '{} {} Bob '.format(greeting, name)

print(hell_fun('Hi', 'Torey').upper())