import numpy as np


LEFT = 0
DIAG_UP = 1
DIAG_DOWN = 2

def traceback(traceback_matrix, states, max_position):
    """
    Use the traceback matrix to reconstruct the most optimal path
    Args: 
        traceback_matrix (np.array): traceback matrix
        states (list): list of states in hmm
        max_position (tuple): starting point for traceback
    Returns:
        optimal_path (str): reconstructed optimal state path after computation
    """
    tb_path = []  # use a list to store traceback path since states could be words instead of single chr

    # initialize starting position 
    current_row, current_col = max_position

    while current_col >= 0:
        # add current state to path
        tb_path.append(states[current_row])
        
        current_move = traceback_matrix[current_row, current_col]
        
        if current_move == LEFT:
            # Update col
            current_col -= 1
       
        elif current_move == DIAG_UP:
            # Update row and col
            current_row -= 1
            current_col -= 1
            
        elif current_move == DIAG_DOWN:
            # Update row and col
            current_row += 1
            current_col -= 1
      

    optimal_path = "-".join(tb_path[::-1])

    return optimal_path


def viterbi(obs, init_probs, trans_probs, emit_probs):
    """
    Implement the Viterbi algorithm for finding the most likely sequence of hidden states given a sequence of observations.
    Args:
        obs (str): observation sequence
        init_probs (dict): initial probabilities of each state
        trans_probs (dict): transition probabilities of each state
        emit_probs (dict): emission probabilities in a given state
    Returns:
        optimal_path (str): reconstructed optimal state path after computation
    """
    # Determine dimensions of matrices (num of hidden states x len of obs)
    states = list(init_probs.keys()) 
    rows = len(states)
    columns = len(obs)  

    # Initialization
    prob_matrix = np.zeros((rows, columns))
    traceback_matrix = np.zeros((rows, columns), dtype=int)

    # Recursion
    max_position, traceback_matrix = max_probabilites(obs, 
                                        init_probs, 
                                        trans_probs, 
                                        emit_probs, 
                                        prob_matrix, 
                                        traceback_matrix)

    # Traceback
    #max_position = np.unravel_index(np.argmax(prob_matrix, axis=None), prob_matrix.shape)
    optimal_path = traceback(traceback_matrix, states, max_position)

    return optimal_path


def main():
    # Example observation sequence
    obs = "GGCACTGAA"

    # Example initial probabilities (probability of starting in each state)
    init_probs = {
        "I": 0.2,
        "G": 0.8
    }

    # Example transition probabilities (probability of moving from one state to another)
    trans_probs = {
        "I": {"I": 0.7, "G": 0.3},
        "G": {"I": 0.1, "G": 0.9}
    }

    # Example emission probabilities (probability of observing a symbol in a given state)
    emit_probs = {
        "I": {"A": 0.1, "C": 0.4, "G": 0.4, "T": 0.1},
        "G": {"A": 0.3, "C": 0.2, "G": 0.2, "T": 0.3}
    }



if __name__ == "__main__":
    main()