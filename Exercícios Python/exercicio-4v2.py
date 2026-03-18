nota = float(input("Digite sua nota: "))

if nota >= 90 and nota <= 100:
    print("Excelente")
elif nota >= 70 and nota <= 89:
    print("Bom")
elif nota >= 50 and nota <= 69:
    print("Regular")
else:
    print("Insuficiente")
