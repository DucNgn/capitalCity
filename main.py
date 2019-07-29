import os, random

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


#Function to announce the correct answer
def answer(ctryName, captCity, correct):
    if correct is True:
        print('Congratulation, your answer is correct !')
        print(captCity + " is the capital city of " + ctryName)
    else:
        print('Your answer is incorrect')
        print(captCity + " is the capital city of " + ctryName)

#Display choices for user
def displayMultChoice(answerList):
    print('\n[A] ' + answerList[0] + '\n'
         '[B] ' + answerList[1] + '\n'
         '[C] ' + answerList[2] + '\n'
         '[D] ' + answerList[3] + '\n'    )

#Convert choice character to number
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



'''
  Start the quiz with differerent modes
  choice # 0 : search mode
  choice # 1 : guess capital city
  choice # 2 : guess the country name
  Multiple choice mode: True or False 
'''
def startQuiz(choiceNum, isMultChoice):
    
    #Enter Search mode
    if choiceNum == 0:
        print('Enter your search query: ')
        search = input()
        
        #Call support methods to search
        if searchCaptByCtry(search) is False and searchCtryByCapt(search) is False:
            print('No result found')
            return


    #Enter Quiz mode

    #Generate question and answer for the quiz
    ctryName = random.choice(list(ctryDict.keys()))
    captCity = ctryDict[ctryName]
            
    if isMultChoice is True:
        answerList = list()

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

            if answerList[choiceNo] == captCity:
                answer(ctryName, captCity, True)
                return True
            else:
                answer(ctryName, captCity, False)
                return False

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

            if answerList[choiceNo] == ctryName:
                answer(ctryName, captCity, True)
                return True
            else:
                answer(ctryName, captCity, False)
                return False

    else:
        #Generate random keys and values
        if choiceNum == 1:
            print('What is the capital city of ' + ctryName + " ?")
            keyIn = input()
            
            if keyIn.lower() == captCity.lower():
                answer(ctryName, captCity, True)
                return True
            else:
                answer(ctryName, captCity, False)
                return False
        
        if choiceNum == 2:
            print(captCity + " is the capital of which city ?")
            keyIn = input()
            if keyIn.lower() == ctryName.lower():
                answer(ctryName, captCity, True)
                return True
            else:
                answer(ctryName, captCity, False)
                return False

startQuiz(2, True)                