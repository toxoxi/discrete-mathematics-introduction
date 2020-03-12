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

INVALID_DIAGONAL_INDICES_FOR_LT_TO_RB = {
  LT_TO_RB: [[-1, 1], [1, -1]],
  RT_TO_LB: [[0, -1], [-1, 0], [1, 0], [0, 1]],
}

INVALID_DIAGONAL_INDICES_FOR_RT_TO_LB = {
  LT_TO_RB: [[0, -1], [-1, 0], [1, 0], [0, 1]],
  RT_TO_LB: [[-1, -1], [1, 1]],
}

def execute(perm):
  # diagonals = n * (n - 3) / 2 # n=5 → 16
  # max_empty_cells = (n * n) - diagonals

  fill_permutations(perm)
  extend(perm, i = 0, j = 0)

# fill permutations with UNDETERMINED
def fill_permutations(perm):
  for i in range(GRID_SIZE):
    columns = []
    for _ in range(GRID_SIZE):
      columns.append(UNDETERMINED)

    perm.append(columns)

# extend permutation from bottom to top, from left to right
# 
# perm: comprehensive permutation
# n: number of cells of a side
# i: current horizontal index
# j: current vertical index
def extend(perm, i, j):
    if i >= GRID_SIZE:
      print(perm)
      exit()

    for diagonal in [LT_TO_RB, RT_TO_LB, NONE]:
      perm[i][j] = diagonal

      if can_be_extended_to_solution(perm, i, j, diagonal):
        # go to next column if vertical index reached to the top
        if j == GRID_SIZE - 1:
          j = 0
          i += 1
        else:
          j += 1

        extend(perm, i, j)
      
def can_be_extended_to_solution(perm, i, j, diagonal):
  surround_range = range(-1, 2)
  
  if diagonal == LT_TO_RB:    
    for type in [LT_TO_RB, RT_TO_LB]:
      for indices in INVALID_DIAGONAL_INDICES_FOR_LT_TO_RB[type]:
        target_i = i + indices[0]
        target_j = j + indices[1]
        if is_over_grid(target_i, target_j):
          continue
        if perm[target_i][target_j] == type:
          return False

  elif diagonal == RT_TO_LB:
    for type in [LT_TO_RB, RT_TO_LB]:
      for indices in INVALID_DIAGONAL_INDICES_FOR_RT_TO_LB[type]:
        target_i = i + indices[0]
        target_j = j + indices[1]
        if is_over_grid(target_i, target_j):
          continue
        if perm[target_i][target_j] == type:
          return False

  else:
    return True

def is_over_grid(i, j):
  if ((i < 0) or (i >= GRID_SIZE)) or ((j < 0) or (j >= GRID_SIZE)):
    return True
  else:
    return False

execute(perm = [])
