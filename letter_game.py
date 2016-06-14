# Python-exercise 'Letter Game'
# Done by timosarkka
# Import Python 3.0 print functions
# Import random library for random number generation
# Import os for building 'clear screen'-function
# Import sys for enabling a structured exit
from __future__ import print_function
import random
import os
import sys

# Creates a list of words to be used by the app
# Opens up a file, the "Oxford English Dictionary" and reads all the lines for words
# Splits them up and appends them to the list 'words'.
words = []
wordlist = open('largelist.txt', 'r')
for word in wordlist.read().split():
	words.append(word)

# A function to clear the screen
# If the operating system is Windows or equivalent (nt), use command cls
# In other cases, use clear
def clear():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

# A function to display the lines, if the guess was wrong; or display the letters, if the guess was right
# Strikes displays the number of bad_guesses using length of list 'bad_guesses'
# Note that the bad_guesses and good_guesses are empty lists at first, which get appended with the guesses by the player
# Note that secret_word is a string which gets looped through for every letter and searched for the right letters
def draw(bad_guesses, good_guesses, secret_word):
	clear

	print('Strikes: {}/20'.format(len(bad_guesses)))
	print('')
	
	for letter in bad_guesses:
		print(letter,end=' ')
	print('\n\n')
	
	for letter in secret_word:
		if letter in good_guesses:
			print(letter,end='')
		else:
			print('_',end='')
			
	print('')

# A function to get a guess from the player
# Runs an infinite while-loop
# Checks first, that the player is not trying to use multiple letters,
# not trying to guess an already used letter and that the symbol guessed is actually a letter
# If all of that checks out, the function returns the players guess
def get_guess(bad_guesses, good_guesses):
	while True:
		guess = raw_input("Guess a letter: ").lower()
		if len(guess) != 1:
			print("You can only guess a single letter!")
		elif guess in bad_guesses or guess in good_guesses:
			print("You've already guessed that letter!")
		elif not guess.isalpha():
			print("You can only guess letters!")
		else:
			return guess

# The *actual* game function
# Clears the screen first
# Takes out a random word from the list of words
# Initializes the bad and good guesses lists
def play(done):
	clear()
	secret_word = random.choice(words)
	bad_guesses = []
	good_guesses = []
	
	# The game loop begins
	# First the draw function is used to display the starting state = empty lines
	# A guess is gotten from the player
	while True:
		draw(bad_guesses, good_guesses, secret_word)
		guess = get_guess(bad_guesses, good_guesses)
		
		# If the letter is found from the secret_word string, the list of good guesses is appended by that letter
		# At the same time, variable found is set to True
		# If there is still a letter missing from the good_guesses list, the game will continue
		# If all the letters are there, a win message is displayed and the variable done is set to True
			# If done is True, the player will be asked whether or not to play again. If the choice is yes, play()-function is repeated.
			# If not, the program is terminated.
		# Else, the letter is added to the list of bad_guesses. If the amount of bad guesses is equal to 20, the game will terminate.
		# The done-sequence is called in this case too.
		if guess in secret_word:
			good_guesses.append(guess)
			found = True
			for letter in secret_word:
				if letter not in good_guesses:
					found = False
			if found:
				print("You win!")
				print("The secret word was {}".format(secret_word))
				done = True
		else:
			bad_guesses.append(guess)
			if len(bad_guesses) == 20:
				draw(bad_guesses, good_guesses, secret_word)
				print("You lost!")
				print("The secret word was {}".format(secret_word))
				done = True
		
		if done:
			play_again = raw_input("Play again? Y/n ").lower()
			if play_again != 'n':
				return play(done=False)
			else:
				sys.exit()

# A function to verify that the player really wants to start the game. If not, the program will terminate.
# Exit is carried out with sys.exit()
# variable done is initialized to be 'False' so that the game loop can go on.
def welcome():
	print('Welcome to Letter Guess!')
	start = raw_input("Press Enter to start or Q to quit. ").lower()
	if start == 'q':
		print("Bye!")
		sys.exit()
	else:
		return True

done = False

while True:
	clear()
	welcome()
	play(done)