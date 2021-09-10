import networkx as nx
import matplotlib.pyplot as plt
from sys import argv

if (len(argv) > 1):
    with open(argv[1], 'r') as fasta:
        data = [x.strip('\n') for x in fasta if not x.startswith('>')]
    # print(data)
    seq1 = [x for x in data[0] if x is not '-']
    seq2 = [x for x in data[1] if x is not '-']
    pairs = [(s1,s2) for s1,s2 in zip(data[0], data[1])]
    B = nx.Graph()
    B.add_nodes_from(seq1, bipartite=0)
    B.add_nodes_from(seq2, bipartite=1)
    for pair in pairs:
        if '-' not in pair:
            B.add_edge(pair[0], pair[1])
    nx.draw(B)
    plt.savefig("test.png")
    # for i, aa in enumerate(data[0]):

    # B.add_nodes_from([1,2,3,4], bipartite=0) # Add the node attribute "bipartite"
    # B.add_nodes_from(['a','b','c'], bipartite=1)
    # B.add_edges_from([(1,'a'), (1,'b'), (2,'b'), (2,'c'), (3,'c'), (4,'a')])