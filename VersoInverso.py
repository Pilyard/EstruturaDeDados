print("*" * 5, "Número Invertido", "*" * 5)

while True:
    try:
        numero = int(input("Digite o número inteiro que deseja inverter: "))
        numero = str(numero)
        numero_invertido = [numero]
        for x in numero_invertido:
            print("Inversão:", x[::-1])
        break

    except ValueError:
        print("A informação digitada está incorreta, tente novamente!")
    except KeyboardInterrupt:
        print("\nO programa foi interrompido!")
        break
    finally:
        print("Volte sempre! :)")
