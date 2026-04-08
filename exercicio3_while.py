saldo=0.0

print("====BANCO SICREDI - sua conta ===\n ")

while True:
    print("\n 1.depositar |2. sacar |3. saldo |4.sair")
    op = input("Escolha: ")
    
    if op == "1":
        
        valor = float(input("valor para depositar R$: "))
        saldo += valor
        print(f"Depositar o valor R${saldo:.2f}")
    elif op =="2":
        valor = float(input("valor para sacar R$"))

        if valor<=saldo:
         saldo-= valor
         print(f"Saque realizado! saldo atual: R${saldo:.2f}")

        else:
            print("Saldo inuficiente!")

    elif op=="3":
       print(f"Saldo atual: R$: {saldo:.2f}")

    elif op=="4":
       print("Saindo!!")
       break
    
    else:
       print("escolha incorreta!")


