# Introduction
We will implement one of the primary assembly algorithms from short-read data that is used today, using a simple form of the algorithm where we _assume perfect sequencing_. That is, everything is sequenced exacty once and there are no errors or variants in the sequencing. 

A graph is composed of **nodes** and **edges** and we will need to develop a data strcture to track edges between nodes in our graph. We have been provided with the basic class structure as well as descriptions of functions to `add_edge` and `remove_edge` from the graph. We will need to implement these functions in order to then build the de Bruijn graph.

In our implementation, we use a `defaultdict` data structure to hold a list of all edges in the graph where all "right" nodes connected to a "left" node are stored in a list for that node.

# Pseudocode
## Add Edge
```

function add_edge(self, left, right):
        dictionary[left].append(right)
        return dictionary

```

## Remove Edge
```
function remove_edge(self, left, right):
        dictionary[left].remove(right)
        return dictionary
```

## Build de Bruijn Graph
```

function build_debruijn_graph(self, input string, k):
dictionary = {}
  string <- length k 
  For each kmer of input string:
      left <- string[0:k]
      right <- string[1:k+1]
      add_edge(left,right)   
      #add k-1 mers as nodes with a directed edge from left k-1 mer to right k-1 mer
  return dictionary
```

## Print Eulerian Walk
```
function print_eularian_walk(self, seed = None):
        if seed is not None:
                set random seed  # random.seed(seed)

        first_node <- randomly select node
        return eularian_walk(first_node, seed)
        
```

## Eularian Walk
```
function eulerian_walk(node, seed = None):
        tour = list(node)
        for last node in tour:
            edge <- randomly selected edge from dictionary
            tour.append(edge)
            dictionary <- remove_edge(edge)
            if ______:
                return tour
            else:
                return eulerian_walk(edge, seed)
        
#V2
function eulerian_walk(node, seed = None):
        tour <- list(node)
        edge <- randomly selected edge from dictionary  #random.choice?
        tour.append(edge)
        dictionary <- remove_edge(node, edge)
        node <- edge
        if dictionary[node] == []  # if the key has an empty list
                return tour
        else  # recurse
                next_tour <- eularian_walk(node)  # store next node and edge
                return tour + next_tour  # combine lists
                

eulerian_walk:
Beginning at first_node as node

For node:
    follow a random valid edge from node
    remove edge
    recurse
```

# Successes
Description of the team's learning points

# Struggles
Description of the stumbling blocks the team experienced

# Personal Reflections
## Group Leader (Allen Benavidez)
Group leader's reflection on the project

## Other member (Zoe Chow)
Other members' reflections on the project

# Generative AI Appendix
As per the syllabus
