import matplotlib.pyplot as plt

#muda aqui, coloca sua base de dados
# Base de dados dos clientes
clclientes_5 = {
    0: {'posicao': [0, 0]},  # Sede da empresa
    1: {'posicao': [1, 13], 'pedido': 4},
    2: {'posicao': [30, 4], 'pedido': 1},
    3: {'posicao': [10, 0], 'pedido': 3},
    4: {'posicao': [15, 20], 'pedido': 2},
}

# Extrair coordenadas dos clientes
coordenadas = [cliente['posicao'] for cliente in clclientes_5.values()]

# Plotar o mapa
plt.figure(figsize=(8, 8))
plt.scatter(*zip(*coordenadas), marker='o', color='blue', label='Clientes')

# Adicionar rótulos para os clientes
for cliente_id, dados in clclientes_5.items():
    plt.text(*dados['posicao'], f'Cliente {cliente_id}', fontsize=8, ha='right')

# Adicionar rótulo para a sede da empresa
plt.text(0, 0, 'Sede da Empresa', fontsize=8, ha='right')

# Configurações adicionais
plt.title('Mapa dos Clientes')
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.legend()
plt.grid(True)

# Exibir o mapa
plt.show()