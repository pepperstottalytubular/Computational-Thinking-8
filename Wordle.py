import random

# Pick a word at random
word_list = ["aback","alloy","abate","acute","abbot","adage","abide","azure","abode","alone","bacon","brush","badly","burnt","baggy","broil","baler","bylaw","banal","buyer","cabal","cower","cabin","clamp","cacao","curry","cacti","cyber","cadet","cutie"]
hidden_word = random.choice(word_list)

# Repeat for 6 guesses
for i in range(6):
    # Guess a word
    guess_word = input()
    output = ""

    # First letter (in python, counting starts at 0 not 1)
    if guess_word[0] == hidden_word[0]:
        output += "🟩"
    elif guess_word[0] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    
# Result
    print(output)
    if output == "🟩🟩🟩🟩🟩":
        print("You win")
        break

    # Second letter (in python, counting starts at 0 not 1)
    if guess_word[1] == hidden_word[1]:
        output += "🟩"
    elif guess_word[1] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    
 # Result
    print(output)
    if output == "🟩🟩🟩🟩🟩":
        print("You win")
        break

    # Third letter (in python, counting starts at 0 not 1)
    if guess_word[2] == hidden_word[2]:
        output += "🟩"
    elif guess_word[2] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    
 # Result
    print(output)
    if output == "🟩🟩🟩🟩🟩":
        print("You win")
        break

    # Fourth letter (in python, counting starts at 0 not 1)
    if guess_word[3] == hidden_word[3]:
        output += "🟩"
    elif guess_word[3] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    
 # Result
    print(output)
    if output == "🟩🟩🟩🟩🟩":
        print("You win")
        break

    # Fifth letter (in python, counting starts at 0 not 1)
    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"


    # Result
    print(output)
    if output == "🟩🟩🟩🟩🟩":
        print("You win")
        break


print(f"You used {i+1} guesses")
