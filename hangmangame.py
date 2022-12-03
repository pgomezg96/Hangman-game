import random

class Game:
    def HangmanGame():
        strickes = int(input('How many tries do you want? '))
        words_bank = ['face', 'pumpkin', 'rainbow', 'family', 'computer', 'swimming', 'brain', 'friendship']
        word = words_bank[random.randint(0, len(words_bank)-1)]
        progress = ['_' for i in range(len(word))]
        print(progress)
        while strickes > 0:
            shot = input('Make your shot! \n')
            if shot in word:
                for i in range(len(word)):
                    if shot == word[i]:
                            progress[i] = shot
            else:
                strickes -= 1
                print(f'Nop! you have {strickes} tries left')
            if '_' not in progress:
                strickes = -1
            print(f'{progress}\n')
        if strickes == -1:
            print('Congratulations! you saved a poor man from being hanged')
        else:
            print('Better luck next time! this man was hanged')
            print(f'The word was "{word}"')
            strickes = -1
   
Game.HangmanGame()
