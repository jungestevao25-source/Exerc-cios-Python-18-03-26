nota = float(input("Digite sua nota: "))

if nota >= 90:
    print("Excelente")
elif nota >= 70:
    if nota <= 89:
        print("Bom")
elif nota >= 50:
    if nota <= 69:
        print("Regular")
else:
    print("Insuficiente")