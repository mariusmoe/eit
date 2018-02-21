import networkx as nx

with open('../data/test-set.csv') as f:
    lines = [l.strip().split(',') for l in f]
lines.pop(0)
lines = [map(int, x) for x in lines]



# TODO fix this so that it is a directed graph
# G = nx.Graph()
G = nx.Graph()

# [322758, 322773]
for i in lines:
    G.add_edge(i[0], i[1])
print G.number_of_nodes()




centrality = nx.eigenvector_centrality(G)
print (['%s %0.2f'%(node,centrality[node]) for node in centrality])
