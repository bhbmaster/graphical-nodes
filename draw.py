#!/usr/bin/env python

import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()

def print_info(G):
    print(f"* {G.nodes()} nodes and {G.edges()} edges")

print_info(G)

print("#######")

G.add_node("kostia")
G.add_nodes_from(["eric","abhi","mike"])

print_info(G)

print("#######")


G.add_edge(1,2)
G.add_edge("eric","abhi")

print_info(G)

print("#######")

cities={
    1:"Toronto",
    2:"SLC",
    "abhi":"SF",
    "kostia":"San Jose",
    "eric":"Los Angeles"
 #   "mike":"Boise"
}

H=nx.relabel_nodes(G,cities)

print_info(G)
print_info(H)

print("#######")

nx.draw(H, with_labels=True)
#plt.savefig("pic3.png")
plt.show()
