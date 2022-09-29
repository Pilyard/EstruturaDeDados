while True:
    try:
        x = float(input("Digite um número entre 0 e 10 que desejar: "))
        if 0 <= x <= 10:
            print("Parabéns, você acertou!")
            break
        else:
            print(f"Tente novamente! {x:.0f} não é correspondente.")
    except ValueError:
        print("Os dados que você digitou está inválido, tente novamente!")
    except KeyboardInterrupt:
        print("\nO programa foi interrompido!")
        break
