import random
word_list = ["one", "two", "three"]
computer_guess = random.choice(word_list)
character_count = len(computer_guess)
print("Guess the word:", end= "")
character_tracking = []

while character_count:
    character_tracking.append("_")
    character_count = character_count - 1
    #print("_", end= "")


while len(computer_guess):
    index = 0
    #print(len(computer_guess))
    print(character_tracking)
    user_guesses = input('\nPlease enter your guess: ')

    #print(user_guesses)
    flag = 0
    for elements in computer_guess:
        #print(elements)

        if user_guesses == elements:
            print("Found it! ")
            flag = 1
            #character_tracking.insert(index,user_guesses)
            character_tracking[index] = user_guesses
            #computer_guess = computer_guess.replace(elements, "")

            #break

        index = index + 1
    if flag != 1:
        print("Letter not found.Try again.")


