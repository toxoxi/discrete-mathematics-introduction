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