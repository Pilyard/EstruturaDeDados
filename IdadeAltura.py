x = 1
lista_age = []
lista_heigh = []
lista_name = []
try:
    for i in range(0, 5):
        name = str(input(f"{x}º pessoa: \nDigite seu nome: "))
        age = int(input("Digite sua idade: "))
        heigh = float(input("Digite sua altura: "))
        x = x + 1
        lista_age.append(age)
        lista_heigh.append(heigh)
        lista_name.append(name)
except ValueError:
    print("Tente novamente!")
except KeyboardInterrupt:
    print("O programa foi interrompido!")
except TypeError:
    print("Por favor, digite os valores correto!")

for z in reversed(lista_age):
    continue
for c in reversed(lista_heigh):
    continue
for y in reversed(lista_name):
    continue

    print(f"\nNome:", lista_name[4], "\nIdade:", lista_age[4], "\nAltura:", lista_heigh[4], "M")
    print(f"\nNome:", lista_name[3], "\nIdade:", lista_age[3], "\nAltura:", lista_heigh[3], "M")
    print(f"\nNome:", lista_name[2], "\nIdade:", lista_age[2], "\nAltura:", lista_heigh[2], "M")
    print(f"\nNome:", lista_name[1], "\nIdade:", lista_age[1], "\nAltura:", lista_heigh[1], "M")
    print(f"\nNome:", lista_name[0], "\nIdade:", lista_age[0], "\nAltura:", lista_heigh[0], "M")
