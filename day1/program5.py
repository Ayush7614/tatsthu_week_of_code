run_player1 = int(input("Enter the run scored by player 1 in 60 balls: "))
run_player2 = int(input("Enter the run scored by player 2 in 60 balls: "))
run_player3 = int(input("Enter the run scored by player 3 in 60 balls: "))
strike_rate1 = run_player1 * 100/60
strike_rate2 = run_player2 * 100/60
strike_rate3 = run_player3 * 100/60
print("Strikerate of player 1 is",strike_rate1)
print("Strikerate of player 2 is",strike_rate2)
print("Strikerate of player 3 is",strike_rate3)
print("Runs scored by player 1 if they played 60 more balls is", run_player1 * 2)
print("Runs scored by player 2 if they played 60 more balls is", run_player2 * 2)
print("Runs scored by player 3 if they played 60 more balls is", run_player3 * 2)
print("Maximum no sixes player 1 could hit =", run_player1//6)
print("Maximum no sixes player 2 could hit =", run_player2//6)
print("Maximum no sixes player 3 could hit =", run_player3//6)
