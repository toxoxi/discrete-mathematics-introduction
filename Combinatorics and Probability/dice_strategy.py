def compute_strategy(dices):
    assert all(len(dice) == 6 for dice in dices)
    dice_results = []

    strategy = dict()
    strategy["choose_first"] = False

    for i in range(len(dices)):
      strategy[i] = (i + 1) % len(dices)

    for i, dice in enumerate(dices):
      dice_results.append([])
      compared_dices = dices
      
      for j, compared_dice in enumerate(compared_dices):
        if i == j: continue
        dice_results[-1].append(count_wins(dice, compared_dice))
    
    for k, result in enumerate(dice_results):
      if all(wins[0] > wins[1] for wins in result):
        return {
          "choose_first": True,
          "first_dice": k,
        }

      most_winnable = result.index(max(result, key=lambda win: win[0] < win[1]))
      if k <= most_winnable:
        most_winnable+=1
      
      strategy[k] = most_winnable

    return strategy

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