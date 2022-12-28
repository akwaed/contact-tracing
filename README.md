# Contact_Tracing

## Description

This creates a network graph to demonstrate network contamination

## Requirements

This package require:
 - python3
 - python3 Standard Library
 - plotly
 - networkx

### Command lines

```bash
python3 main.py
```

### Features

This program basically has a three step procedue:
  1. Generate a random geometric graph with x nodes on a ploty graph. (number x is provided by the user)
  2. Prompt the user to decleare which nodes are infected and base on this color surrounding nodes based on their infenction probability. The color      spectrum is from orange to blue, with orange meaning you're infected and blue signifying you are not.
  3. Using A* algrorithm can back track an infection from "patient zero" to a user selected node
  
 ### Scope
 
The goal of this project was to demostrate the versility of Computational concepts in real-life senario. The program could be impemented in a computer network to determine probability connect nodes get infected. More importantly the project could be use in communities infected by infection/disease outbreaks. Thanks to the backtracking ability implemented using the A* algorithm a contact tracing mecahnism could be implemented to trace an infection path.

### Notes
The various file description for the above files.
- [Network Graph.pdf](Network Graph.pdf): The research paper I submitted for the project written in ACM paper format
- [functions.py](functions.py): The functions used to print and display various contents of the graph
- [main.py](main.py): main py function file to run and excute the program
- [nx_functions](nx_functions): Documentation from the NetworkX libary on the various algorithms used by the program
