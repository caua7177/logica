opcao =0

while opcao != 3:
    print("===MENU===")
    print("1| saudação")
    print("2| info sistema")
    print("3|sair")

    try: 
        opcao = int(input("Escolha uma opção: "))

    except ValueError:
        print("porfavor digite apenas os numeros ")
        continue
        
    if opcao==1:
        print("Olá é um prazer ajudar vc ")

    elif opcao ==2:
        print("\nSistema python3.10")
        print("\nStatus: Operacional")

    elif opcao ==3:
        print("\nobrigado por usar o menu")
        break

    else:
        print("\n====ERRO====")