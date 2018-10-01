secretWord = 'bananas'
guessingWord = '_' * len(secretWord)


def guess(letter):  # function to loop through the secretWord and repalce the '_' of guessingWord
    count = 0
    for i in secretWord:
        if i == letter:
            global guessingWord
            # Line that refers to the changing of _ into the correct letter
            guessingWord = guessingWord[:count] + letter + guessingWord[count + 1:]
        count += 1


while '_' in guessingWord:
    playerGuess = input('Guess a character: ').lower()
    if len(playerGuess) == 1:
        guess(playerGuess)
    else:
        print('Please guess one letter!')
    print(guessingWord)


print('Nice job guessing the word %s!' % secretWord)
