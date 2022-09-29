while True:
    try:

        Primeiro_Numero = float(input("Digite o primeiro valor: "))
        Segundo_Numero = float(input("Digite o segundo valor: "))
        Terceiro_Numero = float(input("Digite o terceiro valor: "))

        Resultado_Media = (Primeiro_Numero + Segundo_Numero + Terceiro_Numero) / 3
        print(f"A sua média foi {Resultado_Media:.1f}")

        if Resultado_Media >= 10:
            print("Aprovado com excêlencia!")
            break
        elif Resultado_Media >= 7:
            print("Aprovado!")
            break
        else:
            print("Reprovado!")
            break

    except ValueError:
        print("Isso não é um número!")
    except KeyboardInterrupt:
        print("O programa foi interrompido!")
        break
