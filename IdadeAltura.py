lista_altura = []
lista_idade = []
lista_nome = []
lista_pessoas = 0

for i in range(0, 5):
    lista_pessoas += 1
    print("* Paciente * ", lista_pessoas)

    nome_pessoa = str(input("Digite o seu nome: "))
    lista_nome.append(nome_pessoa)

    idade_pessoa = int(input("Digite sua idade: "))
    lista_idade.append(idade_pessoa)

    altura_pessoa = float(input("Digite sua altura: "))
    lista_altura.append(altura_pessoa)

print("\nNome(s): ", lista_nome[::-1])
print("Idade: ", lista_idade[::-1])
print("Altura: ", lista_altura[::-1])
