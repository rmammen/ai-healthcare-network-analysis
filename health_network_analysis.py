import pandas as pd 
import networkx as nx 
import matplotlib.pyplot  as plt

# Load in the CSV
df = pd.read_csv("health_network_edges.csv")

print("Edge List Preview:")
print(df.head())
print(df.columns)

G = nx.from_pandas_edgelist(df, source="source", target="target")

# Graph info 
print("\nNumber of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())
print("Nodes in the graph:")
print(list(G.nodes))

# Calculate centrality 
degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)

# Put results into a dataframe
centrality_df = pd.DataFrame({
    "Node": list(degree_centrality.keys()),
    "Degree Centrality": list(degree_centrality.values()),
    "Betweenness Centrality": [betweenness_centrality[node] for node in degree_centrality.keys()]
})

# Sort by degree centrality from highest to lowest
centrality_df = centrality_df.sort_values(by="Degree Centrality", ascending=False)

print("\nCentrality Rankings:")
print(centrality_df)

# Save results 
centrality_df.to_csv("centrality_results.csv", index=False)

plt.figure(figsize=(10, 7))

# Position nodes nicely
pos = nx.spring_layout(G, seed=42)

# Make node sizes based on degree centrality
node_sizes = [degree_centrality[node] * 5000 for node in G.nodes()]

nx.draw_networkx(
    G,
    pos,
    with_labels=True,
    node_size=node_sizes,
    font_size=10
)

plt.title("AI Healthcare Ecosystem Network")
plt.axis("off")
plt.tight_layout()
plt.show()

top_3 = centrality_df.head(3)

print("\nTop 3 Important Nodes:")
print(top_3)