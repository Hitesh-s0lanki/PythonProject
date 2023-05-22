import random
import os
def dashPrint(Answer):
    print("the word is :",end=" ")
    for i in Answer:
        print(i,end=" ")
    
    print("\n")

def checkWin(Amswer,index):
    if(index==0):
        return False
    for i in Answer:
        if '_' in i:
            return True
    return False

def checkLetter(a,word):
    for i in word:
        if a == i:
            return True
    return False


pattern=['''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
---------
---------''',
'''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
---------
---------''',
'''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
---------
---------''',
'''
    +---+
    |   |
    O   |
   /|   |
        |
        |
---------
---------''',
'''
    +---+
    |   |
    O   |
        |
        |
        |
---------
---------''',
'''
    +---+
    |   |
        |
        |
        |
        |
---------
---------'''
]
  
wordList=["hitesh","niraj","kapil"]

word=random.choice(wordList)
Answer=""
for i in range(len(word)):
    Answer+='_'

index=len(pattern)-1
dashPrint(Answer)
while(checkWin(Answer,index) and index!=0):
    a=input("Guess the Letter : ").lower()
    if(checkLetter(a,word)):
        newString=""
        AnswerIndex=0
        for i in word:
            if a == i:
                newString+=a
            else:
                newString+=Answer[AnswerIndex]
            AnswerIndex+=1
        Answer=newString
    else:
        print("Worng Letter")
        index=index-1
    os.system('cls')
    dashPrint(Answer)
    print(pattern[index])

if index==0:
    print("you Lose")
    print(f"the Right Answer is {word}")
else:
    print("You Won")
