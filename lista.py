def mostrar_menu():
    print("\n" + "="*30)
    print("MENU - GERENCIADOR DE CONTATOS ")
    print("="*30)
    print("1. Adicionar contato")
    print("2. Alterar contato")
    print("3. Remover contato")
    print("4. Listar contatos")
    print("5. Sair")


def add_cont(contatos):
    nome = input("\nDigite o nome ddo contato: ")
    telefone = input("Digite o número do telefone: ")

    if nome in contatos:
        print("\n Contaato já existente! Adicionando outro número a ele.")
        contatos[nome].appendd(telefone)
    else:
        contatos[nome] = [telefone]

    print("\n✅ Contato adicionado com sucesso!")


def alterar_contato(contatos):
    nome = input("\nDigite o nome do contato a ser alterado: ")
    if nome in contatos:
        print(f"\nTelefone atualizado com sucesso!")
    else:
        print("\nContato não encontrado!")


def remover_contato(contatos):
    nome = input("\nDigite o nome do contato a ser removido: ")

    if nome in contatos:
        del contatos[nome]
        print("\nContato removido com sucesso!")
    else:
        print("\nContato não encontrado!")


def listar_contatos(contatos):
    if not contatos:
        print("\nNenhum contato salvo!")
        return

    print("\nLista de contatos:")
    for nome, telefones in contatos.items():
        print(f"{nome}: {', '.join(telefones)}")


def main():
    contatos = {}

    while True:
        mostrar_menu()
        escolha = input("\nEscolha uma opção: ")

        if escolha == '1':
            add_cont(contatos)
        elif escolha == '2':
            alterar_contato(contatos)
        elif escolha == '3':
            remover_contato(contatos)
        elif escolha == '4':
            listar_contatos(contatos)
        elif escolha == '5':
            print("\nSaindo do programa... Até mais!")
            break
        else:
            print("\nOperação invalida! Tente novamente")


if __name__ == "__main__":
    main()
