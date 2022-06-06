import random
list_words=[]

with open('wordle.txt') as f:
     a = 0
    for line in f:
        l=line.strip()
        list_words.append(1)
answer = list_words[random.randrange(2315)]

for i in range (0,6):
    guess=input("Guess a 5 letter word: ")
    if answer == guess:
        print("Yippee")
        break
    for j in range(2315):
        if(guess== list_words[j]):
            a = a+ 1
        if(a>0):
            print("wrong answer")
        else:
            print("Invalid word, guess again")
            r = r + 1
    print(answer)
f.close()
