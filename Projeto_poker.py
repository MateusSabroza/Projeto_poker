#Baralho inicial 
Baralho = ("A","7","K","Q","J","A","7","K","Q","J","A","7","K","Q","J","A","7","K","Q","J","A","7","K","Q","J")
#         |          1        |         2         |        3         |   4               |           5       | 
 
"""
Criei uma tupla para ter um valor constante do baralho original tendo 5 copias das cartas (A,7,K,Q,J)

"""

def valor_da_mao(lista):
    """
    Função que recebe uma mão e retorna seu valor em pontos.
    Valores:
         Um par -> 1 ponto          |  Dois pares -> 2 pontos | Uma tripla -> 3 pontos
    Uma tripla e um par -> 5 pontos | Uma quadra -> 10 pontos | Um quina -> 50 pontos
    >>> valor_da_mao(["A","A","K","J","7"])
    1
    """
    pontos = {
    (1,1,1,1,1): 0, #Nada
    (1,1,1,2): 1 ,  #Um par
    (1,2,2): 2 ,    #Dois pares  
    (1,1,3): 3 ,    #Uma tripla
    (2,3): 5 ,      #Uma tripla e um par
    (1,4): 10 ,     #Uma quadra 
    (5,): 50 ,      #Uma quina
    }
    cartas_unicas_na_mao = set(lista)
    combinacoes_na_mao = list()
    for carta in cartas_unicas_na_mao:
        combinacoes_na_mao.append(lista.count(carta))
    combinacoes_na_mao.sort()
    chave_combinacao = tuple(combinacoes_na_mao)
    return pontos[chave_combinacao]

def pontos_da_rodada(lista1,lista2):
    """
    Função recebe uma mão de cada jogador,e retorna uma tupla com a pontuação de cada 
    jogador de acordo com as regras abaixo:
    Aquele que tiver a mão com mais pontos ganha a rodada e recebe os pontos correspondentes,
    o outro jogador não faz nenhum ponto. Em caso de empate, ambos jogadores ganham metade dos pontos.

    >>> pontos_da_rodada(["A","A","K","A","7"],["A","A","K","J","7"])
    (3, 0)
    >>> pontos_da_rodada(["A","A","K","J","7"],["A","A","K","J","7"])
    (0.5, 0.5)
    >>> pontos_da_rodada(["A","A","K","J","7"],["A","A","A","J","7"])
    (0, 3)

    """
    pontos_jogador1 = valor_da_mao(lista1)
    pontos_jogador2 = valor_da_mao(lista2)

    if pontos_jogador1 > pontos_jogador2:
        return (pontos_jogador1, 0)
    elif pontos_jogador1 == pontos_jogador2:
        return (pontos_jogador1/2, pontos_jogador2/2)
    else:
        return (0, pontos_jogador2)



def nao_contribuintes(lista):
    """
    Recebe uma mão(lista) e retorna uma lista com as cartas que não contribuem para pontos.

    """

    cartas_unicas_na_mao = set(lista)
    nao_contribuintes = []
    for carta in cartas_unicas_na_mao:
        if lista.count(carta) == 1 :
            nao_contribuintes += [carta]
    return nao_contribuintes
        














if __name__=="__main__":
    import doctest
    doctest.testmod()

    