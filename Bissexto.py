from calendar import isleap
print("|=|" * 5, "Ano Bissexto", "|=|" * 5)
anoBissexto = int(input("Digite qual ano deseja saber se é bissexto ou não: "))

if isleap(anoBissexto):
    print("É bissexto!")
else:
    print("Não é bissexto!")
