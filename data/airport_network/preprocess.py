import pandas as pd
import numpy as np
from scipy import sparse
from scipy.sparse.csgraph import connected_components


def load_network(func):
    def wrapper(binarize=True, symmetrize=False, *args, **kwargs):
        net, labels, node_table = func(*args, **kwargs)
        if symmetrize:
            net = net + net.T
            net.sort_indices()

        _, comps = connected_components(csgraph=net, directed=False, return_labels=True)
        ucomps, freq = np.unique(comps, return_counts=True)
        s = comps == ucomps[np.argmax(freq)]
        labels = labels[s]
        net = net[s, :][:, s]
        if binarize:
            net = net + net.T
            net.data = net.data * 0 + 1
        node_table = node_table[s]
        return net, labels, node_table

    return wrapper


@load_network
def load_airport_net():
    # Node attributes
    node_table = pd.read_csv(
        "https://raw.githubusercontent.com/skojaku/core-periphery-detection/master/data/node-table-airport.csv"
    )

    # Edge table
    edge_table = pd.read_csv(
        "https://raw.githubusercontent.com/skojaku/core-periphery-detection/master/data/edge-table-airport.csv"
    )
    # net = nx.adjacency_matrix(nx.from_pandas_edgelist(edge_table))

    net = sparse.csr_matrix(
        (
            edge_table["weight"].values,
            (edge_table["source"].values, edge_table["target"].values),
        ),
        shape=(node_table.shape[0], node_table.shape[0]),
    )

    s = ~pd.isna(node_table["region"])
    node_table = node_table[s]
    labels = node_table["region"].values
    net = net[s, :][:, s]
    return net, labels, node_table


net, labels, node_table = load_airport_net()
src, trg, _ = sparse.find(net)
src_trg = np.maximum(src, trg) + 1j * np.minimum(src, trg)
src_trg = np.unique(src_trg)
src, trg = np.real(src_trg).astype(int), np.imag(src_trg).astype(int)
edge_table = pd.DataFrame({"src": src, "trg": trg}).to_csv(
    "edge_table.csv", index=False
)
node_table.to_csv("node_table.csv", index=False)
