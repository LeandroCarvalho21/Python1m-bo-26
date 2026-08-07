# Importe o módulo, crie main() e proteja sua chamada.

import random # importando todas as funções do modulo 
import random as r# importando todas as funções do modulo e atribuindo um apelido "r"
from random import randint # importando apenas uma função do modulo
import regras_estoque # importando todas as funções do modulo regras_estoque



print(r.randint(1,60)) #sorteira um número aleatorio de 1 até 60
serie=["homen-aranha","dragon ball z", "bob esponja"] #criando uma lista com nomes de series
print(f"A serie sorteada foi... {random.choice(serie)}") #sorteira um nome de uma serie



print(regras_estoque.calcular_valor(2,5000))
print(regras_estoque.classificar(5,2))

#importe o módulo, crie main() e proteja sua chamada.
#inicio da proteção dos módulos/chamada
def main():
    pass