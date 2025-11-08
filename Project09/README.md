# Introduction
Implementing forward, backward and forward-backword algorithm

# Pseudocode

```
function probability(i, j,string, initial state, probability_matrix)
    if initial state is not 1:
        calculate first emissions
    for next position, add probabilities from previous emission to possible transitions and emission probs
    after the end position, add up accumalated probs for both states
return matrix_of_probs, total_probability

function forward
    call on probability function
return matrix_of_probs, total_probability


function backward()
    initial_state= 1
    reverse(string)
    call on probability function
    reverse columns of matrix_of_probs
return matrix_of_probs, total_probability


function forward_backward(obs,state, position_number)
    PMP = matrix 
    forward_matrix = index 0 of function forward
    backward_matrix = index 0 of function backward
    total_forward = index 1 of forward function
    total_backward = index 1 of backward function

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
