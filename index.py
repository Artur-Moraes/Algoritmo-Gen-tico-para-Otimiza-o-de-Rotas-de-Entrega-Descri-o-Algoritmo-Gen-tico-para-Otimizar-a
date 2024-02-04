import random
import time

def gerar_base_clientes(qnt_clientes):
    base_clientes = []
    for i in range(qnt_clientes):
        qtd_pedidos = random.randint(1, 4)
        cliente = {
            'nome': f'Cliente_{i + 1}',
            'posicao_x': random.randint(0, 50),
            'posicao_y': random.randint(0, 50),
            'qtd_pedidos': qtd_pedidos
        }
        base_clientes.append(cliente)
    return base_clientes

def imprimir_base_clientes(base_clientes):
    for cliente in base_clientes:
        print(f"Cliente: {cliente['nome']} - Posição: ({cliente['posicao_x']}, {cliente['posicao_y']}) - Qtd. Pedidos: {cliente['qtd_pedidos']}")

def criar_individuo(base_clientes):
    return random.sample(range(len(base_clientes)), len(base_clientes))

def criar_populacao(tamanho_populacao, base_clientes):
    return [criar_individuo(base_clientes) for _ in range(tamanho_populacao)]

def calcular_distancia(cliente1, cliente2):
    x1, y1 = cliente1['posicao_x'], cliente1['posicao_y']
    x2, y2 = cliente2['posicao_x'], cliente2['posicao_y']

    distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distancia

def calcular_satisfacao(cliente1, cliente2):
    x1, y1 = cliente1['posicao_x'], cliente1['posicao_y']
    x2, y2 = cliente2['posicao_x'], cliente2['posicao_y']

    distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    satisfacao = 1.0 / distancia if distancia != 0 else 0.0  # Evita divisão por zero

    return satisfacao

def calcular_tempo_entrega(rota, base_clientes):
    velocidade_media = 30.0  # Exemplo de velocidade média em km/h
    tempo_total = 0.0

    for i in range(len(rota) - 1):
        cliente_atual = base_clientes[rota[i]]
        proximo_cliente = base_clientes[rota[i + 1]]

        distancia = calcular_distancia(cliente_atual, proximo_cliente)
        tempo_entrega = distancia / velocidade_media
        tempo_total += tempo_entrega

    primeiro_cliente = base_clientes[rota[0]]
    ultimo_cliente = base_clientes[rota[-1]]
    tempo_total += calcular_distancia(ultimo_cliente, primeiro_cliente) / velocidade_media

    return tempo_total

def calcular_distancia_total(rota, base_clientes):
    distancia_total = 0.0

    for i in range(len(rota) - 1):
        cliente_atual = base_clientes[rota[i]]
        proximo_cliente = base_clientes[rota[i + 1]]

        distancia = calcular_distancia(cliente_atual, proximo_cliente)
        distancia_total += distancia

    primeiro_cliente = base_clientes[rota[0]]
    ultimo_cliente = base_clientes[rota[-1]]
    distancia_total += calcular_distancia(ultimo_cliente, primeiro_cliente)

    return distancia_total

def fitness(rota, base_clientes):
    return calcular_distancia_total(rota, base_clientes)

def crossover(pai1, pai2):
    ponto_corte = random.randint(1, min(len(pai1), len(pai2)) - 1)

    filho1 = pai1[:ponto_corte] + pai2[ponto_corte:]
    filho2 = pai2[:ponto_corte] + pai1[ponto_corte:]

    return filho1, filho2

def mutacao(individuo):
    indice1, indice2 = random.sample(range(len(individuo)), 2)
    individuo[indice1], individuo[indice2] = individuo[indice2], individuo[indice1]

def selecionarMelhores(populacao, base_clientes):
    return sorted(populacao, key=lambda x: fitness(x, base_clientes))

def calcSatisfacao(rota, base_clientes):
    satisfacao_total = 0.0

    for i in range(len(rota) - 1):
        cliente_atual = base_clientes[rota[i]]
        proximo_cliente = base_clientes[rota[i + 1]]

        satisfacao_cliente = calcular_satisfacao(cliente_atual, proximo_cliente)
        satisfacao_total += satisfacao_cliente

    primeiro_cliente = base_clientes[rota[0]]
    ultimo_cliente = base_clientes[rota[-1]]
    satisfacao_total += calcular_satisfacao(ultimo_cliente, primeiro_cliente)

    return satisfacao_total

def algoritmo_genetico(populacao_inicial, geracoes, base_clientes):
    num_filhos_gerados = 20
    taxa_mutacao = 0.2

    inicio_tempo_entregas = time.time()

    for geracao in range(geracoes):
        fitness = lambda rota: calcular_distancia_total(rota, base_clientes)
        populacao = sorted(populacao_inicial, key=fitness)
        pais = selecionarMelhores(populacao, base_clientes)[:num_filhos_gerados]

        filhos = []
        for i in range(0, len(pais), 2):
            pai1, pai2 = random.sample(pais, 2)
            filho1, filho2 = crossover(pai1, pai2)

            if random.random() < taxa_mutacao:
                mutacao(filho1)
            if random.random() < taxa_mutacao:
                mutacao(filho2)

            filhos.extend([filho1, filho2])

        populacao_inicial = pais + filhos

    fim_tempo_entregas = time.time()
    tempo_total_entregas = fim_tempo_entregas - inicio_tempo_entregas

    melhor_rota = min(populacao_inicial, key=fitness)
    satisfacao_total = calcSatisfacao(melhor_rota, base_clientes)

    return melhor_rota, satisfacao_total, tempo_total_entregas

# Geração de Bases de Clientes
base_clientes = gerar_base_clientes(50)

# Criação da População Inicial
populacao = criar_populacao(10, base_clientes)

# Parâmetros do Algoritmo Genético
max_geracao = 10000

# Execução do Algoritmo Genético
melhor_rota, satisfacao_total, tempo_total_entregas = algoritmo_genetico(populacao, max_geracao, base_clientes)

# Simulação de Entregas e Análise Adicional:

clients = [0, 4, 1, 3, 2, 4, 2, 3, 1, 4, 3, 1, 4, 3, 2, 4, 2, 3, 1, 3, 4, 1, 4, 3, 1, 2, 3, 1, 1, 1, 1]
order_delivery = [0, 28, 7, 0, 27, 0, 8, 30, 0, 2, 10, 0, 27, 0, 13, 0, 2, 10, 0, 23, 7, 0, 8, 3, 0, 15, 0, 28, 14, 21, 8, 0, 9, 0, 28, 11, 0, 14, 28, 0, 29, 18, 0, 12]
capacity = 4
no_served = []
move_useless = 0
duplicate_served = 0
duplicate_client = []
served = []
satisfacao_total_clientes = []

for i in range(0, len(order_delivery)):
    if order_delivery[i] == 0:
        if capacity == 4:
            move_useless += 1
        capacity = 4
    if capacity >= clients[order_delivery[i]]:
        capacity -= clients[order_delivery[i]]
        if order_delivery[i] != 0 and order_delivery[i] in served:
            duplicate_served += 1
            duplicate_client.append(order_delivery[i])

        served.append(order_delivery[i])
        satisfacao_total_clientes.append(calcular_satisfacao(base_clientes[order_delivery[i-1]], base_clientes[order_delivery[i]]))
    else:
        no_served.append(order_delivery[i])


print(f"\nMelhor rota: {melhor_rota}")
print(f"Distância da melhor rota: {round(fitness(melhor_rota, base_clientes), 1)}")
print(f"Satisfação total da melhor rota: {round(satisfacao_total, 1)}")
print(f"Tempo total das entregas: {round(tempo_total_entregas, 1)} segundos")
print(f"Clientes não atendidos ({len(no_served)}): {no_served}")
print(f"Quantidade de movimentos desnecessários: {move_useless}")
print(f"Clientes atendidos em duplicidade ({duplicate_served}): {duplicate_client}")
print(f"Satisfação total dos clientes atendidos: {round(sum(satisfacao_total_clientes), 1)}")
