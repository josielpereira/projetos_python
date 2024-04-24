livros = []

def abre_arquivo(nome_arquivo):
    f = open(nome_arquivo,'r',encoding="utf-8")
    return f
def escrever_arquivo(nome_arquivo, valor):
    f = open(nome_arquivo,'a',encoding="utf-8")
    f.write(valor + "\n")
    f.close

def preenche_lista(f):
    if(livros):
        livros.clear()

    for livro in f:
        livro = livro.strip()
        livros.append(livro)
    
def exibe_livros():
    i = 1
    for livro in livros:
        print("*",i, livro)
        i+=1

def definir(nome_arquivo):
    f = abre_arquivo(nome_arquivo)
    preenche_lista(f)
    exibe_livros()

def main():
    print("Livros lidos:")
    definir("livros_lidos.txt")
    
    print("Livros lendo:")
    definir("livros_lendo.txt")
    
    print("Quero ler:")
    definir("livros_quero_ler.txt")

    resposta = int(input("Gostaria de adicionar novos livros?  \n 1 - Livros lidos \n 2 - Livros lendo \n 3 - Livros Quero ler \n"))
    livro = input("Digite o nome do livro: ")

    if(resposta == 1):
        escrever_arquivo("livros_lidos.txt",livro)
        definir("livros_lidos.txt")
    elif(resposta == 2):
        escrever_arquivo("livros_lendo.txt",livro)
        definir("livros_lendo.txt")
    elif(resposta == 3): 
        escrever_arquivo("livros_quero_ler.txt",livro)
        definir("livros_quero_ler.txt")
    
main()