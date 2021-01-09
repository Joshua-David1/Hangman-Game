import random

words = ['algeria', 'albania', 'australia', 'bulgaria', 'bhutan', 'india', 'ireland', 'zimbabwe', 'namibia', 'nigeria',
         'england', 'china', 'japan', 'jamica', 'iceland']
print("\nHANGMAN GAME\n")
picked_word = random.choice(words)
blanks = []
hangman_doll_list = [
    ' -----\n |   |\n     |\n     |\n     |\n     |\n -----\n',
    ' -----\n |   |\n O   |\n     |\n     |\n     |\n -----\n',
    ' -----\n |   |\n O   |\n |   |\n     |\n     |\n -----\n',
    ' -----\n |   |\n O   |\n\|   |\n     |\n     |\n -----\n',
    ' -----\n |   |\n O   |\n\|/  |\n     |\n     |\n -----\n',
    ' -----\n |   |\n O   |\n\|/  |\n |   |\n     |\n -----\n',
    ' -----\n |   |\n O   |\n\|/  |\n |   |\n/    |\n -----\n',
    ' -----\n |   |\n O   |\n\|/  |\n |   |\n/ \  |\n -----\n'
]
print(hangman_doll_list[0])
word_length = len(picked_word)
blank_count = word_length
for word in picked_word:
    blanks.append('_')

for blank in blanks:
    print(blank, end=' ')

print('\n\n')
print("A random word has been picked\n\n")
lives = 7
life_safe = False
while (lives > 0):
    guess_word = input("Guess word: ").lower()
    print("\n----------------------\n")

    for position in range(len(picked_word)):

        if guess_word == picked_word[position]:
            blanks[position] = guess_word
            blank_count -= 1
            life_safe = True
    if (not life_safe):
        lives -= 1
        print(f"Wrong guess!!.\t\t\t\tLives: {lives}\n")
    else:
        print(f"\t\t\t\t\tLives: {lives}\n")
    life_safe = False

    print(end='\n\n')
    print(hangman_doll_list[7 - lives])
    print("\n")
    for blank in blanks:
        print(blank, end=' ')
    print("\n\n")
    if (blank_count == 0):
        break
if blank_count > 0:
    print(f"You lost\nThe actual word was {picked_word}")
else:
    print(f"You won with {lives} lives remaining")