d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

d_misturado = d1.copy()
d_misturado.update(d2)

print(d_misturado)