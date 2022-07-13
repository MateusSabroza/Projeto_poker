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
    "Nada": 0,
    "Um par" : 1 ,
    "Dois pares": 2 ,  
    "Uma tripla": 3 ,
    "Uma tripla e um par": 5 , 
    "Uma quadra": 10 pontos , 
    "Um quina": 50 pontos ,
    }
    lista2=set(lista)
    lista3=list()
    for x in lista2:
        if lista.count(x)>1:
            lista3.append(lista.count(x))
        
            
                
                
    