
def inicializacao():
    menu = ('''
    INICIAR SISTEMA DE GERENCIAMENTO DE CINEMA
    ------------------------------------------
        Criar um novo arquivo de dados? (s/n): ''')
    return menu

def mostrar_menu():
    menu = ('''
    SISTEMA DE GERENCIAMENTO DE CINEMA
    ----------------------------------
        1 - Adicionar filme
        2 - Listar filme
        3 - Buscar filme
        4 - Atualizar filme
        5 - Remover filme
        6 - Realizar venda de ingressos
        7 - Salvar dados
        0 - Sair
        Escolha uma opção: ''')
    return menu

def ler_dados():
    filmes = []
    cinedadosler = open(arquivo, "r", encoding='utf-8')
    linhas = cinedadosler.readlines()
    for linha in linhas:

        linha_limpa = linha.strip()
        if not linha_limpa:
            continue
        #Forma mais compactada de ler os dados
        id, titulo, genero, duracao, ano_lancamento, sinopse = linha.split(';')
        filme = {'id': int(id), 'titulo': titulo, 'genero': genero, 'duracao': duracao,
        'ano_lancamento': int(ano_lancamento), 'sinopse': sinopse}
        filmes.append(filme)
    return filmes

def salvar_dados(filmes):
    cinedados = open(arquivo, "w", encoding='utf-8')
    for filme in filmes:
        cinedados.write(f"{filme['id']};{filme['titulo']};{filme['genero']};\
{filme['duracao']};{filme['ano_lancamento']};{filme['sinopse']}\n")
    cinedados.close()
    print('Dados salvos com sucesso!')

def adicionar_filme(filmes):
    cinedados = open(arquivo, "w", encoding='utf-8')
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
        cinedados.write(f"{filme['id']};{filme['titulo']};{filme['genero']};\
{filme['duracao']};{filme['ano_lancamento']};{filme['sinopse']}")
    cinedados.close()
    print('Filme adicionado com sucesso!')

def listar_filmes(filmes):
    #verificar se há filme cadastrado
    if len(filmes) == 0:
        print('Nenhum filme cadastrado.\n')
    else:
        for filme in filmes:
            #impressão de forma mais compactada dos filmes
            print(f"ID: {filme['id']}; Título: {filme['titulo']}; Gênero: {filme['genero']}; \
Duração: {filme['duracao']} minutos; Ano de Lançamento: {filme['ano_lancamento']}; Sinopse: {filme['sinopse']}")

def buscar_filme(filmes):
    #verificar se há filme cadastrado
    if len(filmes) == 0:
        print("nenhum filme cadastrado")
        return    
    busca = input('Digite o id ou título do filme a ser buscado:')
    buscaid = 0
    buscacont = 0
    #verificar se é um digito para fazer a pesquisa por id
    if busca.isdecimal():
        buscaid = int(busca)
    for filme in filmes:
        if buscaid == filme['id'] or busca == filme['titulo']:
            print(f"ID: {filme['id']}; Título: {filme['titulo']}; Gênero: {filme['genero']}; \
Duração: {filme['duracao']} minutos; Ano de Lançamento: {filme['ano_lancamento']}; Sinopse: {filme['sinopse']}")
            buscacont +=1
    if buscacont == 0:
        print("filme não encontrado")

def atualizar_filme(filmes):
    if len(filmes) == 0:
        print("nenhum filme cadastrado")
        return
    busca = int(input('Digite o id do filme a ser atualizado:'))
    for filme in filmes:
        if busca == filme['id']:
            print(f"ID: {filme['id']}; Título: {filme['titulo']}; Gênero: {filme['genero']}; \
Duração: {filme['duracao']} minutos; Ano de Lançamento: {filme['ano_lancamento']}; Sinopse: {filme['sinopse']}")
            selecao = input('''
        0 - Atualizar filme completo
        1 - Atualizar informação específica
        Selecione uma opção: ''')
            while selecao !='0' and selecao !='0' and selecao == '':
                    chave = input('''
        Opção não identificada.
        Selecione uma opção novamente:''')
            if selecao == '0':
                titulo = input('Digite o título do filme: ')
                genero = input('Digite o gênero do filme: ')
                duracao = input('Digite a duração do filme (em minutos): ')
                ano_lancamento = int(input('Digite o ano de lançamento do filme: '))
                sinopse = input('Digite a sinopse do filme: ')
                filme['titulo'],filme['genero'],filme['duracao'],filme['ano_lancamento'],filme['sinopse'] = titulo,genero,duracao,ano_lancamento,sinopse
            elif selecao == '1':
                chave = input('''
        titulo - Alterar título
        genero - Alterar gênero
        duracao - Alterar duração
        ano_lancamento - Alterar ano de lançamento
        sinopse - Alterar sinopse
        Digite a informação a ser atualizada: ''')
                while chave not in filme or chave == '':
                    chave = input('''
        Informação não encontrada.
        Digite novamente a informação a ser atualizada:''')
                if chave in filme:
                    valor = input(f'Digite o novo valor para {chave}: ')
                    if chave == 'ano_lancamento' or chave == 'duracao':
                        valor = int(valor)
                    filme[chave] = valor
            return
    print("filme não encontrado")

criar = input(inicializacao())
arquivo = ''
while criar == '':
    criar = input('Opção não identificada. Digite novamente:')
while criar != 'n' and criar != 's':
    criar = input('Opção não identificada. Digite novamente:')
if criar == 's':
    arquivo = input('''
        Digite o nome do arquivo de dados (exemplo.txt): ''')
    while arquivo == '':
        arquivo = input('''
        Arquivo não encontrado.
        Digite o nome novamente (exemplo.txt): ''')
    cinedados = open(arquivo, "w")
    cinedados.close()
    print('Arquivo criado com sucesso!')
elif criar == 'n':
    arquivo = input('''
        Digite o nome do arquivo de dados (exemplo.txt): ''')
    while arquivo == '':
        arquivo = input('''
        Arquivo não digitado.
        Digite o nome novamente (exemplo.txt): ''')

filmes = ler_dados()
opcao = 1
while opcao != '0':
    opcao = input(mostrar_menu())
    if opcao == '1':
        adicionar_filme(filmes)
    elif opcao == '2':
        listar_filmes(filmes)
    elif opcao == '3':
        buscar_filme(filmes)
    elif opcao == '4':
        atualizar_filme(filmes)
    elif opcao == '5':
        remover_filme(filmes)
    elif opcao == '6':
        realizar_venda()
    elif opcao == '7':
        salvar_dados(filmes)
    elif opcao == '0':
        salvar_dados(filmes)
        print('Saindo do programa...')
    elif opcao == '':
        print('Opção vazia, digite novamente.')
    else:
        print('Opção não identificada.')