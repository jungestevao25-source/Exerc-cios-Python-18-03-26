media = float(input("Digite a Média do Aluno: "))
frequencia = int(input("Digite a Freqência do Aluno: "))

import time
import sys

if frequencia < 75 or media < 40:
    print("Reprovado")
elif media >=40 and media <= 59:
    print("Recuperação")
elif media >= 60:
    print("Aprovado")
    
print("Fechando programa ...")
time.sleep(5)
sys.exit(0)