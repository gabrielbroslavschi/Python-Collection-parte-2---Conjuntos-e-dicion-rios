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




meu_texto = 'Bem vindo ao meu github, eu estou usando essa aplicação me python para treinamento!'
print(set(meu_texto.split()))