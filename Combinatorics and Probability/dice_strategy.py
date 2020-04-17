def find_the_best_dice(dices):
    assert all(len(dice) == 6 for dice in dices)

    dice_results = []

    for i, dice in enumerate(dices):
      dice_results.append([])
      compared_dices = dices
      
      for j, compared_dice in enumerate(compared_dices):
        if i == j: continue
        dice_results[-1].append(count_wins(dice, compared_dice))
    
    for k, result in enumerate(dice_results):
      if all(wins[0] > wins[1] for wins in result):
        return k

    return -1
    
def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0
    
    for num1 in dice1:
      for num2 in dice2:
        if num1 > num2:
          dice1_wins += 1
        if num2 > num1:
          dice2_wins += 1

    return (dice1_wins, dice2_wins)