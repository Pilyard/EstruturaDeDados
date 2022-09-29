while True:
    try:
        print("Precisa ser entre 0 e 10!")
        numero = int(input("Digite um número: "))

        if numero >= 0 and numero <= 10:
            print("Parabéns!")
            break

    except ValueError:
        print("Esse número não é válido!")
    except KeyboardInterrupt:
        print("O programa foi interrompido!")
        break
