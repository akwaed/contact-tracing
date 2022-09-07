# Create even weight network graphs having random edge link attributes
# node Attributes are node id and node color = 1

# Algorithm for spread:
# define an infected node and spread the infection based on adjencies based on real life situation
# graph is unidrected

import networkx as nx
import plotly.graph_objects as go

import function

print("Let's create a sample community")

# probability there is an edge connecting nodes
prob_edge = .125

sample_size = int(input("Whats the number of people in your community: "))

# define the network graph
ba = nx.random_geometric_graph(sample_size, prob_edge)
# ba=nx.connected_caveman_graph(30, 3)


# Create Edges
# Add edges as disconnected lines in a single trace and nodes as a scatter trace

edge_x = []
edge_y = []
for edge in ba.edges():
    x0, y0 = ba.nodes[edge[0]]['pos']
    x1, y1 = ba.nodes[edge[1]]['pos']
    edge_x.append(x0)
    edge_x.append(x1)
    edge_x.append(None)
    edge_y.append(y0)
    edge_y.append(y1)
    edge_y.append(None)

edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=0.5, color='orange'),
    hoverinfo='none',
    mode='lines')

node_x = []
node_y = []
for node in ba.nodes():
    x, y = ba.nodes[node]['pos']
    node_x.append(x)
    node_y.append(y)

node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers',
    hoverinfo='text',
    marker=dict(
        showscale=True,
        # colorscale for coloring algorithm
        colorscale='Blues',
        reversescale=True,
        color=[],
        size=10,
        colorbar=dict(
            thickness=15,
            title='Probability of no infection',
            xanchor='left',
            titleside='right'
        ),
        line_width=2))

# Color Node Points
# Color node points by the probability of infection.
#

infected_node = 2
function.print_map(ba, node_trace, edge_trace, infected_node)

end = False

while not end:
    user_input = int(input("Chose among the following options \n "
                     "1. Declare and infected node\n"
                     "2. Backtrack and infection \n"
                     "3. Get the list of high risk cases\n "))

    if user_input == 1:
        node_adjacencies=[]
        node_text=[]
        infected_node= int((input("enter the infected node")))
        function.print_map(ba, node_trace, edge_trace, infected_node)

        # to_continue = y
        # while to_continue == y:
        #     inf_node = int(input("enter the infected node"))
        #     infected_node.append(inf_node)
        #     to_continue = input("do you want to declare another infected node? (y/n)")
        # #function.print_map(ba, node_trace, edge_trace, infected_node)

    elif user_input == 2:
        start = int(input("enter the contaminated node number "))
        end = int(input("enter the desired target "))
        print("here are the  probable infection paths ")
        print([p for p in nx.all_shortest_paths(ba, source=start, target=end)])
        continue

    elif user_input == 3:
        # stor final values
        results = []

        for node in ba.nodes:
            try:
                # if distance between noods is less than 5
                if (nx.astar_path_length(ba, infected_node, node)) < 5:
                    results.append(node)
            except nx.NetworkXNoPath:
                print("There is just one high risk cases")

        print(results)
        print(len(results))
