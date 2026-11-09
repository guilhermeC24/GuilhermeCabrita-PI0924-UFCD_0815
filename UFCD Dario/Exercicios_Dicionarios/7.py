d = {"a": 1, "b": 2, "c": 3}

d_ao_contrario = {}

for chave_fixe, valor_fixe in d.items():
    d_ao_contrario[valor_fixe] = chave_fixe

print(d_ao_contrario)