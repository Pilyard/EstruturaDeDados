while True:
    try:
        print("Celcius para Fahrenheit!")

        c = float(input("Digite o valor para conversão: "))

        f = (c * 1.8) + 32

        print(f"Valor informado: ºC {c}")
        print(f"Valor convertido: ºF {f}")
        break
    except ValueError:
        print("O valor informado é inválido!")
    except KeyboardInterrupt:
        print("O programa foi interrompido!")
        break
