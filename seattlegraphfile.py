import pandas as pd
import networkx as nx

# Load the Excel file
excel_path = "SeattleTopData.xlsx"

# 1. Read the edges sheet
edges_df = pd.read_excel(excel_path, sheet_name="edges")

# 2. Read the attributes sheet
attributes_df = pd.read_excel(excel_path, sheet_name="attributes")

# 3. Create a directed graph (use nx.Graph() for undirected)
G = nx.DiGraph()

# Add nodes with attributes
for _, row in attributes_df.iterrows():
    G.add_node(
        row['name'],
        male=bool(row['male']),  # Convert to boolean for clarity
        followers=int(row['followers']),  # Ensure integer type
        type="person"  # Custom attribute for categorization
    )

# Add edges with weights
for _, row in edges_df.iterrows():
    G.add_edge(
        row['source'],
        row['target'],
        weight=float(row['weight'])  # Ensure float type
    )

# 4. Export to GraphML
nx.write_graphml(G, "seattle_social_network.graphml")

print(f"GraphML file saved! Nodes: {G.number_of_nodes()}, Edges: {G.number_of_edges()}")