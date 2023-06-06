def print_secret_word(word,guessed_letters):
    for letter in word:
        if letter in guessed_letters:
            print(" {} ".format(letter),end="")
        else:    
            print("_ ",end="")
    print("\n")