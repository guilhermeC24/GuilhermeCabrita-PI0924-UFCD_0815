notas = {
    "João": [7, 8, 9],
    "Maria": [10, 9, 8],
    "Ana": [6, 7, 8]
}

for gajo, notas_do_gajo in notas.items():
    media_do_gajo = sum(notas_do_gajo) / len(notas_do_gajo)
    print(f"{gajo}: {media_do_gajo:.1f}")