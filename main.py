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
def displayMultChoice(answerList, quest):
    print('The capital city of ' + quest + " is ?")
    print('\n[A] ' + answerList[0] + '\n'
         '[B] ' + answerList[1] + '\n'
         '[C] ' + answerList[2] + '\n'
         '[D] ' + answerList[3] + '\n'    )


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
    if isMultChoice is True:
        #Generate multiple choice answers
        choices = dict()
        for i in range(4):
            ctryName = random.choice(list(ctryDict.keys()))
            captCity = ctryDict[ctryName]
            #If the city name is already in the dict
            if ctryName in choices:
                i = i - 1
            else:
                choices.setdefault(ctryName, captCity)

        if choiceNum == 1:
            #Quest: Country name
            quest = random.choice(list(choices.keys()))
            displayMultChoice(list(choices.values()), quest)

            while True:
                keyIn = input()
                convertChar = -1
                if   keyIn.lower() == 'a':
                    convertChar = 0
                    break
                elif keyIn.lower() == 'b':
                    convertChar = 1
                    break
                elif keyIn.lower() == 'c':
                    convertChar = 2
                    break
                elif keyIn.lower() == 'd':
                    convertChar = 3
                    break
                else:
                    print('Invalid input. Try again')
            
            if list(choices.keys)[convertChar] == quest:
                print('Congratulation')
                

            
    else:
        #Generate random keys and values
        ctryName = random.choice(list(ctryDict.keys()))
        captCity = ctryDict[ctryName]
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

startQuiz(1, True)                