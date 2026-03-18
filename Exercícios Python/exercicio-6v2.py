idade = int(input("Digite sua idade: "))
matricula_at = bool(input("Possui matrícula ativa ? (1 = sim, 0 = não): "))
autorisacao = bool(input("Possui autorização especial (1 = sim, 0 = não): "))

if idade >= 18:
    idade = True
else:
    idade = False


if autorisacao == True or (matricula_at == True and idade == True):
    print("Resultado: Acesso Permitido")
else:
    print("Resultado: Acesso Negado")