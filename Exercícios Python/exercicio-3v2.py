idade = int(input("Digite sua idade | EX: 18: "))
valor_compra = float(input("Digite o valor | EX: 700.25: "))

if idade >=60 or valor_compra > 200:
    print("Cliente elegível para desconto")
else:
    print("Cliente sem desconto")