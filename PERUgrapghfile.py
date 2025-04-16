import pandas as pd
import networkx as nx

# Load the Excel file
excel_path = "dataFigueroa.xlsx"

# 1. Read the Relationships sheet (adjacency matrix)
adj_matrix = pd.read_excel(excel_path, sheet_name="Relationships", index_col=0)

# 2. Read the Attributes sheet
attributes = pd.read_excel(excel_path, sheet_name="Attributes", index_col="node")

# 3. Create a directed graph (use nx.Graph() for undirected)
G = nx.DiGraph()

# Add nodes with attributes
for node in adj_matrix.index:
    G.add_node(node, 
               Multinacional=int(attributes.loc[node, "Multinacional"]),
               type="elite_member")  # Custom attribute

# Add edges (where value == 1)
for source in adj_matrix.index:
    for target in adj_matrix.columns:
        if adj_matrix.loc[source, target] == 1:
            G.add_edge(source, target, relationship="connection")

# 4. Export to GraphML
nx.write_graphml(G, "peruvian_elite_network.graphml")

print(f"GraphML file saved! Nodes: {G.number_of_nodes()}, Edges: {G.number_of_edges()}")