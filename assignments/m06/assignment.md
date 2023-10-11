---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.14.6
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# Path, connected components and centrality 

## Defining Paths 
There are many ways to count a length of a path between two nodes. Here are four basic definition of *paths*.

- **Walk**: Walk is a sequence of nodes and edges that are connected to form a continuous rout in a network. In a directed network, edges must be traversed according to their direction. It is possible that there may not be a walk in both directed and undirected networks.
- **Trail**: A walk that does not go through the same edge more than once. 
- **Path**: A walk that does not go through the same node more than once. 
- **Cycle**: Cycle is a path where source and target node are the same 
- **Path legnth**: Number of edges in the path. 

***Note***: 
The walk defined above is sometimes referred to as a *path*, and path defined above is instead called "simple path." It is important to be aware of this definitional difference. For this course, we adopt the definitions listed above. 

Now, let's do some exercise. First, let's consider a simple graph below.  

```python
import igraph

g = igraph.Graph()
g.add_vertices(4)
g.add_edges([(0, 1), (1, 2), (0, 2), (0, 3)])
igraph.plot(g, bbox=(150, 150), vertex_label=list(range(4)))
```

In a network, a path is defined as a series of edges that connect two nodes. In this straightforward example, there is at least one path connecting nodes 2 and 3. Let's generate the paths between them by using igraph.

```python
g.get_all_simple_paths(2, to=3)
```

A simple path is defined as a path that does not contain any cycles. If cycles were allowed, there would be an infinite number of paths as one could continuously go around the cycle as many times as they wanted. 

We are often most interested in shortest paths. In an unweighted network, the shortest path is the one with the fewest edges. We can see that of the two simple paths between nodes 2 and 3, one is shorter than the other. We can get this shortest path by

```python
g.get_shortest_paths(2, to=3)
```

Note that there can be multiple shortest paths between two nodes.

# Connected component 

In the simple network above, we can see that for every pair of nodes, we can find a path connecting them. This is the definition of a connected graph. We can check this property for a given graph:

```python
components = g.connected_components()
print("# of components = ", len(components))  # number of components
components.membership  # the IDs of the component each node belongs to.
```

Not every graph is connected:

```python
g.add_vertices(2)
g.add_edges([(4, 5)])
igraph.plot(g, bbox=(150, 150), vertex_label=list(range(6)))
```

```python
components = g.connected_components()
print("# of components = ", len(components))  # number of components
components.membership  # the IDs of the component each node belongs to.
```

And there is no path between nodes in different connected components. And therefore, there is no shortest path between them as well. 

```python
g.get_shortest_paths(0, 5)
```

You can find the set of nodes in the same connected component by 

```python
import numpy as np

np.where(np.array(components.membership) == 0)[0]  # List of nodes with membership = 0
np.where(np.array(components.membership) == 1)[0]  # List of nodes with membership = 1
```

We often care about the largest connected component, which is sometimes referred to as the core of the network. We can make use of numpy `unique` function in order to obtain the largest connected component. 

```python
component_ids, _, freq = np.unique(
    components.membership, return_counts=True, return_inverse=True
)
largest_connected_component_id = component_ids[np.argmax(freq)]
nodes_in_largest_component = np.where(
    np.array(components.membership) == largest_connected_component_id
)[
    0
]  # list of nodes in the largest connected component.
print(nodes_in_largest_component)
```

```python
g_sub = g.induced_subgraph(nodes_in_largest_component)
igraph.plot(g_sub, vertex_label=nodes_in_largest_component, bbox=(150, 150))
```

## Directed paths and components 

Let's extend these ideas about paths and connected components to directed graphs.

```python
g = igraph.Graph(directed=True)
g.add_vertices(6)
g.add_edges(
    [
        (0, 1),
        (1, 2),
        (2, 1),
        (2, 3),
        (2, 5),
        (3, 1),
        (3, 4),
        (3, 5),
        (4, 5),
        (5, 3),
    ]
)
igraph.plot(g, bbox=(250, 250), vertex_label=list(range(6)))
```

In a directed graph, we know that an edge from one node to another does not necessarily mean that there is an edge in the opposite direction. This asymmetry also applies to paths in directed graphs. For example, in the given graph, there is a path from node 0 to node 3, but not in the reverse direction.

```python
print("From 0 to 3", g.get_all_simple_paths(0, to=3))
print("From 3 to 0", g.get_all_simple_paths(3, to=0))
```

The shorst path from 4 to 1 cannot simply go directly to node 3 due to the directionality of the edges; it has to go a longer route. 

```python
g.get_shortest_paths(4, 1)
```

Directed networks have two kinds of connected components. 
- **Strongly connected components**: Strongly connected means that there exists a direct path between every pair of nodes, i.e., that from any node to any other nodes while respecting the edge directionality. 
- **Weakly connected components**: Weakly connected means that there exists a path between every pair of nodes when ignoring the edge directionality. 

```python
print(list(g.connected_components(mode="strong")))
print(list(g.connected_components(mode="weak")))
```

# Closeness centrality

You are now able to compute one of the most widely used measure of network centrality, *closeness centrality*. Closeness centrality of a node measures how  *close* a node is to to any other nodes in a network. Nodes with a high closeness play an influential role in controlling *flows* on the network such as information, goods, and disease. More specifically, a closeness of a node is defined as

$$
c_i:= \frac{n-1}{\sum_{j, i\neq j} d(i,j)},
$$

where $d(i,j)$ is the shortest path length between nodes $i$ and $j$, and $n$ is the number of nodes in the network. With `igraph`, it can be computed by 

```python
g.closeness()
```

And the closeness centrality is affected by the edge directionality. But due to the asymmetric nature of the paths, there are two kinds of the closeness. One defined based on the length of *in-coming* paths and the other based on the length of *out-going* paths. Namely, 
$$
c^{\text{in}}_i:= \frac{n-1}{\sum_{j, i\neq j} d(j,i)},
$$
$$
c^{\text{out}}_i:= \frac{n-1}{\sum_{j, i\neq j} d(i,j)},
$$
where $d(i,j)$ is the length of directed path from node $i$ to node $j$. With `igraph`, they can be computed by  

```python
g.closeness(mode="in"), g.closeness(mode="out")
```

Notice that node $0$ has NaN in coming closeness, because there is no path to node $i$ from any other nodes in the network. 


# Betweenness centrality

Betweenness centrality is another widespread centrality based on the shortest path lengths. It is defined by
$$
b_i:= \sum_{s \neq t\neq i} \frac{\sigma_{s,i,t}}{\sigma_{s,t}}
$$
where $\sigma_{s,t}$ is the number of shortest paths between node $s$ and node $v$, and $\sigma_{s,i,t}$ is the shortest paths between $s$ and $t$ that goes through node $i$. A node with a high betweeness centrality means that the node is a dominant intermediary of flows (that go through the shortest path) between nodes on the network. Or, you can think of it as a bottleneck of flows. 

Betweenness centrality is conceptually similar to the closeness centrality. But it gives a higher centrality to nodes intermediating different clusters than the closeness centrality does. You can compute the betweenness centrality by   

```python
g.betweenness()
```

# Assignment 

We will use the worldwide airport network. We ignore the edge directionality in this assingment. We load and construct the network as follows. 

```python
import pandas as pd

node_table = pd.read_csv(
    "https://raw.githubusercontent.com/skojaku/adv-net-sci-course/main/data/airport_network_v2/node_table.csv"
)
edge_table = pd.read_csv(
    "https://raw.githubusercontent.com/skojaku/adv-net-sci-course/main/data/airport_network_v2/edge_table.csv"
)
```

```python
src, trg = tuple(edge_table[["src", "trg"]].values.T)
edge_list = tuple(zip(src, trg))

# node_id and name dictionary
n_nodes = node_table.shape[0]
id2name = np.array([""] * n_nodes, dtype="<U64")
id2name[node_table["node_id"]] = node_table["Name"].values

g = igraph.Graph(
    edge_list,
    vertex_attrs=dict(Name=id2name),
)

# You can retrieve the airport names by
print(g.vs[0]["Name"], ",", g.vs[1]["Name"], ", ...")
```

<!-- #region -->
**Assignment 1: Is there a direct flight between Syracuse airport (SYR) and Fairbanks Intl  Fairbanks (FAI)? A *direct* flight is one with no intermediate stops.**

Note: 
You can find the node ids of the aiport by 
```python
node_table[node_table["IATA/FAA"].isin(["FAI", "SYR"])]  
```
<!-- #endregion -->

```python

```

**Assignment 2: If I wanted to fly from Syracuse to Fairbanks, Alaska what would be an itinerary with the fewest number of flights? Show the itenerary with the airport names**

Note: You can use id2name to get the aiport names, e.g., id2name[0] gives the name of the aiport corresponding to node 0.

```python

```

**Assignment 3: Is it possible to travel from any airport in the network to any other airport in the netwrok, possibly using connecting flights? In other words, does there exist a path in the network between every possible pair of airports? Ignore the airports with no edge.**

```python

```

**Assignment 4: Which airport is the most central in terms of the closeness centrality? List the top 5 most central airport. You may use the APIs to compute the shortest path but do not use any APIs that give the closeness centrality such as igraph.Graph.closeness**. 

```python
# Your code -------------------
# Compute the centrality

centrality = np.zeros(n_nodes)
centrality = (
    ...
)  # Compute the closeness centrality of each node $i$ and set it to centrality[i].
# -------------------

# Check the correctness of the computed closeness
assert np.all(np.isclose(centrality, g.closeness()))

# Show the top K airport with the largst centrality
topK = 5
top_airport_ids = np.argsort(centrality)[::-1][:topK]
node_table.iloc[top_airport_ids][["Name"]]
```

**Assignment 5: Compute the betweenness centrality of the airports and show the top 5 airports. You may use APIs that directly compute the betweenness centrality such as igraph.Graph.betweenness**. 

You should see an interesting airport that is not central in terms of the closeness centrality but is central in terms of the betweeness centrality. If you are curious why, here is a nice reading to understand why: https://toreopsahl.com/2011/08/12/why-anchorage-is-not-that-important-binary-ties-and-sample-selection/ 

```python

```
