def inicializacao():
    menu = ('''     INICIAR SISTEMA DE GERENCIAMENTO DE CINEMA
     ------------------------------------------
            Criar um novo arquivo de dados? (s/n): ''')
    return menu
def mostrar_menu():
    menu = ('''     SISTEMA DE GERENCIAMENTO DE CINEMA
     ----------------------------------
            1 - Adicionar filme
            2 - Listar filme
            4 - Remover filme
            5 - Realizar venda de ingressos
            6 - Salvar dados
            0 - Sair
            Escolha uma opção: ''')
    return menu


def salvar_dados(filmes):
    cinedados = open(archive, "w")
    for filme in filmes:
        cinedados.write(f"{filme['id']},{filme['titulo']},{filme['genero']},\
{filme['duracao']},{filme['ano_lancamento']},{filme['sinopse']}\n")
    cinedados.close()
    print('Dados salvos com sucesso!')

def adicionar_filme(filmes):
    cinedados = open(archive, "w")
    id = len(filmes) + 1
    titulo = input('Digite o título do filme: ')
    genero = input('Digite o gênero do filme: ')
    duracao = input('Digite a duração do filme (em minutos): ')
    ano_lancamento = int(input('Digite o ano de lançamento do filme: '))
    sinopse = input('Digite a sinopse do filme: ')
    filme = {'id': int(id), 'titulo': titulo, 'genero': genero, 'duracao': duracao,
        'ano_lancamento': int(ano_lancamento), 'sinopse': sinopse}
    filmes.append(filme)
    print(filme)
    for filme in filmes:
        cinedados.write(f"{filme['id']},{filme['titulo']},{filme['genero']},\
            {filme['duracao']},{filme['ano_lancamento']},{filme['sinopse']}\n")
    cinedados.close()
    print('Filme adicionado com sucesso!')

def ler_dados():
    filmes = []
    cinedadosler = open(archive, "r")
    linhas = cinedadosler.readlines()
    for linha in linhas:
        id, titulo, genero, duracao, ano_lancamento, sinopse = linha.split(',')
        filme = {'id': len(filmes) + 1, 'titulo': titulo, 'genero': genero, 'duracao': duracao,
        'ano_lancamento': int(ano_lancamento), 'sinopse': sinopse}
        filmes.append(filme)
    return filmes 

def listar_filmes(filmes):
    if len(filmes) == 0:
        print('Nenhum filme cadastrado.\n')
    else:
        for filme in filmes:
            print(f"ID: {filme['id']}, Título: {filme['titulo']}, Gênero: {filme['genero']}, \
Duração: {filme['duracao']} minutos, Ano de Lançamento: {filme['ano_lancamento']}, Sinopse: {filme['sinopse']}\n")

def buscar_filme(filmes, busca):
    if filmes.size() == 0:
        print("Nenhum filme cadastrado.")
        return
    for filme in filmes:
        if busca == filme['id']:
            print("ID: {} ".format(filmes['id']))
            print("Título:{} ".format(filmes['titulo']))
            print("Gênero: {} ".format(filmes['genero']))
            print("Duração: {} ".format(filmes['duracao']))
            print("Ano de Lançamento: {} ".format(filmes['ano_lancamento']))
            print("Sinopse: {}".format(filmes['sinopse']))
            return
    print("Filme não encontrado") 

def excluir_filme(filmes, busca):
        for filme in filmes:
            if busca == filme['id']:
                filmes.remove(filme)
                return
        print("Filme não encontrado.")

criar = input(inicializacao())
archive = ''
if criar == 's':
    archive = input('Digite o nome do arquivo de dados (exemplo.txt): ')
    cinedados = open(archive, "w")
    cinedados.close()
    print('Arquivo criado com sucesso!')
elif criar == 'n':
    archive = input('Digite o nome do arquivo de dados (exemplo.txt): ')

filmes = ler_dados()
opcao = -1
while opcao != 0:
    opcao = int(input(mostrar_menu()))
    if opcao == 1:
        adicionar_filme(filmes)
    elif opcao == 2:
        listar_filmes(filmes)
    elif opcao == 3:
        busca = int(input("digite o id do filme: "))
        buscar_filme(filmes, busca)
    elif opcao == 4:
        #remover_filme()
        busca = int(input("Digite o nome do filme a ser excluído: "))
        excluir_filme(filmes, busca)
    elif opcao == 5:
        realizar_venda()
    elif opcao == 6:
        salvar_dados(filmes)
    elif opcao == 0:
        salvar_dados(filmes)
        print('Saindo do programa...')






        '''

#antes de def salvarDados
def atualizarPessoa (pessoas, busca, nome, idade, altura, sexo):
    if pessoas.size() == 0:
        print("nenhuma pessoa cadastrada")
        return
    for pessoa in pessoas:
        if busca == pessoa['id']: 
            pessoa['nome'] = nome
            pessoa['idade'] = idade
            pessoa['altura'] = altura
            pessoa['sexo'] = sexo
            return
    print("pessoa não encontrada")

#antes de def listarPessoas
def buscarPessoa(pessoas, busca):
    if pessoas.size() == 0:
        print("nenhuma pessoa cadastrada")
        return
        #a mesma coisa acontece para as outras funções
    for pessoa in pessoas:
        if busca == pessoa['id']:
            print("ID: ".format(pessoa['id']))
            print("Nome: ".format(pessoa['nome']))
            print("Idade: ".format(pessoa['idade']))
            print("altura: ".format(pessoa['altura']))
            print("sexo: ".format(pessoa['sexo']))
            return
    print("pessoa não encontrada")





    













        '''