print("*" * 5, "Média Aritmética", "*" * 5)
y = 1
z = []

for i in range(0, 3):
    x = float(input(f"Digite sua nota {y}: "))
    y = y + 1
    z.append(x)

somar_nota = sum(z)
media_final = somar_nota / 3
print(f"Sua média é {media_final:.1f}")

if media_final >= 10:
    print("Você foi aprovado com graciosidade!")
elif media_final >= 7:
    print("Você foi aprovado!")
else:
    print("Você foi reprovado!")

