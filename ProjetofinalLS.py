'''menu de inicialização para caso já exista um arquvio ou se for necessário criar'''
def inicializacao():
    menu = ('''
    INICIAR SISTEMA DE GERENCIAMENTO DE CINEMA
    ------------------------------------------
        Criar um novo arquivo de dados? (s/n): ''')
    return menu

'''menu principal do sistema, com as operações''' 
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

'''Função para ler o arquivo e iniciar o sistema'''
def ler_dados():
    filmes = []
    cinedadosler = open(arquivo, "r", encoding='utf-8')
    #ler todas as linhas do arquivo e armazenar em uma lista
    linhas = cinedadosler.readlines()
    #Para evitar linhas em branco
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

'''Função para salvar o arquivo'''
def salvar_dados(filmes):
    cinedados = open(arquivo, "w", encoding='utf-8')
    for filme in filmes:
        #Forma mais compactada do que a demonstrada na aula para salvar os dados
        cinedados.write(f"{filme['id']};{filme['titulo']};{filme['genero']};\
{filme['duracao']};{filme['ano_lancamento']};{filme['sinopse']}\n")
    cinedados.close()
    print('Dados salvos com sucesso!')

'''Função de adicionar filme com id automático'''
def adicionar_filme(filmes):
    cinedados = open(arquivo, "w", encoding='utf-8')
    #adiciona o i com base na quantidade de filmes
    id = len(filmes) + 1
    titulo = input('Digite o título do filme: ')
    genero = input('Digite o gênero do filme: ')
    duracao = input('Digite a duração do filme (em minutos): ')
    ano_lancamento = int(input('Digite o ano de lançamento do filme: '))
    sinopse = input('Digite a sinopse do filme: ')
    filme = {'id': int(id), 'titulo': titulo, 'genero': genero, 'duracao': duracao,
        'ano_lancamento': int(ano_lancamento), 'sinopse': sinopse}
    filmes.append(filme)
    print(f'''
    ID: {filme['id']}
    Título: {filme['titulo']} || Gênero: {filme['genero']}
    Duração: {filme['duracao']} minutos || Ano de Lançamento: {filme['ano_lancamento']}
    Sinopse: {filme['sinopse']}''')
    #Salva automaticamente um novo filme adicionado de forma compactada
    for filme in filmes:
        cinedados.write(f"{filme['id']};{filme['titulo']};{filme['genero']};\
Duração: {filme['duracao']};{filme['ano_lancamento']};{filme['sinopse']}")
    cinedados.close()
    print('Filme adicionado com sucesso!')

'''Função para listar todos os filmes no arquivo'''
def listar_filmes(filmes):
    #verificar se há filme cadastrado
    if len(filmes) == 0:
        print('Nenhum filme cadastrado.\n')
    else:
        for filme in filmes:
            #impressão dos filmes
            print(f'''
    ID: {filme['id']}
    Título: {filme['titulo']} || Gênero: {filme['genero']}
    Duração: {filme['duracao']} minutos || Ano de Lançamento: {filme['ano_lancamento']}
    Sinopse: {filme['sinopse']}''')

'''Função de busca para pesquisar os filmes por id ou título, caso haja mais de um filme com 
o mesmo título ou que o título seja igual a um id, ambos serão listados
A ideia é que caso a pessoa não saiba o nome exato do filme ou id'''
def buscar_filme(filmes):
    #verificar se há filme cadastrado
    if len(filmes) == 0:
        print("Nenhum filme cadastrado")
        return    
    busca = input('Digite o id ou título do filme a ser buscado:')
    buscaid = 0
    buscacont = 0
    #verificar se é um digito para fazer a pesquisa por id
    if busca.isdecimal():
        buscaid = int(busca)
    for filme in filmes:
        if buscaid == filme['id'] or busca.lower() in filme['titulo'].lower():
            print(f'''
    ID: {filme['id']}
    Título: {filme['titulo']} || Gênero: {filme['genero']}
    Duração: {filme['duracao']} minutos || Ano de Lançamento: {filme['ano_lancamento']}
    Sinopse: {filme['sinopse']}''')
            #Para caso encontre filme, adiciona 1 ao contador
            buscacont +=1
    #Para caso não encontre nenhum filme, o contador será 0
    if buscacont == 0:
        print("Filme não encontrado")

'''Função de atualizar os filmes por id, há a opção de atualizar o filme por 
completo ou apenas uma informação específica'''
def atualizar_filme(filmes):
    if len(filmes) == 0:
        print("Nenhum filme cadastrado")
        return
    busca = int(input('Digite o id do filme a ser atualizado:'))
    for filme in filmes:
        if busca == filme['id']:
            print(f'''
    ID: {filme['id']}
    Título: {filme['titulo']} || Gênero: {filme['genero']}
    Duração: {filme['duracao']} minutos || Ano de Lançamento: {filme['ano_lancamento']}
    Sinopse: {filme['sinopse']}''')
            selecao = input('''
        0 - Atualizar filme completo
        1 - Atualizar informação específica
        Selecione uma opção: ''')
            if selecao == '0':
                titulo = input('Digite o título do filme: ')
                genero = input('Digite o gênero do filme: ')
                duracao = input('Digite a duração do filme (em minutos): ')
                ano_lancamento = int(input('Digite o ano de lançamento do filme: '))
                sinopse = input('Digite a sinopse do filme: ')
                filme['titulo'],filme['genero'],filme['duracao'],filme['ano_lancamento'],filme['sinopse'] = titulo,genero,duracao,ano_lancamento,sinopse
                print('Filme atualizado com sucesso!')
                print('Não se esqueça de salvar os dados para confirmar alterações!')
            elif selecao == '1':
                chave = input('''
        titulo - Alterar título
        genero - Alterar gênero
        duracao - Alterar duração
        ano_lancamento - Alterar ano de lançamento
        sinopse - Alterar sinopse
        Digite a informação a ser atualizada: ''')
                if chave in filme:
                    valor = input(f'Digite o novo valor para {chave}: ')
                    if chave == 'ano_lancamento' or chave == 'duracao':
                        valor = int(valor)
                    filme[chave] = valor
                    print(f'{chave} atualizada com sucesso!')
                    print('Não se esqueça de salvar os dados para confirmar alterações!')
            return
    print("Filme não encontrado")

'''Função de remover o filme por id, com input para verificação'''
def remover_filme(filmes):
    if len(filmes) == 0:
        print("Nenhum filme cadastrado")
        return
    busca = int(input('Digite o id do filme a ser removido:'))
    for filme in filmes:
        if busca == filme['id']:
            print(f"ID: {filme['id']}; Título: {filme['titulo']}; Gênero: {filme['genero']}; \
Duração: {filme['duracao']} minutos; Ano de Lançamento: {filme['ano_lancamento']}; Sinopse: {filme['sinopse']}")
            verificacao = input('''
        Tem certeza que deseja remover este filme? (s/n): ''')
            if verificacao == 's':
                filmes.remove(filme)
                for filme in filmes:
                    if filme['id'] > busca:
                        filme['id'] -= 1
                print("Filme removido com sucesso!")
                print('Não se esqueça de salvar os dados para confirmar alterações!')
                return
            elif verificacao == 'n':
                print("Remoção cancelada.")
                return
    print("Filme não encontrado")

'''Função de realizar vendas de ingressos'''
def realizar_venda(filmes, ingtotal, ingtotal2):
    print(ingtotal, ingtotal2)
    buscacount = 0
    ingressoid = int(input('''
        VENDA DE INGRESSOS
        ------------------
        Digite o id do filme para o qual deseja comprar ingressos: '''))
    for filme in filmes:
        if ingressoid == filme['id']:
            buscacount +=1
            print(f"ID: {filme['id']}; Título: {filme['titulo']}; Gênero: {filme['genero']}; \
Duração: {filme['duracao']} minutos; Ano de Lançamento: {filme['ano_lancamento']}; Sinopse: {filme['sinopse']}")
            sala = input('''
        Salas de Exibição: 01 || 02
        Digite a sala de exibição: ''')
            #função while para evitar que o usuário digite uma entrada inválida
            while sala != '01' and sala != '02':
                sala = input('Sala inválida. Digite novamente:')
            ingressotipo = input('      Digite o tipo de ingresso (inteira/meia): ')
            while ingressotipo != 'inteira' and ingressotipo != 'meia':
                ingressotipo = input('Tipo inválido. Digite novamente: ')
            ingressoquant = 0
            ingressoquant2 = 0
            if sala == '01':
                print(f'     Ingressos disponíveis para o filme {filme["titulo"]} na sala 01: {ingtotal[ingressoid-1]}')
                ingressoquant = int(input(f'     Digite a quantidade de ingressos {ingressotipo} a ser comprada: '))
            if sala == '02':
                print(f'     Ingressos disponíveis para o filme {filme["titulo"]} na sala 01: {ingtotal2[ingressoid-1]}')
                ingressoquant = int(input(f'     Digite a quantidade de ingressos {ingressotipo} a ser comprada: '))
            maisopcao = input('     Deseja comprar mais ingressos? (s/n): ')
            if maisopcao == 's':
                ingressotipo2 = input('     Digite o tipo de ingresso (inteira/meia): ')
                while ingressotipo2 != 'inteira' and ingressotipo2 != 'meia':
                    ingressotipo2 = input('Tipo inválido. Digite novamente: ')
                ingressoquant2 = int(input(f'     Digite a quantidade de ingressos {ingressotipo} a ser comprada: '))
                print(f'''
                CONFIRMAÇÃO DE COMPRA
                ---------------------
                Ingresso para o filme: {filme['titulo']}
                Sala: {sala}
                Tipo: {ingressotipo} e {ingressotipo2}
                Quantidade: {ingressoquant} e {ingressoquant2} ''')
                verificacao = input('     Confirmar compra? (s/n): ')
                if verificacao == 's':
                    if sala == '01':
                        ingtotal[ingressoid-1] -= ingressoquant
                        ingtotal[ingressoid-1] -= ingressoquant2
                    if sala == '02':
                        ingtotal2[ingressoid-1] -= ingressoquant
                        ingtotal2[ingressoid-1] -= ingressoquant2
                    print(ingtotal, ingtotal2)
                    print("Venda de ingressos realizada com sucesso!")
                    return
                elif verificacao == 'n':
                    print("Venda de ingressos cancelada.")
                    return
            print(f'''
                CONFIRMAÇÃO DE COMPRA
                ---------------------
                Ingresso para o filme: {filme['titulo']}
                Sala: {sala}
                Tipo: {ingressotipo}
                Quantidade: {ingressoquant}''')
            verificacao = input('     Confirmar compra? (s/n): ')
            if verificacao == 's':
                if sala == '01':
                    ingtotal[ingressoid-1] -= ingressoquant
                if sala == '02':
                    ingtotal2[ingressoid-1] -= ingressoquant
                print("Venda de ingressos realizada com sucesso!")
                return
            elif verificacao == 'n':
                print("Venda de ingressos cancelada.")
                return
            else:
                print("Venda de ingressos cancelada.")
                return
    if buscacount == 0:
        print("Filme não encontrado")
        return

#caso não haja arquivo, criará um novo 
criar = input(inicializacao())
arquivo = ''

#Todo while que conter '' ou != (opções do input) é para evitar entradas em branco ou inválidas
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

#Para realizar a contagem de ingressos, foi necessário criar lista para cada sala e que fossem fora de alguma função
ingtotal= []
ingtotal2= []
for filme in filmes:
    ingtotal+=[30]
    ingtotal2+=[30]

#menu do sistema de gerenciamento
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
        realizar_venda(filmes, ingtotal, ingtotal2)
    elif opcao == '7':
        salvar_dados(filmes)
    elif opcao == '0':
        salvar_dados(filmes)
        print('Saindo do programa...')
    elif opcao == '':
        print('Opção vazia, digite novamente.')
    else:
        print('Opção não identificada.')