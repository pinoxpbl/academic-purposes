def valida_dado(pergunta,min):
    while True:
        x = input(pergunta)
        if(len(x) > min):
            break
        else:
            print("Um nome é necessário para se confirmar")
            continue

    return x.title()

def valida_int(pergunta,min,max):
    while True:
        try:
            x = int(input(pergunta))
            if(x < min or x > max):
                continue
            else:
                break
        except ValueError:
            print("Apenas números inteiros são aceitos")
    return x

def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, "wt+")
        a.close()
    except:
        print("Erro na criação do arquivo")
    else:
        print("Arquivo criado com sucesso")

def cadastrar(nomeArquivo, dicionarioJogo):
    try:
        a = open(nomeArquivo,"at")
    except:
        print("Erro ao abrir o arquivo")
    else:
        a.write("{}\n".format(dicionarioJogo))
    finally:
        a.close()

def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, "rt")
    except:
        print("Erro ao abrir o arquivo")
    else:
        print(a.read())
    finally:
        a.close()

# Programa principal
games = {}
arquivo = "games.txt"
if(existeArquivo(arquivo)):
    print("Arquivo localizado no computador")
else:
    print("Arquivo inexistente")
    criaArquivo(arquivo)

while True:
    print("MENU")
    print("1 - Cadastrar itens")
    print("2 - Listar itens")
    print("3 - Sair")

    menu = valida_int("O que deseja fazer?: ",1,3)

    if(menu == 1):
        print("Cadastrando itens...")
        games["Nome"] = valida_dado("Nome do jogo: ",1)
        games["Videogame"] = valida_dado("Nome do videogame: ",1)
        games["Ano"] = valida_int("Ano do lançamento: ",1960,2022)
        cadastrar(arquivo,games)
    elif(menu == 2):
        print("Listando os itens...")
        listarArquivo(arquivo)
    elif(menu == 3):
        print("Encerrando o programa...")
        break
