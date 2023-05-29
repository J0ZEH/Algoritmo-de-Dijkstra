'''
Algoritmo que calcula o caminho de custo mínimo entre vértices de um grafo. Escolhido um vértice como raiz da busca, este algoritmo calcula o custo mínimo deste vértice para todos os demais vértices do grafo.
Vídeo de apresentação: https://youtu.be/ooJtGkkBFPQ
Por: José Florêncio de Melo Neto
'''

import networkx as nx

def dijkstra(graph, start_node, end_node):
    distances = {node: float('inf') for node in graph.nodes()}  # Dicionário para armazenar as distâncias dos nós ao nó de partida
    predecessors = {node: None for node in graph.nodes()}  # Dicionário para armazenar os predecessores de cada nó
    distances[start_node] = 0  # A distância do nó de partida para ele mesmo é zero
    total_distance = 0  # Variável para armazenar a distância total percorrida

    unvisited_nodes = set(graph.nodes())  # Conjunto de nós não visitados

    while unvisited_nodes:
        current_node = min(unvisited_nodes, key=lambda node: distances[node])  # Seleciona o nó não visitado com menor distância
        unvisited_nodes.remove(current_node)  # Remove o nó atual do conjunto de não visitados

        for neighbor in graph.neighbors(current_node):  # Percorre os vizinhos do nó atual
            edge_weight = graph[current_node][neighbor]['weight']  # Peso da aresta entre o nó atual e o vizinho
            distance = distances[current_node] + edge_weight  # Calcula a distância acumulada até o vizinho

            if distance < distances[neighbor]:  # Atualiza a distância se for menor do que a distância atual
                distances[neighbor] = distance  # Atualiza a distância do vizinho
                predecessors[neighbor] = current_node  # Define o predecessor do vizinho como o nó atual

            total_distance += edge_weight  # Atualiza a distância total percorrida

    path = []
    current = end_node
    while current is not None:  # Constrói o caminho mais curto do último nó até o primeiro nó
        path.insert(0, current)  # Insere o nó no início da lista (caminho mais curto é construído ao contrário)
        current = predecessors[current]  # Obtém o predecessor do nó atual

    return path, total_distance  # Retorna o caminho mais curto e a distância total percorrida

G = nx.Graph()
G.add_edge('A', 'B', weight=4)
G.add_edge('A', 'C', weight=2)
G.add_edge('B', 'C', weight=1)
G.add_edge('B', 'D', weight=5)
G.add_edge('C', 'D', weight=8)
G.add_edge('C', 'E', weight=10)
G.add_edge('D', 'E', weight=2)
G.add_edge('D', 'F', weight=6)
G.add_edge('E', 'F', weight=2)

shortest_path, total_distance = dijkstra(G, 'A', 'F')

print(f'O caminho mais curto é {shortest_path}, com a distância total de {total_distance}.')