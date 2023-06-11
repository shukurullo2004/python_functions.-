from random_word import RandomWords

r = RandomWords()
word = r.get_random_word()

print("Welcome to the Word Guessing Game!")
print("Try to guess the word by entering one letter at a time.")
print("The word contains", len(word), "letters.")

guessed_letters = []
incorrect_guesses = 0

while True:
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "-"

    print("Current progress:", display)
    print("Incorrect guesses:", incorrect_guesses)

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You've already guessed that letter. Try again.")

    elif guess in word:
        guessed_letters.append(guess)
        if len(guessed_letters) == len(set(word)):
            print("Congratulations! You've guessed the word correctly:", word)
            break

    else:
        incorrect_guesses += 1
        print("Incorrect guess. Try again.")

        if incorrect_guesses >= 10:
            print("You've reached the maximum number of incorrect guesses.")
            print("The word was:", word)
            break







