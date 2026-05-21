"""
1-Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.
"""

def print_first():
    print('Imprime desde la primera funcion')
def print_second():
    print('Imprime la segunda funcion y luego:')
    print_first()
print_second()
