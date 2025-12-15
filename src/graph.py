import networkx as nx
import pandas as pd

def build_tx_graph(df):
    G = nx.Graph()
    for _, row in df.iterrows():
        user = f"user_{row['user_id']}"
        merchant = f"merch_{row['merchant_id']}"
        G.add_node(user, type='user')
        G.add_node(merchant, type='merchant')
        if G.has_edge(user, merchant):
            G[user][merchant]['weight'] += 1
        else:
            G.add_edge(user, merchant, weight=1)
    return G

def suspicious_components(G, min_size=3):
    comps = [G.subgraph(c).copy() for c in nx.connected_components(G) if len(c) >= min_size]
    return comps
