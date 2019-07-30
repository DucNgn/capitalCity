import os, random, time
from selenium import webdriver

#------------------process the csv file -----
ctryListObj = open('country-list.csv')

#The structure of content in the file
structure = '"country","capital","type"'
content = ctryListObj.read()
listCountries = content.split('\n')

ctryDict = dict()

def make_Keys_Values(element):
    temp = element.split(',')
    keys_Value = [temp[0].replace('\"', ''), temp[1].replace('"', '')]
    return keys_Value

for each in listCountries:
    if each != structure:
        keys_Value = make_Keys_Values(each)
        ctryDict.setdefault(keys_Value[0], keys_Value[1])

#------finish processing the csv file -----

'''
  Start the quiz with differerent modes
  choice # 0 : search mode
  choice # 1 : guess capital city
  choice # 2 : guess the country name
  Multiple choice mode: True or False 
'''
def newSession(choiceNum, isMultChoice):
    #clear screen
    os.system('clear')
    print('Session starts')
    
    #Enter Search mode
    if choiceNum == 0:
        print('Enter your search query: ')
        search = input()
        
        #Call support methods to search
        if searchCaptByCtry(search) is False and searchCtryByCapt(search) is False:
            print('No result found')
            return

    #Enter Quiz mode

    #Generate question and answer for the quiz mode
    ctryName = random.choice(list(ctryDict.keys()))
    captCity = ctryDict[ctryName]
            
    if isMultChoice is True:
        answerList = list()
        
        #Guess capital city by country name
        if choiceNum == 1:

            for i in range(4):
                tempCity = random.choice(list(ctryDict.values()))
                if tempCity == captCity or tempCity in answerList:
                    i = i - 1
                else:
                    answerList.append(tempCity)
            
            #Append the right answer
            answerList[random.randint(0, 3)] = captCity

            #Prompt
            print('What is the capital city of ' + ctryName + " is ?")
            displayMultChoice(answerList)

            choiceNo = -1
            while True:
                keyIn = input()
                choiceNo = convertChoice(keyIn)
                if  choiceNo == -1:
                    print('Invalid input')
                else:
                    break

            return evaluate(ctryName, captCity, True, answerList[choiceNo])

        #Guess country name by capital city        
        else:
            for i in range(4):
                tempCtry = random.choice(list(ctryDict.keys()))
                if tempCtry == ctryName or tempCtry in answerList:
                    i = i - 1
                else:
                    answerList.append(tempCtry)

            #Append the right answer
            answerList[random.randint(0, 3)] = ctryName

            #Prompt
            print(captCity + " is the capital city of which country?")
            displayMultChoice(answerList)

            choiceNo = -1
            while True:
                keyIn = input()
                choiceNo = convertChoice(keyIn)
                if  choiceNo == -1:
                    print('Invalid input')
                else:
                    break

            return evaluate(ctryName, captCity, False, answerList[choiceNo])
    
    #Multiple choice mode off
    else:
        #Guess capital city by country name
        if choiceNum == 1:
            print('What is the capital city of ' + ctryName + " ?")
            keyIn = input()
            
            return evaluate(ctryName, captCity, True, keyIn)
        
        #Guess country name by capital city
        if choiceNum == 2:
            print(captCity + " is the capital of which city ?")
            keyIn = input()
            
            return evaluate(ctryName, captCity, False, keyIn)

#---------------------Support methods in 1 session-----------------

#-----------SUPPORT FOR SEARCH MODE --------------------
#Search country name by capital name and display results
def searchCtryByCapt(captCity):
    result = list()
    for ctry, city in ctryDict.items():
        if city.lower() == captCity.lower():
            result.append(ctry)
    
    if len(result) == 0:
        return False
    else:
        for each in result:
            print("The capital city of the country " + each + " is the city of " + ctryDict[each])
            getDetails(each)
            getDetails(ctryDict[each])


#Search capital name by country name and display results
def searchCaptByCtry(ctryName):
    result = list()
    for ctry, city in ctryDict.items():
        if ctry.lower() == ctryName.lower():
            result.append(ctry)
        
    if len(result) == 0:
        return False
    else:
        for each in result:
            print("The capital city of the country " + each + " is the city of " + ctryDict[each])
            getDetails(each)
            getDetails(ctryDict[each])
#-------------------------------------------------------


#--------------------SUPPORT FOR QUIZ MODE -----------------------------
#DISPLAY CHOICES IN MULTIPLE CHOICE MODE
def displayMultChoice(answerList):
    print('\n'  +
         '[A] ' + answerList[0] + '\n'
         '[B] ' + answerList[1] + '\n'
         '[C] ' + answerList[2] + '\n'
         '[D] ' + answerList[3] + '\n'    )

#CONVERT CHOICE INPUT TO CORRESPOND NUMBER FOR MULTIPLE CHOICE MODE
def convertChoice(keyIn):
    if keyIn.lower() == 'a':
        return 0
    elif keyIn.lower() == 'b':
        return 1
    elif keyIn.lower() == 'c':
        return 2
    elif keyIn.lower() == 'd':
        return 3
    else: #Invalid input
        return -1


#EVALUATE USER'S ANSWER
def evaluate(ctryName, captCity, guessCapt, answer):
    #Guessing capital city
    if guessCapt is True:
        if answer.lower() == captCity.lower():
            announce(ctryName, captCity, True)
            return True
        else:
            announce(ctryName, captCity, False)
            return False
    
    #Guessing country name
    else: 
        if answer.lower() == ctryName.lower():
            announce(ctryName, captCity, True)
            return True
        else:
            announce(ctryName, captCity, False)
            return False


#ANNOUNCEMENT
def announce(ctryName, captCity, correct):
    if correct is True:
        print('\nCongratulation, your answer is CORRECT !')
        print(captCity + " is the capital city of " + ctryName)
    else:
        print('\nYour answer is INCORRECT')
        print(captCity + " is the capital city of " + ctryName)
    
    #Wiki request
    getDetails(ctryName)
    getDetails(captCity)

#-------END OF SUPPORTS FOR QUIZ MODE -------------------

def getDetails(location):
    print('\nDo you want to know more detail about ' + location + " ?")
    print('[Y] Yes      [other] No')
    keyIn = input()
    if keyIn.lower() == 'y':
        wiki(location)


#GET MORE DETAILS OF THE PLACE ON WIKIPEDIA
def wiki(location):
    print('Directing to Wikipedia')
    url = 'https://en.wikipedia.org/wiki/' + location
    browser = webdriver.Chrome()
    browser.get(url)
    time.sleep(10)

#--------------END of Support methods in 1 session

#DRIVER METHOD
def Start():
    #___INIT___ 
    total = 0
    #total number 
    correctTotal = 0
    falseTotal = 0

    while True:
        #WELCOME MESSAGE
        os.system('clear')
        os.system('figlet Capital Cities')
        print('Author: Duc Nguyen @2019'.rjust(70))
        print('All rights reserved.'.rjust(70) + '\n')
        print('[1] [Quiz mode]     [2][Multiple choice questions]     [3]Search mode   [4] Exit')
        keyIn = input()

        '''
        Result of each round
        0: search mode
        True: correct answer
        False: wrong answer
              init with 0
        '''
        result = 0

        if keyIn == '1':
            print('Preparing Quiz mode')
            result = newSession(guessCapt(),False)
        elif keyIn == '2':
            print('Preparing multiple choice questions')
            result = newSession(guessCapt(), True)
        elif keyIn == '3': #SEARCH MODE
            newSession(0, False)
        elif keyIn == '4':
            finalScore(total, correctTotal, falseTotal)
        else:
            print('Invalid input. Try again')

        if result is True:
            correctTotal = correctTotal + 1
        elif result is False:
            falseTotal = falseTotal + 1

        #Recalculate the total score
        total = correctTotal - falseTotal

        #Clear screen after 1 session
        os.system('clear')
        

#DETERMINE MODE
def guessCapt():
    print('[Y]Guess capital city by country name      [other]Guess country name by capital city')
    keyIn = input()

    if keyIn.lower() == 'y':
        return 1   #Guess capital name
    else:
        return 2   #Guess country name


def finalScore(total, correctTotal, falseTotal):
    os.system('clear')
    os.system('figlet total score:   ' + str(total))
    print('Number of correct answers: ' + str(correctTotal))
    print('Number of wrong answers: ' + str(falseTotal))
    print('Game ended')
    exit(0)

Start()