import random

words = ["rahul","lahur","sawant","wasant","reshma","masher","vaibhavi","vivaibha",
         "rohit","hitro","minal","nilam","shwetali","litashwe","rutika","tikaru",
         "abhijit","bhijita"]
score=0

while True:
    letters = list(random.choice(words))
    l="".join(letters)
    print("guess the correct word :-> ", "".join(letters))
    user_word=input("Write a correct word or (quite the game) :->").lower()

    if user_word == 'quite' :
        break
    if user_word != l:
        valid = True
        for letter in user_word:
            if letter in letters:
                letters.remove(letter)
            else:
                valid= False
                break
        if valid and user_word in words:
            score = score + len(user_word)
            print(f"your score is :-> {score}")
        else:
            print("Wrong")
        if valid and user_word not in words:
            score=score-len(user_word)
            print(f"your score is deducted :-> {score}")
        else:
            print("score is same")
    else:
        print("you enter same word which I provided")
        
print("Thanks for playing game")












  
            
