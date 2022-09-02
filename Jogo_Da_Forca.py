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
palavra = input()
c = len(palavra)
chance = 0
saida = ['_']*c
# estabelecendo o critério para mais de uma palavra
if ' ' in palavra:
    k = palavra.count(' ')
    for i in range(k): 
        l = palavra.index(' ', i)
        saida[l] = ' '
# transformando em string e printando o template vazio 
r = ''.join(saida)
print(forca[0])
print(r)
# critérios para continuar o jogo
while (r != palavra) and (chance < 8):
    letra = input()
    if letra in palavra:
        k = palavra.count(letra)
        # após verificar quantas vezes a letra aparece, substituir '_' pela letra
        for i in range(k):
            l = palavra.index(letra, i)
            saida[l] = letra
            r = ''.join(saida)
    else: 
        chance += 1
    # atualizar o template com a última tentativa
    print(forca[chance])
    if chance < 8: print(r)