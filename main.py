import random
from hangman_words import word_list
from hangman_art import stages, logo

chosen_word = random.choice(word_list)
word_len = len(chosen_word)
lives = 6

print(logo)

#Testing code
#print(f'the solution is {chosen_word}.')

#Blanks to show word list and generate blanks in display
display = []
for blank in range(word_len):
    display += "_"
print(display)


while "_" in display:
    guess = input('Guess a letter: ').lower()

    #Check if user type the same letter
    if guess in display:
      print(f"You've already guessed {guess}")

    #Check guessed letter
    for position in range(word_len):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter            
                

    
    #Check if user is wrong
    if guess not in chosen_word:
      print(f"You guessed {guess}, that's not in the word. You lose a live")
      
      lives -= 1
      if lives == 0:
          print('You Lose.')
          print(stages[lives])
          break
    
    #Join all the elements in the list and turn it into a String
    print(f"{' '.join(display)}")

    #Check if user has got all letter
    if not "_" in display:
        print('You Win!')
     
    print(stages[lives])