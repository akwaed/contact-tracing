# contact-tracing
CS 315 Capstone project

The program was designed to detect the possible flow
path of bacterial/viral infection in a sample community and
possibly serve as a means for contact tracing. For instance,
if a member (node) in a community gets infected by an 
illness the program will be able to provide the high-risk
nodes based on the connections with the infected node. The
main idea here is that each edge represents the
interconnections between nodes, we should be able to
determine the probability a node gets infected based on the
number of edges separating the node in question from the
infected node.
A combination of two algorithms was used as a
backbone for this project. The A Star (A*) search algorithm
was used to get the length of edges between the
contaminated and target node. Based on the length the
probability of infection and hence the node color is
determined. Also based on that probability we can
determine if the node is a high-risk node or not. The second
algorithm used was Dijkstra's algorithm. Passing the source
(infected) and target nodes, we could get the list of all
possible viral flow paths and hence implement a contact
tracing mechanism.
The program was implemented using Python 3 and a
Layered architectural pattern where each subtask has a
unique function called sequentially as the program is being
executed. Each function acted individually with the
exception of a few that used global variables to
intercommunicate with each other. Two python packages
were used in the project implementation namely:
• NetworkX for the creation and manipulation of the
network graphs used in the illustration of our
project
• Plotly was used simultaneously with NetworkX to
create an interactive graph visual of the graph
The Program execution can be broken down into three
main parts; graph creation, spread implementation and
contact tracing.
