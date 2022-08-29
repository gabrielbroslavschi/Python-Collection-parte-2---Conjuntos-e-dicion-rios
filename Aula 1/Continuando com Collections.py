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