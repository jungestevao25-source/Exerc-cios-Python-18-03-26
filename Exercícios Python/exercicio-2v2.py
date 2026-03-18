temperatura = float(input("Digite a temperatura em Graus Celsius: "))

if temperatura < 10:
    print("Temperatura Baixa")
if temperatura >= 10 and temperatura <= 25:
    print("Temperatura agradável")
if temperatura > 25:
    print("Temperatura Alta")