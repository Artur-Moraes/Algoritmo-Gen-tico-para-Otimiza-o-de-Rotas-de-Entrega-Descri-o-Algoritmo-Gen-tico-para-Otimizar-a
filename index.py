import random
import math

cargaAtual = 4

def gerar_base_clientes(qnt_clientes):
    base_clientes = []
    for i in range(qnt_clientes):
        qtd_pedidos = random.randint(1, 4)
        cliente = {
            'nome': f'Cliente_{i+1}',
            'posicao_x': random.randint(0, 50),
            'posicao_y': random.randint(0, 50),  
            'qtd_pedidos': qtd_pedidos  
        }
        base_clientes.append(cliente)
    return base_clientes

def imprimir_base_clientes(base_clientes):
    for cliente in base_clientes:
        print(f"Cliente: {cliente['nome']} - Posição: ({cliente['posicao_x']}, {cliente['posicao_y']}) - Qtd. Pedidos: {cliente['qtd_pedidos']}")

base_1 = gerar_base_clientes(5)
base_2 = gerar_base_clientes(10)
base_3 = gerar_base_clientes(30)

print("Base 1:")
imprimir_base_clientes(base_1)

print("\nBase 2:")
imprimir_base_clientes(base_2)

print("\nBase 3:")
imprimir_base_clientes(base_3)


def criar_individuo(base_clientes):
    return random.sample(range(len(base_clientes)), len(base_clientes))

def criar_populacao(tamanho_populacao, base_clientes):
    return [criar_individuo(base_clientes) for _ in range(tamanho_populacao)]

def calcular_distancia(cliente1, cliente2):
    x1, y1 = cliente1['posicao_x'], cliente1['posicao_y']
    x2, y2 = cliente2['posicao_x'], cliente2['posicao_y']

    distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distancia

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

base_clientes = gerar_base_clientes(50)
populacao = criar_populacao(10, base_clientes)

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

maxGeracao = 10000
atualGeracao = 0

while atualGeracao < maxGeracao:
    populacao = selecionarMelhores(populacao, base_clientes)
    melhoresIndividuos = populacao[:2]

    nova_populacao = melhoresIndividuos.copy()

    for _ in range(4):
        pai1, pai2 = random.sample(melhoresIndividuos, 2)
        filho1, filho2 = crossover(pai1, pai2)
        
        if random.random() < 0.1:  
            mutacao(filho1)
        if random.random() < 0.1:
            mutacao(filho2)

        nova_populacao.extend([filho1, filho2])

    populacao = nova_populacao
    atualGeracao += 1

melhor_rota = selecionarMelhores(populacao, base_clientes)[0]
distancia_melhor_rota = calcular_distancia_total(melhor_rota, base_clientes)

print("Melhor rota:", melhor_rota)
print("Distância da melhor rota:", round(distancia_melhor_rota))
