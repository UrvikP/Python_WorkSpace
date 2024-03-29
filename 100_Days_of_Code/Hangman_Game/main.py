import random
import hangman_art
import hangman_words

print('''
-------------------------------------------------------------------------------------------------
_________________________________________________________________________________________________
|  |   |  |       ____       |  \   |  | |  _________|  |  \    /  |       ____       |  \   |  |
|  |   |  |      / __ \      |   \  |  | |  |           |   \  /   |      / __ \      |   \  |  |
|  |___|  |     / /  \ \     |    \ |  | |  |   ______  |    \/    |     / /  \ \     |    \ |  |
|   ___|  |    / /____\ \    |     \|  | |  |   |__  |  |  |\  /|  |    / /____\ \    |     \|  |
|  |   |  |   /  ______  \   |  |\     | |  |     |  |  |  | \/ |  |   /  ______  \   |  |\     |
|  |   |  |  /  /      \  \  |  | \    | |   \____|  |  |  |    |  |  /  /      \  \  |  | \    |
|__|   |__| /__/        \__\ |__|  \___|  \__________/  |__|    |__| /__/        \__\ |__|  \___|
-------------------------------------------------------------------------------------------------
''')
chosen_word = random.choice(hangman_words.word_list)

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')
# For each letter in the chosen_word, add a "_" to 'display'.
display = []
for letter in chosen_word:
    display.append("_")

tries = len(hangman_art.stages) - 1

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    while guess in display:
        guess = input(
            "You've already guessed this letter correctly. Choose another letter: ")

    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess

    if guess not in chosen_word:
        print(
            f"You guessed {guess}, that's not in the word. You lose a life.")
        tries -= 1
    if tries == 0:
        print("You Lose.")
        end_of_game = True

    print(f"{' '.join(display)}")
    print(hangman_art.stages[tries])
    if "_" not in display:
        print("You win!")
        end_of_game = True
