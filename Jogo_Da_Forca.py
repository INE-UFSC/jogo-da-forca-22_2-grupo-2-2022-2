import random


# A progressão das falhas
forca = [
    ''' 
     ______
    |      |
    |     
    |      
    |      
    |      
    |
    |
   _|_
    ''',
    ''' 
     ______
    |      |
    |     ( )
    |      
    |      
    |      
    |
    |
   _|_
    ''',
    ''' 
     ______
    |      |
    |     ( )
    |      |
    |      |
    |      |
    |
    |
   _|_
    ''',
    ''' 
     ______
    |      |
    |     ( )
    |    __|
    |      |
    |      |
    |
    |
   _|_
    ''',
    ''' 
     ______
    |      |
    |     ( )
    |    __|__
    |      |
    |      |
    |
    |
   _|_
    ''',
    ''' 
     ______
    |      |
    |     ( )
    |    __|__
    |      |
    |      |
    |     /
    |    /
   _|_
    ''',
    ''' 
     ______
    |      |
    |     ( )
    |    __|__
    |      |
    |      |
    |     / \\
    |    /   \\
   _|_
    ''',
    ''' 
     ______
    |      |
    |    (* *)
    |    __|__
    |      |
    |      |
    |     / \\
    |    /   \\
   _|_
    ''',
    '''
    ---GAME OVER---
    '''
    ]
lista_palavras = ['amarelo', 'amiga', 'amor', 'ave', 'bolo', 'branco', 'cama', 'caneca', 'celular', 'clube', 'copo', 'doce', 'elefante', 'escola', 'estojo', 'faca', 'foto', 'garfo', 'geleia', 'girafa', 'janela', 'limonada', 'meia', 'noite', 'ovo', 'pai', 'parque', 'passarinho', 'peixe', 'pijama', 'rato', 'umbigo']

n = random.randint(0,31)
palavra = lista_palavras[n]
palavra = palavra.lower()
status = list(palavra)
c = len(palavra)
chance = 0
saida = ['_']*c
# estabelecendo o critério para mais de uma palavra
while ' ' in status:
    l = status.index(' ')
    saida[l] = ' '
    status[l] = '*'
# transformando em string e printando o template vazio 
r = ''.join(saida)
print(forca[0])
print(r)
# critérios para continuar o jogo
while (r != palavra) and (chance < 8):
    letra = input()
    letra = letra.lower()
    if letra in palavra:
        # após verificar quantas vezes a letra aparece, substituir '_' pela letra
        while letra in status:
            l = status.index(letra)
            saida[l] = letra
            status[l] = '*'
    else: 
        chance += 1
    # atualizar o template com a última tentativa
    print(forca[chance])
    r = ''.join(saida)
    if chance < 8: print(r)