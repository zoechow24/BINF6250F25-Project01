import numpy as np

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
        HMM characteristics for the initial probs, transition probs, and emission probs.

        Args:
            init_probs (dict): Initial probabilities of each state
            trans_probs (dict of dict): Transition probabilities of each state
            emit_probs (dict of dict): Emission probabilities of each state for observed symbols
        """
        self.states = list(init_probs.keys())
        self.init_probs = init_probs
        self.trans_probs = trans_probs
        self.emit_probs = emit_probs

    def probability(self, i, j, obs, init_sym = 0, prob_matrix):
        """
        Calculate the probability of each state and symbol of the observation.

        Arg:
            i (int): current state position
            j (int): current symbol (observation position)
            obs (str): observation
            prob_matrix (arra): probability matrix
        Returns:
            prob (float): accumulated probability at that position
        """
        # calculate probability of first col/symbol of obs
        # if we're on the first col (j==0), prob = init_sym if init_sym=1, else init_prob * emit_prob


        # calculate probabiltiy of other cols
        # sum(last col * trans_prob * emit_prob)

        return prob

    def forward(self, obs):
        """
        Perform the Forward Algorithm and calculate the probabiltiy matrix and total accumulated probability for the observation given our HMM.

        Args:
            obs (str): observation
        Return:
            forward_matrix (array): matrices with the total probability at each given position
            accum_prob (float): total accumulated probability for the forward matrix (sum of last column)
        """
        # initialize forward matrix


        # loop through each position of the matrix and get total probability


        # determine total accumulated probability (sum of both states for last col)

        
        return forward_matrix, accum_prob

    def backward(self, obs):
        """
        Perform the Backward Algorithm and calculate the probabiltiy matrix and total accumulated probability for the observation given our HMM.

        Args:
            obs (str): observation
        Return:
            backward_matrix (array): matrices with the total probability at each given position
            accum_prob (float): total accumulated probability for the forward matrix (sum of last column)
        """
        # initialize backward matrix


        # reverse observation string


        # loop through each position of the matrix and get total probability


        # determine total accumulated probability (sum of both states for last col)


        # reverse matrix back so that the symbols of the observation string is in the correct order
        # np.fliplr(arr)

        
        return backward_matrix, accum_prob

    
    def forward_backward(self, obs):
        """
        Perform the Forward-Backward Algorithm. Calculate the probability of a position in the observation being assigned a particular hidden state using Posterior Marginal Probability (PMP), and use Posterior Decoding to determine path. 

        Args:
            obs (str): observations
        Returns:
            path (str): decoded path 
        """
        # initialize PMP matrix


        # Get forward matrix, total accumulated forward probability


        # Get backward matrix, total accumulated backward probability


        # do we want to create functions that calculates PMP and performs traceback? Similar to the max_probs and traceback functions from viterbi.
        # Calculate PMP for each position of the PMP matrix 
        


        # Select path using traceback


        return path

def main():
    # Example observation sequence
    obs = "ATGCAA"

    # Example initial probabilities (probability of starting in each state: E := Exon, I := Intron)
    init_probs = {
        "E": 0.6,
        "I": 0.4
    }

    # Example transition probabilities (probability of moving from one state to another)
    trans_probs = {
        "E": {"E": 0.8, "I": 0.2},
        "I": {"E": 0.3, "I": 0.7}
    }

    # Example emission probabilities (probability of observing a symbol in a given state)
    emit_probs = {
        "E": {"A": 0.3, "C": 0.2, "G": 0.2, "T": 0.3},
        "I": {"A": 0.1, "C": 0.4, "G": 0.4, "T": 0.1}
    }

    hmm = HMM(init_probs, trans_probs, emit_probs)
    print(f"Path: {hmm.forward_backward(obs)}")

if __name__ == "__main__":
    main()


