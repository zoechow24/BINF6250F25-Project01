import numpy as np
import math

START = 0
LEFT = 1
DIAG_UP = 2
DIAG_DOWN = 3


class HMM:
    """
    Hidden Markov Model
    Attributes
    ----------
    init_probs : dict
        Log initial state probabilities.
    trans_probs : dict of dict
        Log transition probabilities.
    emit_probs : dict of dict
        Log emission probabilities.
    states : list
        Ordered list of HMM states.
    """

    def __init__(self, init_probs, trans_probs, emit_probs):
        """
        Log probabilities for the initial probs, transition probs, and emission probs.
        Args:
            init_probs (dict): Initial probabilities of each state
            trans_probs (dict of dict): Transition probabilities of each state
            emit_probs (dict of dict): Emission probabilities of each state for observed symbols
        """
        self.states = list(init_probs.keys())
        self.init_probs = {state: math.log(prob) for state, prob in init_probs.items()}
        self.trans_probs = {
            state: {
                transition: math.log(prob)
                for transition, prob in trans_probs[state].items()
            }
            for state in trans_probs
        }
        self.emit_probs = {
            state: {sym: math.log(prob) for sym, prob in emit_probs[state].items()}
            for state in emit_probs
        }

    def _max_probabilities(self, i, j, obs, prob_matrix):
        """
        Calculate maximum probability and determine the traceback direction of each position of the observation.
        Args:
            i (int): current state position
            j (int): current observation position
            obs (str): observation
            prob_matrix (array): probability matrix
        Returns:
            max_prob (float): Best log probability to reach this state at this position
            traceback (int): encoded traaceback direction
        """
        rows = len(self.states)
        state = self.states[i]
        sym = obs[j]

        if j == 0:
            # calculate the probability of the first column
            max_prob = self.init_probs[state] + self.emit_probs[state][sym]
            traceback = START
        else:
            candidates = []  # (list of probability, traceback)

            # LEFT - calculating prob from same state transition
            left = prob_matrix[i, j - 1]
            left_prob = (
                left + self.trans_probs[state][state] + self.emit_probs[state][sym]
            )
            candidates.append((left_prob, LEFT))

            # both cases will be performed if conditions are met (aka when there are more than 2 states)
            # DIAG_DOWN
            if i < rows - 1:
                prev_state = self.states[i + 1]
                diag_down = prob_matrix[i + 1, j - 1]
                diag_down_prob = (
                    diag_down
                    + self.trans_probs[prev_state][state]
                    + self.emit_probs[state][sym]
                )
                candidates.append((diag_down_prob, DIAG_DOWN))

            if i > 0:
                prev_state = self.states[i - 1]
                diag_up = prob_matrix[i - 1, j - 1]
                diag_up_prob = (
                    diag_up
                    + self.trans_probs[prev_state][state]
                    + self.emit_probs[state][sym]
                )
                candidates.append((diag_up_prob, DIAG_UP))

            # select greatest probability with corresponding traceback direction
            max_prob, traceback = max(candidates, key=lambda x: x[0])

        return max_prob, traceback

    def _traceback(self, traceback_matrix, max_position):
        """
        Use the traceback matrix to reconstruct the most optimal path of states for the observation.
        Args:
            traceback_matrix (np.array): traceback matrix
            max_position (tuple): starting point for traceback
        Returns:
            optimal_path (str): reconstructed optimal state path after computation
        """
        tb_path = []  # use a list to store traceback path since states could be words instead of single chr

        # initialize starting position
        current_row, current_col = max_position

        # stop condition: reached start column
        while True:
            # record state before moving
            tb_path.append(self.states[current_row])

            # break condition
            if current_col == 0:
                break

            current_move = traceback_matrix[current_row, current_col]

            if current_move == LEFT:
                current_col -= 1

            elif current_move == DIAG_UP:
                current_row -= 1
                current_col -= 1

            elif current_move == DIAG_DOWN:
                current_row += 1
                current_col -= 1

        optimal_path = "-".join(tb_path[::-1])

        return optimal_path

    def viterbi(self, obs):
        """
        Implement the Viterbi algorithm for finding the most likely sequence of hidden states given a sequence of observations.
        Args:
            obs (str): observation sequence
        Returns:
            optimal_path (str): reconstructed optimal state path after computation
        """

        # Determine dimensions of matrices (num of hidden states x len of obs)
        rows = len(self.states)
        columns = len(obs)

        # Initialization
        prob_matrix = np.full((rows, columns), -math.inf)  # use -inf due to log-space
        traceback_matrix = np.zeros((rows, columns), dtype=int)

        # Recursion
        for i in range(rows):
            for j in range(columns):
                # Calculate+update score and traceback of each position
                prob_matrix[i, j], traceback_matrix[i, j] = self._max_probabilities(
                    i, j, obs, prob_matrix
                )

        # determine max_position of the last column to start traceback
        max_position = (np.argmax(prob_matrix[:, -1]), columns - 1)

        # traceback
        optimal_path = self._traceback(traceback_matrix, max_position)

        return optimal_path


def main():
    # Example observation sequence
    obs = "GGCACTGAA"

    # Example initial probabilities (probability of starting in each state)
    init_probs = {"I": 0.2, "G": 0.8}

    # Example transition probabilities (probability of moving from one state to another)
    trans_probs = {"I": {"I": 0.7, "G": 0.3}, "G": {"I": 0.1, "G": 0.9}}

    # Example emission probabilities (probability of observing a symbol in a given state)
    emit_probs = {
        "I": {"A": 0.1, "C": 0.4, "G": 0.4, "T": 0.1},
        "G": {"A": 0.3, "C": 0.2, "G": 0.2, "T": 0.3},
    }

    hmm = HMM(init_probs, trans_probs, emit_probs)
    print(f"Optimal Path: {hmm.viterbi(obs)}")


if __name__ == "__main__":
    main()
