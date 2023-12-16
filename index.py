
posicoes = [[10, 0], [1, 13], [30, 4]]
distancias = [((pos[0] - posicoes[0][0])**2 + (pos[1] - posicoes[0][1])**2)**0.5 for pos in posicoes[1:]]
tempoTolerancia = [int(distancia * 1.5) for distancia in distancias]

for i, distancia in enumerate(distancias):
    print(f"Distância do cliente {i + 1} para a sede: {distancia} unidades")
    print(f"Tempo de tolerância do cliente {i + 1}: {tempoTolerancia[i]} minutos")


pedido = [[1, 4], [3, 3], [2, 1]]
informacaoPedido = [{'cliente': p[0], 'quantidade_agua': p[1]} for p in pedido]

for info in informacaoPedido:
    print(f"Cliente {info['cliente']} pediu {info['quantidade_agua']} galões de água.")
