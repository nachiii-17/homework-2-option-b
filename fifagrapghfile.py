 
import pandas as pd
import networkx as nx

# Read the Excel sheets
players_df = pd.read_excel('fifa2022.xlsx', sheet_name='fifa2022')
clubs_df = pd.read_excel('fifa2022.xlsx', sheet_name='attributes_club')
countries_df = pd.read_excel('fifa2022.xlsx', sheet_name='attributes_country')

# Create a directed graph
G = nx.DiGraph()

# Add country nodes with attributes
for _, row in countries_df.iterrows():
    G.add_node(row['country'], 
               type='country',
               developed=row['developed'])

# Add club nodes with attributes
for _, row in clubs_df.iterrows():
    G.add_node(row['club'],
               type='club',
               winner_country=row['winnerCountry'])

# Add player nodes and edges
for _, row in players_df.iterrows():
    player_name = row['name']
    player_attributes = {
        'type': 'player',
        'position': row['pos'],
        'age': row['age2022'],
        'caps': row['caps'],
        'goals': row['goals'],
        'club': row['club'],
        'nationality': row['nationality']
    }
    
    # Add player node
    G.add_node(player_name, **player_attributes)
    
    # Add edges: player to club and player to country
    G.add_edge(player_name, row['club'], relationship='plays_for')
    G.add_edge(player_name, row['nationality'], relationship='represents')

# Save as GraphML file
nx.write_graphml(G, 'fifa2022_graph.graphml')

print("GraphML file created successfully with:")
print(f"- {len([n for n in G.nodes() if G.nodes[n]['type'] == 'country'])} countries")
print(f"- {len([n for n in G.nodes() if G.nodes[n]['type'] == 'club'])} clubs")
print(f"- {len([n for n in G.nodes() if G.nodes[n]['type'] == 'player'])} players")