# Import necessary modules
import time
import random


def main():
    starting_money = 10000
    target_money = 1000000
    tries = 3

    play_game(starting_money, target_money, tries)


def play_game(starting_money, target_money, tries):
    # While the player still has tries
    while tries > 0:
        slow_print(f"Try number {4 - tries} of 3", 0.2, 0.2)
        result = roulette()

        if result == "died":
            slow_print("Game over ", 0.1, 0.1)
            break
        # End game if the player dies

        updated_money = money(starting_money, result)
        slow_print(
            f"Money after this try: ${updated_money:.0f} \n Goal: $1,000,000", 0.1, 0.1
        )
        # Tell the player how much money they have after a try

        starting_money = updated_money
        tries -= 1

        if updated_money >= target_money:
            slow_print("You got your money, now get out", 0.1, 0.1)
            break
        # Give the player the win once they meet the threshold

        if tries == 0:
            slow_print("Game over. You ran out of tries", 0.1, 0.1)
        # When the player runs out of tries, tell them that the game is done

def roulette():
    bullet = random.randint(1, 6)
    shots = 0
    exit = False
    used_chambers = set()

    while shots < 5:
        slow_print("Which bullet do you choose 1-6", 0.1, 0.1)

        while True:
            try:
                choice = int(input())
                if choice not in (1, 2, 3, 4, 5, 6):
                    raise ValueError
                elif choice in used_chambers:
                    # Alert the player they cannot shoot the same chamber twice when they choose the same one
                    slow_print(
                        "You cannot choose the same chamber twice in a try ", 0.1, 0.1
                    )
                    continue
                second = second_guess()
                if second == True:
                    used_chambers.add(choice)
                    # Add the player's choice to used_chambers if they say yes
                    break
                elif second == False:
                    pass
                    # Don't add anything if they say no
                else:
                    used_chambers.add(choice)
                    # Add the player's choice if second_guess() doesn't trigger
                    break
            except ValueError:
                slow_print("Answer appropriately", 0.1, 0.1)
        if choice == bullet:
            slow_print("You ... died", 0.1, 0.1)
            return "died"
        else:
            shots += 1
            slow_print("You ... lived", 0.1, 0.1)
            slow_print("Continue? y/n", 0.1, 0.1)
            # Let the player choose if they are going to continue within the same try
            while True:
                decision = input().lower()
                if decision == "n" or decision == "no":
                    exit = True
                    break
                elif decision == "y" or decision == "yes":
                    slow_print("Brave", 0.25, 0)
                    break
                else:
                    slow_print("Answer appropriately", 0.1, 0.1)

        if exit:
            break
    return shots


def money(starting_money, shots_survived):
    multipliers = [1.5, 1.75, 2.25, 3.5, 5]
    current_money = starting_money

    for i in range(shots_survived):
        current_money *= multipliers[i]

    return current_money


def slow_print(text, char_delay, word_delay):
    words = text.split()
    for word in words:
        for char in word:
            print(char, end="", flush=True)
            time.sleep(char_delay)
        print(" ", end="", flush=True)
        time.sleep(word_delay)
    print()


def second_guess():
    chance = random.randint(1, 3)
    # ! in 3 chance to trigger this event
    if chance == 1:
        while True:
            slow_print("Are you sure..? y/n", 0.1, 0.1)
            suspense = input().lower()
            if suspense == "y" or suspense == "yes":
                return True
            elif suspense == "n" or suspense == "no":
                return False
            else:
                slow_print("Answer appropriately", 0.1, 0.1)


if __name__ == "__main__":
    main()
