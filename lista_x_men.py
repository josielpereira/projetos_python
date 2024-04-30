# Lista de X-Men
x_men = ["Professor X", "Wolverine", "Cyclope", "Tempestade", "Jean Grey", "Fera", "Noturno", "Colossus", "Gambit"]

# Função para encontrar X-Men com nomes começando com uma letra específicada 
def find_xmen_with_letter(letter):
    xmen_with_letter = [] 
    for x_man in x_men:
        if x_man.startswith(letter):
            xmen_with_letter.append(x_man)
    return xmen_with_letter

# Função para contar o número de X-Men
def count_xmen():
    return len(x_men)

# Função para exibir os X-Men em ordem alfabética
def display_xmen_alphabetically():
    sorted_xmen = sorted(x_men)
    for xman in sorted_xmen:
        print(xman)

# Exemplo de uso das funções
print("X-Men cujos nomes começam com 'C':", find_xmen_with_letter('C'))
print("Número total de X-Men:", count_xmen())
print("Lista de X-Men em ordem alfabética:")
display_xmen_alphabetically()
