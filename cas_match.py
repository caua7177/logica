while True:
    print("===MENU===\n Voce deseja: salvar,carregar ou sair ?")
    comando=input("qual sua escolha:")
    
    match comando:
        case "salvar":
            print("salvando seu jogo...")
            break
        
        case "carregar":
            print("Carregando seu jogo...")
            break

        case "sair":
            print("saindo do jogo...")
            break

        case _:
            print("comando invalido")