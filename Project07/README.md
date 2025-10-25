# BINF6250 Project07: Burrows-Wheeler Transformation
# Introduction
The Burrows-Wheeler Transform (BWT) is a powerful algorithm used in data compression and bioinformatics. In this project, we will use BWT to compress and revert a string. This works by sorting all possible cyclic rotations of a string lexicographically and extracting the last column of the sorted matrix. 

# Pseudocode
## Burrows-Wheeler Transform
```
FUNCTION BWT:
  takes input string and returns transform of the input string (last column)
  1. Create all rotations of the input string
  2. Sort rotated strings lexicographically
  3. Extract last column

FUNCTION suffix_array:
  takes input string and returns list of integers representing the starting positions of the lexicographically sorted suffixes
  
  
FUNCTION BWT_from_suffix_array:
  calculates BWT from a suffix array. Uses suffix array to identify the character that precedes each suffix in the sorted order. 
  takes input string and suffix positions and returns BWT of the input string
```

## Inverting Burrows-Wheeler Transform
```
FUNCTION cal_count:
  takes input string and returns a dictionary that indicates the count of characters lexicographically smaller than it
  Keys: unique letters
  Value: count of characters lexicographically smaller than it


FUNCTION cal_occur: 
  calculate occurrence of each unique character within the bwt_string
  takes bwt_string and returns dictionary of list with occurence counts
  Ex. cal_occur('annb$aa') -> 
        {'$': [0, 0, 0, 0, 1, 1, 1], 'a': [0, 1, 1, 1, 1, 2, 3], 'b': [0, 0, 0, 1, 1, 1, 1], 'n': [0, 0, 2, 2, 2, 2, 2]}


FUNCTION update_range:
  updates search range during backward search in the BWT pattern matching algorithm
  Args:
        lower: The lower boundary of the current range.
        upper: The upper boundary of the current range.
        count: cal_count dictionary
        occur: cal_occur dictionary
        a: The character being processed in the pattern.
    
    Returns:
        A tuple containing the updated lower and upper boundaries of the range.

FUNCTION find_match:
  searches for all occurrences of the query string within the. reference string and returns a list of integers representing the starting positions of the occurrences of the query string within the reference string
  Args:
        query: The pattern string to search for.
        reference: The text string to search within.
    
    Returns:
        A list of integers representing the 0-based starting positions of all occurrences of the query string within the reference string. 
        Empty list if no matches are found.
        
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
