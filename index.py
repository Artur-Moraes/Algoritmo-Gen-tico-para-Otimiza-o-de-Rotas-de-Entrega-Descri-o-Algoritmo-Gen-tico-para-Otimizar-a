def getDistancia(x1, y1, x2, y2):
    distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return distancia

def calcSatisfacao(arr_ordem):
    tempo_atual = 0
    carga_atual = 4  
    satisfacao_total = 0

    for i in range(len(arr_ordem) - 1):
        cliente_atual = arr_ordem[i]
        proximo_cliente = arr_ordem[i + 1]

        distancia = getDistancia(*posicoes[cliente_atual], *posicoes[proximo_cliente])
        tempo_entrega = distancia * 0.5  
        tempo_atual += tempo_entrega

        tempo_tolerancia = distancia * 0.75  #

        if tempo_atual <= tempo_tolerancia:
            satisfacao_total += 6
        elif tempo_atual < tempo_tolerancia * 1.5:  
            satisfacao_total += 8
        else:  
            atraso_percentual = (tempo_atual - tempo_tolerancia) / tempo_tolerancia * 100
            if atraso_percentual <= 100:
                if atraso_percentual <= 10:
                    satisfacao_total += 5
                elif atraso_percentual <= 20:
                    satisfacao_total += 4
                elif atraso_percentual <= 40:
                    satisfacao_total += 3
                elif atraso_percentual <= 60:
                    satisfacao_total += 2
                elif atraso_percentual <= 80:
                    satisfacao_total += 1
                else:
                    satisfacao_total += 0


        if proximo_cliente == 0:  
            carga_atual = 4  
        else:
            carga_atual -= arr_pedido[proximo_cliente - 1][1]  

        
        if arr_pedido[proximo_cliente - 1][1] > carga_atual:
            satisfacao_total -= 1  

    return satisfacao_total

ordem_entrega = [0, 1, 2, 0]  
satisfacao = calcSatisfacao(ordem_entrega)
print(satisfacao)  



def avaliacaoRota(lista_clientes):
    tempo_total = 0

    for i in range(len(lista_clientes) - 1):
        cliente_atual = lista_clientes[i]
        proximo_cliente = lista_clientes[i + 1]

        x = getDistancia(*posicoes[cliente_atual], *posicoes[0]) 
        y = getDistancia(*posicoes[cliente_atual], *posicoes[proximo_cliente])  

        tempo_total += x + y

    return tempo_total

clientes_rota = [0, 1, 2]  
avaliacao = avaliacaoRota(clientes_rota)
print(avaliacao)  

base_1 = [
    {"nome": "Cliente 1", "x": 10, "y": 0, "quantidade_pedidos": 3},
    {"nome": "Cliente 2", "x": 1, "y": 13, "quantidade_pedidos": 2},
    {"nome": "Cliente 3", "x": 30, "y": 4, "quantidade_pedidos": 1},
    {"nome": "Cliente 4", "x": 20, "y": 15, "quantidade_pedidos": 4},
    {"nome": "Cliente 5", "x": 5, "y": 25, "quantidade_pedidos": 2},
]

sede_1 = {"x": 0, "y": 0}  

base_2 = [
    {"nome": "Cliente 1", "x": 10, "y": 0, "quantidade_pedidos": 3},
    {"nome": "Cliente 2", "x": 1, "y": 13, "quantidade_pedidos": 2},
    {"nome": "Cliente 3", "x": 30, "y": 4, "quantidade_pedidos": 1},
    {"nome": "Cliente 4", "x": 20, "y": 15, "quantidade_pedidos": 4},
    {"nome": "Cliente 5", "x": 5, "y": 25, "quantidade_pedidos": 2},
    {"nome": "Cliente 6", "x": 35, "y": 18, "quantidade_pedidos": 3},
    {"nome": "Cliente 7", "x": 17, "y": 8, "quantidade_pedidos": 1},
    {"nome": "Cliente 8", "x": 12, "y": 30, "quantidade_pedidos": 2},
    {"nome": "Cliente 9", "x": 28, "y": 21, "quantidade_pedidos": 5},
    {"nome": "Cliente 10", "x": 7, "y": 5, "quantidade_pedidos": 3},
]

sede = {"x": 0, "y": 0}  

base_3 = [
    {"nome": "Cliente 1", "x": 10, "y": 0, "quantidade_pedidos": 3},
    {"nome": "Cliente 2", "x": 1, "y": 13, "quantidade_pedidos": 2},
    {"nome": "Cliente 3", "x": 30, "y": 4, "quantidade_pedidos": 1},
    {"nome": "Cliente 4", "x": 20, "y": 15, "quantidade_pedidos": 4},
    {"nome": "Cliente 5", "x": 5, "y": 25, "quantidade_pedidos": 2},
    
]

sede = {"x": 0, "y": 0}  

ordem_entrega = [0, 1, 2, 0]  
satisfacao = calcSatisfacao(ordem_entrega)
print(satisfacao)  
