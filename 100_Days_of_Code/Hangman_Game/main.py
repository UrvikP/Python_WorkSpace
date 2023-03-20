import random
import hangman_art
import hangman_words


chosen_word = random.choice(hangman_words.word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
for letter in chosen_word:
    display.append("_")

tries = len(hangman_art.stages) - 1
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess

    if guess not in chosen_word:
        tries -= 1
    if tries == 0:
        print("You Lose.")
        end_of_game = True
        # Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
    print(display)
    print(hangman_art.stages[tries])
