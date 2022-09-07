import networkx as nx
import plotly.graph_objects as go


def print_map(network, node_trace, edge_trace, infected_nodes):
    node_adjacencies = []
    node_text = []
    node_sizes = []

    # Go through each nodes
    for node, adjacencies in enumerate(network.adjacency()):
        # Modification if you want to print node size based on number of edges
        # node_sizes.append(len(adjacencies[1]))

        # print infected node color
        if node == infected_nodes:
            node_adjacencies.append("violet")
            node_text.append("(infected) Node number " + str(node) + ' # of connections: ' + str(len(adjacencies[1])))

        # visit other nodes
        else:
            try:
                # get the distance between contaminated node and target node
                node_adjacencies.append(nx.astar_path_length(network, infected_nodes, node))
            except nx.NetworkXNoPath:
                # if path doesn't exist print it white
                node_adjacencies.append("white")
            node_text.append('Node number ' + str(node))

    # get the node colors and text
    node_trace.marker.color = node_adjacencies
    node_trace.text = node_text

    ## modification for size of nodes pased on number of edges
    # node_trace.marker.size = node_sizes

    # graph parameters
    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                        title='<br><b>NETWORK GRAPH DEMONSTRATING INFECTION SPREAD<b>',
                        titlefont_size=16,
                        titlefont=dict(family="sans serif", size=18, color="Black"),
                        showlegend=False,
                        plot_bgcolor="#202A44",
                        hovermode='closest',
                        margin=dict(b=20, l=5, r=5, t=40),
                        annotations=[dict(
                            text=" by Elnoel Akwa CS315 Spring 2022 University of Kentucky",
                            align="center",
                            font=dict(family="sans serif", size=18, color="white"),
                            showarrow=False,
                            xref="paper", yref="paper",
                            x=0.005, y=-0.002)],
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                    )

    fig.update_traces(textposition='top center')

    # print graph
    fig.show()
