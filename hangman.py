import random, hangman_stages,sys,print_word
print("Welcome to Hangman!! Let's see if you can guess this word\n")
dic=["tiger","mouse","cake","friends","team"]
hints=["This animal has stripes.",
       "A small animal with long tail and it loves cheese.",
       "A sugary delight which is a mandatory part of every celebration.",
       "A group of people closest to us.",
       "A group of people who tackle a task together."]
def hint(hints):
    if word==dic[0]:
        return hints[0]
    elif word==dic[1]:
        return hints[1]
    elif word==dic[2]:
        return hints[2]
    elif word==dic[3]:
        return hints[3]
    elif word==dic[4]:
        return hints[4]
def select_word(dic):
    return random.choice(dic)

word=select_word(dic)

print(hint(hints))
print(len(word)*"_ ")

remaining_attempt=6
guessed_letters=""
print(hangman_stages.get_hangman(remaining_attempt))
print(select_word)

def is_guess_in_secret_word(guess,word):
    if len(guess)>1 or not guess.isalpha():
        print("ERROR: Only single letters are allowed at a time. RESTART")
        sys.exit()
    else:
        if guess in word:
            return True
        else:
            return False

def get_unique_letters(dic):
    return "".join(set(dic))

while remaining_attempt>0 and len(guessed_letters)<len(get_unique_letters(word)):
    guess=input("Guess a letter:")
    guess_in_secret_word=is_guess_in_secret_word(guess,word)
    if guess_in_secret_word:
        if guess in guessed_letters:
            print("You have already guessed the letter {}".format(guess))
        else:
            print("Yess!! The letter {} is part of the secret word".format(guess))
            guessed_letters+=guess
    else:
        print("No! The letter {} is not part of the secret word".format(guess))
        remaining_attempt-=1
    
    print(hangman_stages.get_hangman(remaining_attempt))
    print("\n{} ateempts remaining.\n".format(remaining_attempt))
    print_word.print_secret_word(word,guessed_letters)
    print("{} Letters guessed so far.\n".format(len(guessed_letters)))
    
if len(guessed_letters)==len(word):
    print("Wohooo!!You guessed it right. You Win!!")
else:
    print("Better Luck next time!!")