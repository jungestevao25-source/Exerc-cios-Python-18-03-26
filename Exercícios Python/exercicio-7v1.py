pontuacao = int(input("Digite a pontuação do participante: "))
tempo = int(input("Digite o tempo gasto (EM MINUTOS) do participante: "))

if pontuacao >= 90:
    print("Medalha de ouro")
    if tempo < 120:
        print("Participante destaque da competição")
elif pontuacao >= 70:
    print("Medalha de prata")
elif pontuacao >= 50:
    print("Medalha de Bronze")
else:
    print("Sem medalha")
    