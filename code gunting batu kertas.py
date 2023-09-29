import random

print("Let's play Rock Paper Scissors!")
print("Enter your choice - rock, paper or scissors")

player_score = 0
computer_score = 0

rounds = 5

for _ in range(rounds):
    print("""
       _______
  --'   ____)
         (_____)
         (_____)
          (____)
  --.__(___)
    """)
    user_choice = input().lower()

    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chooses {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        user_choice == 'rock' and computer_choice == 'scissors' or
        user_choice == 'paper' and computer_choice == 'rock' or
        user_choice == 'scissors' and computer_choice == 'paper'
    ):
        print("You win this round!")
        player_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    print("Player score:", player_score)
    print("Computer score:", computer_score)
    print()

print("""
      _________      .__                                   
     /   _____/ ____ |__| ______ __________   ___________  
     \_____  \_/ ___\|  |/  ___//  ___/  _ \ /  _ \_  __ \ 
     /        \  \___|  |\___ \ \___ (  <_> |  <_> )  | \/ 
    /_______  /\___  >__/____  >____  >____/ \____/|__|    
            \/     \/        \/     \/              
""")

if player_score > computer_score:
    print("Congratulations, you win!")
elif player_score < computer_score:
    print("Computer wins!")
else:
    print("It's a tie!")
