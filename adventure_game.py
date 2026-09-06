# adventure_game.py
# A text-based CLI adventure game where the player explores a forest or a cave
# in search of a legendary treasure, making choices that lead to winning,
# losing, or restarting the quest.

print("Loading Adventure Game...")


def get_choice(prompt, valid_choices):
    """Keep asking until the player enters one of the valid_choices."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in valid_choices:
            return choice
        print(f"Please choose one of: {', '.join(valid_choices)}\n")


def forest_path(name):
    """Handles the forest scenario and its branching choices."""
    print(f"\n{name} steps into the dense, shadowy forest.")
    print("Sunlight barely breaks through the canopy above.")
    print("Ahead, you see a river gently flowing, and a tall old tree to climb.\n")

    choice = get_choice("Do you want to (river) or (tree)? ", ["river", "tree"])

    if choice == "river":
        print("\nYou follow the river and find a small wooden boat.")
        boat_choice = get_choice(
            "Do you (row) across or (walk) along the bank? ", ["row", "walk"]
        )
        if boat_choice == "row":
            print("\nYou row across and spot a glint of gold on the far bank.")
            print("You found the legendary TREASURE! You win!")
            return True
        else:
            print("\nWalking the bank, you slip on wet rocks and twist your ankle.")
            print("You can't continue the quest. You lose.")
            return False
    else:
        print("\nYou climb the tall tree for a better view.")
        tree_choice = get_choice(
            "Do you climb (higher) or climb back (down)? ", ["higher", "down"]
        )
        if tree_choice == "higher":
            print("\nFrom the treetop, you spot a hidden trail leading to a treasure chest!")
            print("You found the legendary TREASURE! You win!")
            return True
        else:
            print("\nYou climb down, but a branch snaps and you tumble to the ground.")
            print("Injured, you must abandon the quest. You lose.")
            return False


def cave_path(name):
    """Handles the cave scenario and its branching choices."""
    print(f"\n{name} steps into a cold, mysterious cave.")
    print("The air smells damp, and you can hear water dripping in the darkness.\n")

    choice = get_choice("Do you (torch) or go in the (dark)? ", ["torch", "dark"])

    if choice == "torch":
        print("\nWith the torch lit, you carefully make your way deeper.")
        step_choice = get_choice(
            "Do you (proceed) carefully or (rush) ahead? ", ["proceed", "rush"]
        )
        if step_choice == "proceed":
            print("\nYour careful steps lead you to a glittering treasure chest!")
            print("You found the legendary TREASURE! You win!")
            return True
        else:
            print("\nRushing ahead, you trigger a hidden trap and the ceiling collapses.")
            print("The quest ends here. You lose.")
            return False
    else:
        print("\nStumbling in the dark, you can barely see a few feet ahead.")
        step_choice = get_choice(
            "Do you keep (walking) or (turn) back? ", ["walking", "turn"]
        )
        if step_choice == "walking":
            print("\nYou fall into a hidden pit in the darkness.")
            print("The quest ends here. You lose.")
            return False
        else:
            print("\nYou turn back safely, but leave the cave without the treasure.")
            print("The quest ends here. You lose.")
            return False


def start_game():
    """Displays the introduction and lets the player choose their starting path."""
    print("=" * 50)
    print("      WELCOME TO THE QUEST FOR THE LOST TREASURE")
    print("=" * 50)
    name = input("\nWhat is your name, brave explorer? ").strip()
    if not name:
        name = "Explorer"

    print(f"\nWelcome, {name}! Legend tells of a treasure hidden in this ancient land.")
    print("Two paths lie before you: a dark forest and a mysterious cave.\n")

    path_choice = get_choice(
        "Which path do you choose? (forest) or (cave)? ", ["forest", "cave"]
    )

    if path_choice == "forest":
        return forest_path(name)
    else:
        return cave_path(name)


def main():
    """Runs the game loop, offering a restart after each attempt."""
    while True:
        won = start_game()
        if won:
            print("\nCongratulations! Your adventure ends in triumph!")
        else:
            print("\nBetter luck next time, adventurer.")

        play_again = get_choice("\nWould you like to play again? (yes/no) ", ["yes", "no"])
        if play_again == "no":
            print("\nThanks for playing. Farewell, explorer!")
            break


if __name__ == "__main__":
    main()
