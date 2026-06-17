oficina_geral = []

def cadastrar_ordem_serviço():
    print("\n---ORDEM DE SERVIÇO---")

    cliente = input("Nome do cliente: ")
    modelo_carro = input("Modelo de carro: ")

    while True:
        try:
            ano_carro = int(input("Ano do veiculo (AAAA): "))
            if ano_carro < 1900 or ano_carro > 2026:
                print("Por favor digite um ano válido")
                continue
            break
        except ValueError:
            print("ERROR! : o ano deve ser um número inteiro!")

    while True:
        try:
            quilometragem = int(input("Quilometragem do carro: "))
            if quilometragem < 0:
                print("Quilometragem inválida")
                continue
            break
        except ValueError:
            print("Erro: a quilometragem deve ser um número inteiro")

    necessita_revisao_completa = False
    if quilometragem > 1000 or ano_carro < 2020:
        print("\nAlerta de sistema: veículo necessita revisão preventiva")
        necessita_revisao_completa = True
    else:
        print("\nStatus: Manutenção de Rotina")

    lista_peca = []
    total_orcamento = 0.00

    print("\n---LANÇAMENTO DE PEÇAS E SERVIÇOS---")
    while True:
        peca = input("Nome de peça/serviço (ou 'fim' para encerrar): ").strip()
        if peca.lower() == "fim":
            break
        try:
            preco = float(input(f"Preço de '{peca}': R$ "))
            if preco < 0:
                print("O preço não pode ser negativo")
                continue

            lista_peca.append(peca)
            total_orcamento += preco

        except ValueError:
            print("ERRO: Preço inválido! Item desconsiderado. Tente novamente")

    ordem_serviço = {
        "cliente": cliente,
        "veiculo": modelo_carro,
        "ano": ano_carro,
        "km": quilometragem,
        "alerta_revisao": necessita_revisao_completa,
        "itens": lista_peca,
        "total": total_orcamento,
        "status": "Em aberto",
    }
    oficina_geral.append(ordem_serviço)
    print(f"\nOrdem de serviço de {cliente} gerada com sucesso!")


def lista_todas_as_ordem():
    print("\n" + 30 * "=")
    print("RELATÓRIO GERAL NA OFICINA")
    print(30 * "=")

    if not oficina_geral:
        print("Nenhum veículo em manutenção no momento")
        return

    for indice, ordem in enumerate(oficina_geral, 1):
        print(f"\n#OS: {indice} | Cliente: {ordem['cliente']} | Carro: {ordem['veiculo']}")
        print(f"#Ano: {ordem['ano']} | KM: {ordem['km']}")
        print(f"#Revisão Crítica: {'SIM' if ordem['alerta_revisao'] else 'NÃO'}")
        print(f"Itens trocados: {', '.join(ordem['itens']) if ordem['itens'] else 'Nenhum item lançado'}")
        print(f"Total: R$ {ordem['total']:.2f}")
        print(f"Status: {ordem['status']}")
        print("-" * 45)


def menu_principal():
    while True:
        print("\n==== SISTEMA INTELIGENTE ====")
        print("1. Cadastrar nova ordem de serviço")
        print("2. Listar ordem de serviço")
        print("3. Sair do sistema")

        opcao = input("Escolher uma opção: ")

        if opcao == "1":
            cadastrar_ordem_serviço()

        elif opcao == "2":
            lista_todas_as_ordem()

        elif opcao == "3":
            print("Fecha o sistema. Até logo, meu caro!")
            break
        else:
            print("Opção inválida!! Tente novamente")


