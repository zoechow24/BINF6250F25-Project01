
# BINF6250 - Project 08: Viterbi Algorithm
# Introduction
We are implementing the viterbi alogrithm to demonstrate our understanding of hidden markovs. Our objective is to finding the most likely sequence of hidden states given a sequence of observations.

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
    3. Returns updated prob_matrix and traceback_matrix
```
### Traceback
```
FUNCTION traceback(traceback_matrix):
    1. Reconstruct optimal path using traceback matrix
    2. Reverse path 
    3. Returns optimal path
```
# Successes
We were pretty fast to come up with a plan for this project. We felt we could take from some previous approaches from other projects and implement them into our pseudocode. Once we had a plan laid out, certain parts of the project seemed to come together quickly. We were also able to meet up together and work through problems with our code. We were also pretty quick to choose Positron as our mode for coding and updating our github branch which thus far has been much easier to use than Rstudio.

# Struggles
Our function, max_probabilities() which performs our recursion process was giving us issues particularly when updating the traceback.

# Personal Reflections
## Group Leader (Allen Benavidez)
Like many of my of the other projects previous to this one, I had to take some extra time to study the algorithm. Though I was able to understand the algorithm, I struggled to think of a specific way I could recreate the process in code. Overall, I found this algorithm to be easier to conceptually understand than some of our more recent projects.
## Other member (Zoe Chow)
Other members' reflections on the project

# Generative AI Appendix

