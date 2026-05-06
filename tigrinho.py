import random # 14. MÁQUINA DE SLOTS
simbolos = ["🐮", "🐷", "🐗", "🐭", "🐹", "🐰"]
saldo = 20.0
print("=== Kassinão do senai ===\n")
while saldo >=2:
    input("\nPressione Enter para girar (custa R$2,00")
    saldo -= 2.0

    resultado = [random.choice(simbolos) for _ in range(3)]
    print("|".join(resultado))

    if resultado[0] == resultado[1] == resultado [2]:
        premio = 20
        saldo += premio
        print(f" JACKPOT!!! Você ganhou R$ {premio}!")
    else:
        print("Não foi dessa vez...")