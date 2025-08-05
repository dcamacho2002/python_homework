def make_hangman(secret_word):
    guesses = []
    def hangman_closure(letter):
        guesses.append(letter.lower())
        result = ""
        for character in secret_word:
            if character.lower() in guesses:
                result += character
            else:
                result += "_"
        print(result)
        for character in secret_word:
            if character not in guesses:
                return False
        return True
    return hangman_closure

word = input("Enter a secret word: ")
hangman = make_hangman(word)
while True:
    guessLetter = input("Guess a letter: ")
    if hangman(guessLetter): 
        print(f"You guessed the word: {word}")
        break
