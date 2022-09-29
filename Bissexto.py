from calendar import isleap

while True:
    try:
        anoBissexto = int(input("Digite qual ano deseja saber se é bissexto ou não: "))

        if isleap(anoBissexto):
            print("É bissexto!")
            break
        else:
            print("Não é bissexto!")
            break
    except ValueError:
        print("Digite um ano válido!")
    except KeyboardInterrupt:
        print("O programa foi interrompido!")
        break
