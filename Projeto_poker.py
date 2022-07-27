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
    >>> nao_contribuintes(["A","A","K","J","7"])
    ['7', 'J', 'K']
    >>> nao_contribuintes(["A","A","K","A","7"])
    ['7', 'K']
    >>> nao_contribuintes(["A","7","K","Q","J"])
    ['7', 'A', 'J', 'K', 'Q']
    """

    cartas_unicas_na_mao = set(lista)
    nao_contribuintes = []
    for carta in cartas_unicas_na_mao:
        if lista.count(carta) == 1 :
            nao_contribuintes += [carta]
    return sorted(nao_contribuintes)     # como conjuntos não possuem ordem, a lista poderia vir escrita de maneira diferente, então estamos ordenando para o doctest funcionar.
        

def nao_contribuintes_ate_3(lista):
    """
    retorna 3 cartas que não contribuem para pontos
    
    >>> nao_contribuintes_ate_3(["A","A","K","J","7"])
    ['7', 'J', 'K']
    >>> nao_contribuintes_ate_3(["A","A","K","A","7"])
    ['7', 'K']
    >>> nao_contribuintes_ate_3(["A","7","K","Q","J"])
    ['7', 'A', 'J']
    """
    nao_contribuinte = nao_contribuintes(lista)
    if len(nao_contribuinte) <= 3 :
        return nao_contribuinte
    else :
        return [nao_contribuinte[0],nao_contribuinte[1],nao_contribuinte[2]] 
#Importando intertools
from itertools import combinations
    
def possiblidades(mao_parcial, num_cartas, cartas_restantes):
    """Gerador de combinações da mão parcial(5-num_cartas cartas) com  num_cartas das cartas_restantes"""
    lista=list()
    for combinacao in combinations(cartas_restantes, num_cartas):#esse for percorre cada elemento de uma lista de combinacoes
        l=mao_parcial[:]#cria uma copia da mão parcial
        l+=combinacao#junta o elemento da lista de combinacoes com a copia da lista das cartas da mão
        lista.append([l])# cria uma lista de todas as combinacoes possiveis com a mão       
    return (x for x in lista) #retorna um gerador da lista


# 2 b )
def vale_apena_trocar(mao, mao_parcial):
    """
    mao sao todas as cartas que vc tem, mao_parcial sao as cartas que vc não vai trocar
    """
    continuar = True
    Baralho = ["A","7","K","Q","J","A","7","K","Q","J","A","7","K","Q","J","A","7","K","Q","J","A","7","K","Q","J"]
    vale_apena = 0
    nao_vale_apena = 0
    
    #até aqui apenas defini alguns parametros 

    for elemento in mao:
        Baralho.remove(elemento)
    cartas_restantes = Baralho  #aqui apenas tirei asd cartas que estão na minha mão do braralho
    possiveis_maos = possiblidades(mao_parcial, 5- len(mao_parcial) , cartas_restantes) #criando um gerador das possibilidades de maos usando a função feita anteriormente

    while continuar == True:
        #quando o gerador ficar vazio dara um erro, usaremos isso para finalizar nossa função.
        try:
            uma_possibilidade = next(possiveis_maos) #isso retorana uma lista de lista sendo  a lista de dentro a mao
        except:
            if vale_apena > nao_vale_apena:
                return print(f'vale apena {vale_apena,nao_vale_apena}')
            elif vale_apena < nao_vale_apena:
                return print(f'nao vale apena {vale_apena,nao_vale_apena}')
            else:
                print(f'tanto faz {vale_apena,nao_vale_apena}')
        
        if valor_da_mao(uma_possibilidade[0]) > valor_da_mao(mao):
            vale_apena += 1
        else:
            nao_vale_apena += 1

#resultado : uma dupla  vale apena (836, 304) 
#            uma trinca nao vale apena (69, 121)
#            uma quadra nao vale apena (1, 19)

# 2 c )
# trocando duas: vale apena (134, 56)
# trocando uma: vale apena (11, 9)

def valor_médio_troca(mao, trocas):
    """
    retorna o valor da media das possibilidades de maos 
    """
    
    continuar = True
    Baralho = ["A","7","K","Q","J","A","7","K","Q","J","A","7","K","Q","J","A","7","K","Q","J","A","7","K","Q","J"]
    valores_apos_troca = []
    mao_parcial = mao #fazendo uma copia
    
    
    for elemento in trocas:
        mao_parcial.remove(elemento)
    
    for elemento in mao:
        Baralho.remove(elemento)
    cartas_restantes = Baralho # tirando as cartas que tenho na mao do baralho

    possiveis_maos = possiblidades(mao_parcial, 5- len(mao_parcial) , cartas_restantes)

    while continuar == True:
        try:
            uma_possibilidade = next(possiveis_maos)
        except:
           return sum(valores_apos_troca)/len(valores_apos_troca)        
        
        valores_apos_troca += [valor_da_mao(uma_possibilidade[0])]

        


if __name__=="__main__":
    import doctest
    doctest.testmod()