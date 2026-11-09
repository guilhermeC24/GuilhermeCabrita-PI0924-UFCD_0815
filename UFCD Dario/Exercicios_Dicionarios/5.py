palavra_do_gajo = input("Palavra: ")
letras_bue_fixes = {}

for letra in palavra_do_gajo:
    if letra in letras_bue_fixes:
        letras_bue_fixes[letra] += 1
    else:
        letras_bue_fixes[letra] = 1

print(letras_bue_fixes)