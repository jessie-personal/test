import random

print("""
===================
Rock Paper Scissors
===================

1) ✊
2) ✋
3) ✌️
""")
player = int(input("Pick a number: "))
computer = random.randint(1, 3)

if player == 1:
    player_choose = "✊"
elif player == 2:
    player_choose = "✋"
else:
    player_choose = "✌️"

if computer == 1:
    computer_choose = "✊"
elif computer == 2:
    computer_choose = "✋"
else:
    computer_choose = "✌️"

print(f"You chose: {player_choose}")
print(f"CPU chose: {computer_choose}")
if player == computer:
    print("It's a tie!")
elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
    print("The player won!")
else:
    print("The computer won!")