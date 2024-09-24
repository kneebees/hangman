## HANGMAN GAME
# imports random
import random
win = False
words = ['BUMBLEBEE', 'FILLET', 'ONION', 'ELEVATOR', 'MACHINE', 'MARKERS', 'PROTRACTOR', 'CABBAGE', 'BROCCOLI', 'MANSION', 'KIDNEY', 'RANDOM', 'DESPICABLE', 'AVALANCHE', 'PUNCTUATION', 'EXCLAMATION', 'QUESTION', 'ALUMINUM', 'METABOLISM', 'TOOTHBRUSH', 'BINDER', 'CALENDAR', 'NOTORIOUS', 'MATHEMATICS', 'MONITORED', 'JIGSAW', 'RAINBOW', 'CUCUMBER', 'ULTRAVIOLET', 'ANIMATION', 'BALD', 'MUSTACHE', 'JUMBLED', 'SCRAMBLED', 'DISASTROUS', 'ERASER', 'EXPLOSION', 'ESPIONAGE', 'LANGUAGE', 'SUPERHERO', 'SITUATION', 'NAVIGATOR', 'CLIPBOARD', 'OLYMPIAN', 'PROGRESSIONS', 'SPLENDID', 'ACADEMY','WOLVERINES']

def choose(words):
  global word
  global word_
  word = random.choice(words)
  word_ = ' '.join(word)

def intro():
  name = input("What is your name? ").capitalize()
  print("\n Hello, {}. Welcome to Hangman, a game where you have to guess the letters in a word or just the word itself. You have as many  lives as the hangman has body parts (e.g. 1 arm = 1 life). Once you input the correct letter, the blank spaces with that letter will be replaced by your guess. Have fun.".format(name))

def blan():
  global blank
  choose(words)
  i = 0
  blank = []
  for i in range(0, len(word)):
    blank.append('_')
    print("_ ", end='')

lives = 6
life =  '  ____\n |    |\n |    \n |\n---'
life1 = '  ____\n |    |\n |    o\n |\n---'
life2 = '  ____\n |    |\n |    o\n |   /\n |\n---'
life3 = '  ____\n |    |\n |    o\n |   /|\n |\n---'
life4 = '  ____\n |    |\n |    o\n |   /|\ \n |\n---'
life5 = '  ____\n |    |\n |    o\n |   /|\ \n |  _/\n---'
life6 = '  ____\n |    |\n |    o\n |   /|\ \n |  _/ \_\n---'
hangman = [life, life1, life2, life3, life4, life5, life6]
x = 0
guesses = []

def game(blank, word, x, lives, guesses):
  while lives == 1 or lives == 2 or lives == 3 or lives == 4 or lives == 5 or lives == 6:
    try: 
      lette = input("\n\nWould you like to guess the letter or the word? ").lower()
      if lette == "letter" or lette == "l":
        guess = input("What letter do you think is in this word? ").upper()
        y = 0
        if len(guess) == 1 and guess not in guesses:
          guesses.append(guess)
          for i in range(0, len(word)):
            if guess in word[y]:
              blank.pop(y)
              blank.insert(y, guess)
            elif guess not in word:
              x += 1
              lives -= 1
              break
            y += 1
          blank = ' '.join(blank)
          if blank == word_:
            print(hangman[x])
            print(word_)
            print("Congratulations. You won")
            break
          print(hangman[x])
          print(blank)
          blank = ''.join(blank)
          blank = ' '.join(blank)
          blank = blank.replace(' ', '')
          blank = list(blank)
          guesses = ', '.join(guesses)
          print("Your guesses so far: {}.".format(guesses))
          guesses = guesses.replace(', ', '')
          guesses = list(guesses)
        elif len(guess) > 1 or len(guess) < 1:
          print("Write one letter.")
        elif guess in guesses:
          print("You've already guessed this.")
      elif lette == "word" or lette == "w":
        guess = input("What word do you think this is? ").upper()
        if len(guess) > 1 and guess not in guesses:
          guesses.append(guess)
          if guess == word:
            print(hangman[x])
            print(word_)
            print("Contratulations. You win.")
            break
          elif guess not in word:
            x += 1
            blank = ' '.join(blank)
            print(hangman[x])
            print(blank)
            blank = ' '.join(blank)
            blank = blank.replace(' ', '')
            blank = list(blank)
            guesses = ', '.join(guesses)
            print("Your guesses so far: {}.".format(guesses))
            guesses = guesses.replace(', ', '')
            guesses = list(guesses)
            lives -= 1
        elif len(guess) <= 1:
          print("Write a word. ")
        elif guess in guesses:
          print("You've already guessed this. ")
    except:
      print("Your answer is not valid. Try again.")
  else:
    print("You lost. The answer was {}.".format(word_))
    
intro()
blan()
game(blank, word, x, lives, guesses)
