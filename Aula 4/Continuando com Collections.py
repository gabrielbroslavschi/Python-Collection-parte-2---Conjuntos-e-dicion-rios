from collections import defaultdict, Counter

usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]


assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)
print(assistiram)


print(set(assistiram))

print(set([4, 1, 2, 3, 1]))
print(type(set([4, 1, 2, 3, 1])))



usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

for usuario in set(assistiram):
    print(usuario)

print(usuarios_machine_learning | usuarios_data_science)

print(usuarios_machine_learning & usuarios_data_science)

print(usuarios_data_science - usuarios_machine_learning)

print(usuarios_data_science ^ usuarios_machine_learning)



usuarios = {1, 5, 76, 34, 52, 13, 17}
print(len(usuarios))

usuarios.add(13)
print(len(usuarios))

usuarios.add(765)
print(len(usuarios))

usuarios = frozenset(usuarios)
print(usuarios)
#usuarios.add(123)




meu_texto = 'Bem vindo ao meu github, eu estou usando essa aplicação me python para treinamento! Bem vindo'
print(set(meu_texto.split()))


aparicoes = {
    "Bem":2,
    "vindo":2,
    "ao":1,
    "meu":1
}
print(type(aparicoes))


print(aparicoes['Bem'])

print(aparicoes.get('testando', 0))
print(aparicoes.get('meu', 0))

del aparicoes['ao']

for elemento in aparicoes:
    print(elemento)

for elemento in aparicoes.keys():
    print(elemento)

for elemento in aparicoes.values():
    print(elemento)

for elemento in aparicoes.keys():
    print(elemento, aparicoes[elemento])

for elemento in aparicoes.items():
    print(elemento)

for chave, valor in aparicoes.items():
    print(chave, '=', valor)

print(['palavra {}'.format(chave) for chave in aparicoes.keys()])




"""meu_texto = meu_texto.lower()
aparicoes = defaultdict(int)
for palavra in meu_texto.split():
    aparicoes[palavra] += 1
print(aparicoes)"""

class Conta:
    def __init__(self):
        print('criando uma ocnta')

contas = defaultdict(Conta)
contas[19]
contas[17]
contas[22]


meu_texto = meu_texto.lower()
aparicoes = Counter(meu_texto.split())
print(aparicoes)