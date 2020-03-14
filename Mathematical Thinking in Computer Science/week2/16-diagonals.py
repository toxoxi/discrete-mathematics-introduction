# 16 Diagonals puzzle (Backtracking)
# 
# The goal in this puzzle is to place many diagonals
# into a square grid such that no two diagonals have a common point,
# or in other words, they do not touch each other
# 
# Size of the grid is n * n

GRID_SIZE = 5

# DIAGONALS
UNDETERMINED = -1
NONE = 0
LT_TO_RB = 1
RT_TO_LB = 2

# fill permutations with UNDETERMINED
def filled_permutations():
  perm=[]
  for i in range(GRID_SIZE * GRID_SIZE):
    perm.append(UNDETERMINED)
  return perm

# extend permutation from bottom to top, from left to right
# 
# perm: comprehensive permutation
def extend(perm):
  if perm[len(perm)-1] != UNDETERMINED:
    print(perm)
    exit()

  last_index = find_last_determined_index(perm)
  current_index = last_index + 1

  for diagonal in [LT_TO_RB, RT_TO_LB, NONE]:
    perm[current_index] = diagonal
    if can_be_extended_to_solution(perm, current_index):
      extend(perm)
    
  perm[current_index] = UNDETERMINED

def find_last_determined_index(perm):
  for i, diagonal in enumerate(perm):
    if diagonal == UNDETERMINED:
      return i-1

def can_be_extended_to_solution(perm, i):
  max_empty_cells = 9 # better to be calculated based on GRID_SIZE

  # false if no possibility
  if perm.count(NONE) > max_empty_cells:
    return False

  # next if NONE
  if perm[i] == NONE:
    return True

  n = GRID_SIZE
  is_top = (i + 1) % n == 0
  is_bottom = (i + 1) % n == 1
  is_left = i < n
  opposite_diagonal = RT_TO_LB if perm[i] == LT_TO_RB else LT_TO_RB

  diffs = []
  if not is_left:
    diffs.append(-n)
  if not is_left and not is_bottom:
    diffs.append(-n-1)
  if not is_left and not is_top:
    diffs.append(-n+1)
  if not is_bottom:
    diffs.append(-1)

  for d in diffs:
    target_index = i + d
    compare_target = perm[target_index]
    if abs(d) == 1 or abs(d) == n:
      if compare_target == opposite_diagonal:
        return False
    else:
      if (perm[i] == LT_TO_RB and abs(d) == n-1) or (perm[i] == RT_TO_LB and abs(d) == n+1):
        if compare_target == perm[i]:
          return False

  return True

extend(perm = filled_permutations())
