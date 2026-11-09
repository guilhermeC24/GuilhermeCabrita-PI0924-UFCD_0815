frase_do_tuga = input("Frase: ")
palavras_da_cena = frase_do_tuga.split()
contagem_bue_loka = {}

for palavra in palavras_da_cena:
    if palavra in contagem_bue_loka:
        contagem_bue_loka[palavra] += 1
    else:
        contagem_bue_loka[palavra] = 1

print(contagem_bue_loka)