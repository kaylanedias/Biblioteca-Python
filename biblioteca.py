print('Bem-vindo(a) à Livraria da Kaylane Dias!\n')

lista_livros = []
id_global = 0

# Função para cadastro dos livros
def cadastrar_livro(id):
    global id_global
    print('-' * 40)
    print('-' * 11 + ' MENU DE CADASTRO ' + '-' * 11)
    print('-' * 40)

    id_global += 1 # Iniciar em 1
    print(f"\nCadastro de Livro - ID: {id_global}")
    titulo = input('Digite o Título do livro: ')
    autor = input('Digite o Autor do livro: ')
    editora = input('Digite a Editora do livro: ')

    livro = {
        'id': id_global,
        'titulo': titulo,
        'autor': autor,
        'editora': editora,
    }
    # Adiciona o livro à lista
    lista_livros.append(livro)
    print(f'\nLivro "{titulo}" cadastrado com sucesso!\n')

# Função para consultar os livros
def consultar_livro():
    while True:
        print('-' * 40)
        print('-' * 11 + ' MENU DE CONSULTA ' + '-' * 11)
        print('-' * 40)
        print('\nEscolha a opção desejada:')
        print('1 - Consultar Todos')
        print('2 - Consultar por ID')
        print('3 - Consultar por Autor')
        print('4 - Retornar ao Menu Principal')
        opcao = input('\n>> ')

        if opcao == '1':
            print('\n- Livros Cadastrados:\n')
            if lista_livros:
                for livro in lista_livros:
                    print(
                        f'ID: {livro["id"]} \nTítulo: {livro["titulo"]} \nAutor: {livro["autor"]} \nEditora: {livro["editora"]}\n')
            else:
                print("Nenhum livro cadastrado.")

        elif opcao == '2':
            try:
                id_livro = int(input('\nDigite o ID do livro: '))
                encontrado = False
                for livro in lista_livros:
                    if livro['id'] == id_livro:
                        print('\n- Livro Encontrado:')
                        print(
                            f'\nTítulo: {livro["titulo"]} \nAutor: {livro["autor"]} \nEditora: {livro["editora"]}\n')
                        encontrado = True
                        break
                if not encontrado:
                    print('ID inválido.')
            except ValueError:
                print("Por favor, insira um número válido para o ID.")

        elif opcao == "3":
            autor_consulta = input("\nDigite o nome do autor: ")
            encontrados = [livro for livro in lista_livros if livro["autor"].lower(
            ) == autor_consulta.lower()]
            if encontrados:
                print("\nLivros encontrados:\n")
                for livro in encontrados:
                    print(
                        f'ID: {livro["id"]} \nTítulo: {livro["titulo"]} \nAutor: {livro["autor"]} \nEditora: {livro["editora"]}\n')
            else:
                print("Nenhum livro foi encontrado para este autor.")
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

# Função para remover livros
def remover_livro():
    print('-' * 40)
    print('-' * 11 + ' MENU DE REMOÇÃO ' + '-' * 11)
    print('-' * 40)

    try:
        id_livro = int(input('\nDigite o ID do livro a ser removido: '))
        for livro in lista_livros:
            if livro['id'] == id_livro:
                lista_livros.remove(livro)
                print(f'\nLivro "{livro["titulo"]}" removido com sucesso!\n')
                break
        else:
            print('ID inválido. Nenhum livro removido.')
    except ValueError:
        print("Por favor, insira um número válido para o ID.")


# PROGRAMA PRINCIPAL
while True:
    print('-' * 40)
    print('-' * 12 + ' MENU PRINCIPAL ' + '-' * 12)
    print('-' * 40)
    print('\nEscolha a opção desejada:')
    print('1 - Cadastrar Livro')
    print('2 - Consultar Livro(s)')
    print('3 - Remover Livro')
    print('4 - Sair')
    opcao = input('\n>> ')

    if opcao == '1':
        cadastrar_livro(id_global)
    elif opcao == '2':
        consultar_livro()
    elif opcao == '3':
        remover_livro()
    elif opcao == '4':
        print('Finalizando o sistema...')
        break
    else:
        print('Opção inválida. Tente novamente.')
