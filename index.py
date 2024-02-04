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

# Exemplo para Base 1
base_1 = gerar_base_clientes(5)
imprimir_base_clientes(base_1)
populacao_1 = criar_populacao(10, base_1)
melhor_rota_1, satisfacao_total_1, tempo_total_entregas_1 = algoritmo_genetico(populacao_1, 10000, base_1)

# Exemplo para Base 2
base_2 = gerar_base_clientes(10)
imprimir_base_clientes(base_2)
populacao_2 = criar_populacao(10, base_2)
melhor_rota_2, satisfacao_total_2, tempo_total_entregas_2 = algoritmo_genetico(populacao_2, 10000, base_2)

# Exemplo para Base 3
base_3 = gerar_base_clientes(30)
imprimir_base_clientes(base_3)
populacao_3 = criar_populacao(10, base_3)
melhor_rota_3, satisfacao_total_3, tempo_total_entregas_3 = algoritmo_genetico(populacao_3, 10000, base_3)

# Parâmetros do Algoritmo Genético
max_geracao = 10000

# Execução do Algoritmo Genético
# Base 1 com 5 clientes
base_1 = gerar_base_clientes(5)
populacao_1 = criar_populacao(10, base_1)
melhor_rota_1, satisfacao_total_1, tempo_total_entregas_1 = algoritmo_genetico(populacao_1, max_geracao, base_1)

# Simulação de Entregas e Análise Adicional:
clients_1 = [cliente['qtd_pedidos'] for cliente in base_1]
order_delivery_1 = melhor_rota_1  # Melhor rota da Base 1
capacity = 4
no_served = []
move_useless = 0
duplicate_served = 0
duplicate_client = []
served = []
satisfacao_total_clientes = []

# Para garantir que a simulação use a base correta
base_clientes = base_1

for i in range(0, len(order_delivery_1)):
    if order_delivery_1[i] == 0:
        if capacity == 4:
            move_useless += 1
        capacity = 4
    if capacity >= clients_1[order_delivery_1[i]]:
        capacity -= clients_1[order_delivery_1[i]]
        if order_delivery_1[i] != 0 and order_delivery_1[i] in served:
            duplicate_served += 1
            duplicate_client.append(order_delivery_1[i])

        served.append(order_delivery_1[i])
        satisfacao_total_clientes.append(calcular_satisfacao(base_clientes[order_delivery_1[i-1]], base_clientes[order_delivery_1[i]]))
    else:
        no_served.append(order_delivery_1[i])


print(f"\nMelhor rota Base 1: {melhor_rota_1}")
print(f"Distância da melhor rota Base 1: {round(fitness(melhor_rota_1, base_1), 1)}")
print(f"Satisfação total da melhor rota Base 1: {round(satisfacao_total_1, 1)}")
print(f"Tempo total das entregas Base 1: {round(tempo_total_entregas_1, 1)} segundos")
print(f"Clientes não atendidos Base 1 ({len(no_served)}): {no_served}")
print(f"Quantidade de movimentos desnecessários Base 1: {move_useless}")
print(f"Clientes atendidos em duplicidade Base 1 ({duplicate_served}): {duplicate_client}")
print(f"Satisfação total dos clientes atendidos Base 1: {round(sum(satisfacao_total_clientes), 1)}")

print(f"\nMelhor rota Base 2: {melhor_rota_2}")
print(f"Distância da melhor rota Base 2: {round(fitness(melhor_rota_2, base_2), 1)}")
print(f"Satisfação total da melhor rota Base 2: {round(satisfacao_total_2, 1)}")
print(f"Tempo total das entregas Base 2: {round(tempo_total_entregas_2, 1)} segundos")
print(f"Clientes não atendidos Base 2 ({len(no_served)}): {no_served}")
print(f"Quantidade de movimentos desnecessários Base 2: {move_useless}")
print(f"Clientes atendidos em duplicidade Base 2 ({duplicate_served}): {duplicate_client}")
print(f"Satisfação total dos clientes atendidos Base 2: {round(sum(satisfacao_total_clientes), 1)}")

print(f"\nMelhor rota Base 3: {melhor_rota_3}")
print(f"Distância da melhor rota Base 3: {round(fitness(melhor_rota_3, base_3), 1)}")
print(f"Satisfação total da melhor rota Base 3: {round(satisfacao_total_3, 1)}")
print(f"Tempo total das entregas Base 3: {round(tempo_total_entregas_3, 1)} segundos")
print(f"Clientes não atendidos Base 3 ({len(no_served)}): {no_served}")
print(f"Quantidade de movimentos desnecessários Base 3: {move_useless}")
print(f"Clientes atendidos em duplicidade Base 3 ({duplicate_served}): {duplicate_client}")
print(f"Satisfação total dos clientes atendidos Base 3: {round(sum(satisfacao_total_clientes), 1)}")
