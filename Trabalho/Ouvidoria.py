#Ouvidoria Universidade ABC
#1) Listar todas as manifestações 
#2) Listar todas as sugestões
#3) Listar todas as reclmações
#4) Listar todos os elogios
#5) Enviar uma manifestação (criar uma nova)
#6) Pesquisar protocolo por número (ID)
#7) Sair
print("Bem vindo a ouvidoria da Universidade ABC") #Inicio
print() #Espaço

#Variaveis:
opcoes = [] #Menu Principal
manifestacoes = [] #Lista de Manifestações
tipo = ["sugestoes", "reclamacoes", "elogios"] #Menu de reclamações
#posição:    0             1            2

#MENU:
while opcoes != 7: #Exibição de Menu
    print("1) Listar todas as manifestações")
    print("2) Listar todas as sugestões")
    print("3) Listar todas as reclmações")
    print("4) Listar todos os elogios")
    print("5) Enviar uma manifestação (criar uma nova)")
    print("6) Pesquisar protocolo por número (ID)")
    print("7) Sair)")
    print() #Espaço

#Interação com Usuario    
    opcoes = int(input("Digite a sua opção ")) #Escolher Menu
    print() #Espaço 

#Transforma Lista em quantidade de elementos
    quantidadeManifestacoes=len(manifestacoes) #Quantidade de casas

#Condição para a variavel entrar no if    
    if opcoes < 1 or opcoes > 7: #Condição
        print("Entrada Inválida") #Exibição de Erro
        print() #Espaço
    
#1 Listar todas as manifestações:
    if opcoes == 1: #LISTAR TODAS AS MANIFESTAÇÕES
        print("Manifestações") #Exibição
        print() #Espaço
        if quantidadeManifestacoes == 0: #Condição
            print("Não há manifestações!") #Exibição de Erro
            print()
        else:
            for mani in manifestacoes: #Transforma em Elementos
                print(mani) #Elemento
                print() #Espaço
            
#2 Listar todas as Sugestões:
    if opcoes == 2: #LISTAR TODAS AS SUGESTÕES
        print("Sugestões") #Exibição
        print() #Espaço
        for sugestoes in manifestacoes: #transformando em lista apresentavel
            sugestoesQuebrados = sugestoes.split("-") #quebrando o codigo, dividindo a lista
            if tipo[0] == sugestoesQuebrados[2]: #ligando o tipo a o problema
                sugestoesQuebrados.pop(2) #tirando a apresentação redundante
                print("Codigo ", end="") #apresentando o codigo e organizando horizontalmente
                for i in sugestoesQuebrados: #criando a apresentação completa
                    print("- " + i, end = " ") #espaçamento entre o codigo e organizando horizontalmente
                print() #espaço
            
#3 Listar todas as reclmações
    if opcoes == 3: #entrando na opção 3
        print("Reclamações") #apresentando aba
        print() #espaço
        for reclamacoes in manifestacoes: #transformando lista apresentavel
            reclamacoesQuebrados = reclamacoes.split("-") #quebrando a lista apresentavel
            if tipo[1] == reclamacoesQuebrados[2]: #ligando o tipo ao problema
                reclamacoesQuebrados.pop(2) #excluindo a redundancia
                print("Codigo ", end= " ") #exibindo o codigo e organizando horizontalmente
                for i in reclamacoesQuebrados: #criando a apresentação completa
                    print("- " + i, end = " ") #apresentando e organizando horizontalmente
                print() #espaço

#4 Listar todos os elogios
    if opcoes == 4: #entrando na opção 4
        print("Elogios") #exibindo aba
        print() #espaço
        for elogios in manifestacoes: #transformando lista apresentavel
            elogiosQuebrados = elogios.split("-") #quebrando a lista apresentavel
            if tipo[2] == elogiosQuebrados[2]: #ligando o tipo ao problema
                elogiosQuebrados.pop(2) #excluindo a redundancia
                print("Codigo ", end="") #exibindo o codigo e organizando horizontalmente
                for i in elogiosQuebrados: #criando a apresentação completa
                    print("- " + i, end = " ") #apresentando e organizando horizontalmente
                print() #espaço

#5 Enviar uma manifestação (criar uma nova)
#Transforma Lista em quantidade de elementos
    if opcoes == 5: #entrando na opção 5
        protocolo = len(manifestacoes) + 1 #transformando a lista em Quantidade de casas
        nome = input("Digite o seu nome: ") #interação com o usuario
        menu2 = -1 #entrando no while
        while menu2 <1 or menu2 >3: #condição do while
            menu2 = int(input("Digite 1 para Sugestões, 2 para Reclamações e 3 para Elogios ")) #interação com o usuario
            print()
            if menu2 <1 or menu2 >3:
                print("Digite novamente")
        descricao = input("Digite a sua descrição: ")
        print()
        dados = str(protocolo) + "-" + nome + "-" + tipo[menu2-1] + "-" + descricao
        manifestacoes.append(dados)
        print()

#6) Pesquisar protocolo por número (ID)

    if opcoes == 6:
        print("Protocolo")
        pesquisa = -1
        tamanhoManifestacoes = len(manifestacoes)
        while pesquisa <=0 or pesquisa > tamanhoManifestacoes:
            pesquisa=int(input("Digite o numero do seu Protocolo: "))
            print()
            if pesquisa <=0 or pesquisa > tamanhoManifestacoes:
                print("Protocolo não encontrado!")
                print()
                break
        for listapesquisa in manifestacoes:
            listaquebrada = listapesquisa.split("-")
            if int(listaquebrada[0]) == (pesquisa):
                print("codigo", end="")
                for proto in listaquebrada:
                    print("- " + proto, end=" ")
                print()

print("Programa encerrado")