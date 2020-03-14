# Recursion: Number of Moves to Solve the Hanoi Towers Puzzle
# 
# The number of moves required to solve the Hanoi Towers puzzle for n=1 and n=2 discs is equal to 1 and 3, respectively.
# Implement the recursive solution for the Hanoi Towers (described in the lectures) and count the number of moves for n=6n=6 discs.

def num_of_moves(n):
  if n == 1:
    return 1
  return (num_of_moves(n-1) * 2) + 1
