
# uses dictionary for flashcard game

import random
from random import randint

identDict={
    "y=cot(x), y'=?":"-csc^2(x)",
    "y=tan(x), y'=?":"sec^2(x)",
    "y=cos(x), y'=?":"-sin(x)",
    "y=sin(x), y'=?":"cos(x)",
    "1+cot^2(x)=?":"cos^2(x)",
    "tan^2(x)+1=?":"sec^2(x)",
    "sin^2(x)+cos^2(x)=?":"1",
    "lim x->0 {(cos(x)-1)/(x)}=?": "0",
    "lim x->0 {(sin(x)/(x)}=?": "1",
    "ln(e^-1)=?": "-1",
    "ln(e)=?":"1",
    "ln(1)=?":"0",
    "e^0=?":"1",
    "y=sec(x), y'=?":"sec(x)tan(x)",
    "y=csc(x), y'=?":"-csc(x)cot(x)",      
    }
print("Trig Identity Quiz! Good Luck! \n")

#shuffles dictionary keys and creates list of questions and answers for test iteration
identList = list(identDict.keys())
random.shuffle(identList)

#score board
correct = 0
total = 0

#iterates through list of identities
for x in range(0,(len(identDict))):

    #identifies question and answer
    question=identList[x]
    answer=identDict[identList[x]]

    # creates random answer choices
    randomAnswer1=(randint(0,len(identDict)-1))
    randomAnswer2=(randint(0,len(identDict)-1))
    randomAnswer3=(randint(0,len(identDict)-1))


    # ensures no duplicate answer choices
    while identDict[identList[randomAnswer1]] == answer:
        randomAnswer1=(randint(0,len(identDict)-1))
    while identDict[identList[randomAnswer2]] == identDict[identList[randomAnswer1]]:
        randomAnswer2=(randint(0,len(identDict)-1))
    while identDict[identList[randomAnswer3]] == identDict[identList[randomAnswer2]]:
        randomAnswer3=(randint(0,len(identDict)-1))

    #creates answer bank
    answerList=[
        answer,
        identDict[identList[randomAnswer1]],
        identDict[identList[randomAnswer2]],
        identDict[identList[randomAnswer3]],
    ]
    
    #shuffles answer bank
    random.shuffle(answerList)

    #assigns answers to letter value
    answerDict={
        ("A"):answerList[0],
        ("a"):answerList[0],
        ("B"):answerList[1],
        ("b"):answerList[1],
        ("C"):answerList[2],
        ("c"):answerList[2],
        ("D"):answerList[3],
        ("d"):answerList[3],
        }
    
    # prints question and answer bank 
    print("Evaluate: ", question)
    print("\n(A)", answerList[0])
    print("(B)", answerList[1])
    print("(C)", answerList[2])
    print("(D)", answerList[3])

    #takes user input and stores value in userAnswer
    userAnswer= input("\nSelect the correct answer: ")
    
    #evaluates answer, tallys score per iteration, and displays message
    if answerDict[userAnswer]== answer:
        correct+=1
        total+=1
        print("\nNice work!")
        print("Your score it", correct, "/", total,"\n")
    else:
        total+=1
        print("Oops. You missed one.\n")
        print("The correct answer was ", answer)
        print("Your score is", correct, "/", total,"\n")

#calculates final score and displays message 
score=correct/total*100
print("You finished the quiz.")
if score>=90:
    print("You're an expert. Take a break!")
elif score<90 and score>=80:
    print("You're doing great. Keep studying!")
elif score<80 and score>=75:
    print("Not so hot, but you'll get there.")
else:
    print("You might have to pull an all nighter to catch up...")    
print("Your score is ", score)






























