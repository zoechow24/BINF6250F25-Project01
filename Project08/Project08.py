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