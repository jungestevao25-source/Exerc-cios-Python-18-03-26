idade = int(input("Digite sua idade: "))
matricula_at = int(input("Possui matrícula ativa ? (1 = sim, 0 = não): "))
autorisacao = int(input("Possui autorização especial (1 = sim, 0 = não): "))

if autorisacao == True:
    print("Resultado: Acesso Permitido")
elif idade == True:
    if matricula_at == True:
        print("Resultado: Acesso Permitido")
else:
    print("Resultado: Acesso Negado")