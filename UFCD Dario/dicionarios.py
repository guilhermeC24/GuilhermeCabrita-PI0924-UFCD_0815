# not lista "[]" ; não é acessivél por index
# dicionario "{}" ; é acessivél por maping (key) ; Por exemplo: {"nome":"Guilherme"} , em que a key é "nome"abs

dic_pes = {"Nome":"Guilherme", "Idade":17, "Sexo":"M", "Tel":123456789}
print("Original: ",dic_pes)

# se "apelido ainda não existir cria nova entrada"
dic_pes["Apelido"]="Gui"
print("Adição (apelido): ",dic_pes)

# substituir valores já existentes localmente
dic_pes["Nome"]="Matheus"
dic_pes["Idade"]=18
dic_pes["Sexo"]="M"
dic_pes["Tel"]=987654321
dic_pes["Apelido"]="MT"
print("Substituição (local): ",dic_pes)

#print(dic_pes.keys()) # mostra todas as keys
#print(dic_pes.values()) # mostra todos os valores
#print(dic_pes.items()) # mostra as keys + valores

dic_pes.update({"Nome":"Pedro"})
dic_pes.update({"Apelido":"Gordo"})
print("Updates (local): ",dic_pes) 

# apaga a última entrada
dic_pes.popitem()
print("PopItem: ",dic_pes) 

# inacabado
#for key.value in dic_pes.items():
   # print(f"Chave: { key }, ")