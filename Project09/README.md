# Introduction
Implementing forward, backward and forward-backword algorithm

# Pseudocode
## Helper Function for Forward and Backward Algorithm
```
function probability(i, j,string, initial symbol=0, probability_matrix)
    if j == 0 (first col):
        if inital symbol == 1:
            prob of position == initial symbol
        else:
            calculate probability of the first symbol (initial prob * emission prob)
    else:       
        for all other positions, multiply probabilities from previous emission to possible transitions and emission probs and add them together
return prob
```

## Forward Function
```
function forward
    initialize forward matrix (number of states X length of obs)
    for each row and column of the matrix, call on probability function
        add probability to probability matrix
    determine total accumulated probability of the matrix
return forward probability matrix, total accumulated probabiltiy
```

## Backward Function
```
function backward()
    initialize backward matrix (number of states X length of obs)
    set initial symbol probabiltiy = 1
    reverse observation string
    for each row and column of the matrix, call on probability function
        add probability to probability matrix
    determine total accumulated probability of the matrix
    reverse columns of the probability matrix so that columns are in the same order as obs
return backward probability matrix, total accumulated probability
```

## Foward-Backward Function
```
function forward_backward(obs)
    initialize matrix for PMP (number of states X length of obs)
    
    Get foward matrix, total forward prob, backward matrix, total backward prob (can call as tuples)
        forward_matrix = first return of forward (index 0)
        total_forward = second return of forward function (index 1)
        backward_matrix = first return of backward function (index 0)
        total_backward = second return of backward function (index 1)
    
    for each position of PMP calculate [PMP Calculation]
    create paths by choosing greatest state at position i
```

# Successes
Description of the team's learning points

# Struggles
Description of the stumbling blocks the team experienced

# Personal Reflections
## Group Leader
Group leader's reflection on the project

## Other member
Other members' reflections on the project

# Generative AI Appendix
As per the syllabus
