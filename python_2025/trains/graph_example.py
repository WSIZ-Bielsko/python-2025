from igraph import Graph, plot

# Create a completely connected graph with 6 nodes
num_nodes = 6

# Create an empty graph with 6 vertices
g = Graph()
g.add_vertices(6)  # Add 6 vertices (labeled 0 to 5)

# Define custom connections (edges) as pairs of vertex indices
custom_edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0), (0, 3)]

# Add the custom edges to the graph
g.add_edges(custom_edges)

graph = g

# Assign labels to nodes for clarity
graph.vs["label"] = [f'node{i}' for i in range(num_nodes)]

# Define colors based on the remainder of division by 3
colors = ["red", "blue", "green"]  # Colors for remainders 0, 1, and 2
graph.vs["color"] = [colors[i % 3] for i in range(num_nodes)]

# Plot the graph
plot(
    graph,
    # vertex_color=graph.vs["color"],
    vertex_color='lightblue',
    vertex_label=graph.vs["label"],
    layout=graph.layout("fruchterman_reingold"),  #circle, kamada_kawai, tree,fruchterman_reingold
    bbox=(300, 300),
    margin=20,
    target="graph_example.png",
)
