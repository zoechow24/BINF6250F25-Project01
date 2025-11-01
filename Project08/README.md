
# BINF6250 - Project 08: Viterbi Algorithm
# Introduction
Description of the project

# Pseudocode
## Viterbi Function
```
FUNCTION viterbi(obs_state, init_probs, trans_probs, emit_probs):
    1. Initialization
        Create 2 matrices of 2 x length of sequence to store **probabilities** and **traceback**

    2. Max Probabilities
        Recurse through all states and positions to find the highest probability and store values and paths in **probabilities** and **traceback** matrices, respectively

    3. Traceback
        Go through traceback matrix and reconstruct optimal path

```
## Helper Functions
### Max_Probabilities
```
FUNCTION Max_Probabilties(position, prob_matrix, traceback_matrix, init_probs, trans_probs, emit_probs):
    1. Calculate maximum probability for each position and possible state and store in **probability** matrix:
        Max(Most optimal previous probability * Transition Probability * Emission Probability)
    2. For each probability store 0, 1, or 2 to represent LEFT, DIAG-DOWN, DIAG-UP in traceback matrix.
```
### Traceback
```
FUNCTION traceback(traceback_matrix):
    1. Reconstruct optimal path using traceback matrix
    2. Reverse path 
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
