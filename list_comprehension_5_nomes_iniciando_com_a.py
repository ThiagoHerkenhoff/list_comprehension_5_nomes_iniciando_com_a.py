"""
Dada uma lista de strings representando nomes, crie uma nova lista contendo apenas
os nomes que começam com a letra "A" e tenham menos de 6 caracteres.

nomes = ["Ana", "Arthur", "Alice", "Amanda", "Pedro", "André", "João", "Alex"]

Dica: Você pode usar o método startswith() para verificar se uma string começa com
a letra "A" e a função len() para verificar o comprimento da string.
"""

nomes = ["Ana", "Arthur", "Alice", "Amanda", "Pedro", "André", "João", "Alex"]

nomes_a = [nome for nome in nomes if nome.startswith('A') and len(nome) < 6]

print(nomes_a)

