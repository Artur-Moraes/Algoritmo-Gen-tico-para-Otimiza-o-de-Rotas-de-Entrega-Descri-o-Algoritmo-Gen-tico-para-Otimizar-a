
posicoes = [[10, 0], [1, 13], [30, 4]]
distancias = [((pos[0] - posicoes[0][0])**2 + (pos[1] - posicoes[0][1])**2)**0.5 for pos in posicoes[1:]]
tempoTolerancia = [int(distancia * 1.5) for distancia in distancias]

for i, distancia in enumerate(distancias):
    print(f"Distância do cliente {i + 1} para a sede: {round(distancia)} unidades")
    print(f"Tempo de tolerância do cliente {i + 1}: {round(tempoTolerancia[i])} minutos")

pedido = [[1, 4], [3, 3], [2, 1]]
informacaoPedido = [{'cliente': p[0], 'quantidade de água': p[1]} for p in pedido]

for info in informacaoPedido:
    print(f"Cliente {info['cliente']} pediu {info['quantidade de água']} galões de água.")

"""

----------------------------------------------------------------------------------------
                Parte para Calcular a satisfação do cliente
----------------------------------------------------------------------------------------

"""

def getSa7sfacao(posicaoCliente, tempoEntrega):
    
    indiceCliente = -1
    for i, posicao in enumerate(posicoes):
        if posicao == posicaoCliente:
            indiceCliente = i
            break
    
    if indiceCliente == -1:
        return "Cliente não encontrado"
    
    tempo_tolerancia = tempoTolerancia[indiceCliente - 1] if indiceCliente > 0 else 0
    
    if tempoEntrega == tempo_tolerancia:
        return 6
    elif tempoEntrega < tempo_tolerancia / 2:
        return 10
    elif tempoEntrega < tempo_tolerancia:
        return 8
    elif tempoEntrega <= tempo_tolerancia * 1.1:
        return 5
    elif tempoEntrega <= tempo_tolerancia * 1.2:
        return 4
    elif tempoEntrega <= tempo_tolerancia * 1.4:
        return 3
    elif tempoEntrega <= tempo_tolerancia * 1.6:
        return 2
    elif tempoEntrega <= tempo_tolerancia * 1.8:
        return 1
    else:
        return 0


"""

----------------------------------------------------------------------------------------
                Parte para mostra satisfação com tempo de entrega
----------------------------------------------------------------------------------------

"""

#Teste para unitário de cliente com o tempo de entrega 
posicaoCliente = posicoes[1]
tempoEntrega = 15
satisfacaoCliente = getSa7sfacao(posicaoCliente, tempoEntrega)
print(f"A satisfação do cliente com o tempo de entrega de {tempoEntrega} minutos é: {satisfacaoCliente}")
#--------------------------------------------------------------------------------------------------------

for i, posicaoCliente in enumerate(posicoes[1:], start=1):
    tempoEntrega = tempoTolerancia[i - 1]  
    satisfacaoCliente = getSa7sfacao(posicaoCliente, tempoEntrega)
    print(f"A satisfação do cliente {i} com o tempo de entrega de {tempoEntrega} minutos é: {satisfacaoCliente}")

