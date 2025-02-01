import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Add nodes with labels and colors
num_nodes = 6
colors = ["red", "blue", "green"]
node_colors = [colors[i % 3] for i in range(num_nodes)]
labels = {i: f'node{i}' for i in range(num_nodes)}

# Add nodes
G.add_nodes_from(range(num_nodes))

# Add custom edges
custom_edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0), (0, 3)]
G.add_edges_from(custom_edges)

# Create the layout
pos = nx.spring_layout(G)  # equivalent to fruchterman_reingold

# Draw the graph
plt.figure(figsize=(4, 4))
nx.draw(G,
        pos=pos,
        node_color='lightblue',
        labels=labels,
        with_labels=True,
        node_size=1000)

# Save the plot
plt.show()
# plt.savefig('graph_example.png', bbox_inches='tight')
# plt.close()
