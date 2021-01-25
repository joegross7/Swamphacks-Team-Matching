import csv
import operator
import math
import random 

class Student:
     def __init__(self, name, email, experienceLvl,  teammatesNum, language, projectType):
        self.name = name
        self.email = email
        self.experienceLvl = experienceLvl
        self.teammatesNum = (teammatesNum)
        self.language = language
        self.projectType = projectType
        self.groupList = []
        self.previousTeammatesList = []       
        self.groupChoiceList = []
        self.assignedGroup = None


class Groups:
    def __init__(self, student, groupNum):
        self.groupNum = groupNum
        self.studentList = [student]
        self.experienceLvl = student.experienceLvl;
        self.language = student.language
        self.numStudent = student.teammatesNum
        student.groupList.append(self)
        self.projectType = student.projectType
        self.round = -1

    def AddStudent(self, student):
        self.studentList.append(student)
        self.numStudent += student.teammatesNum
        student.groupList.append(self)

    def removeStudents(self):
        for student in self.studentList:
            student.groupList.remove(self)
        studentList = []

        

class GroupsList:
    def __init__(self, groupList):
        self.groupList = groupList
        self.cu

def addUniqueToArray(arr, element):
    for e in arr:
        if e == element:
            return
        
    arr.append(element)
    return        

def teamMatchingAlgorithm(studentList):
    groupMaxNum = 4
    #sort langugages into an dict. put students into separate language groups
    # languageDict = {}
    # projectDictDict = {}
    # for student in studentList:
    #     templanguageGroup = languageDict.get(student.language)
    #     if templanguageGroup == None:
    #         languageDict[student.language] = Groups(student,0)
    #     else:
    #         templanguageGroup.AddStudent(student)

    #sort langugages into an dict. put students into separate exp level groups
    expLvlDict = {}
    projectDictDict = {}
    for student in studentList:
        tempExpLvlGroup = expLvlDict.get(student.experienceLvl)
        if tempExpLvlGroup == None:
            expLvlDict[student.experienceLvl] = Groups(student,0)
        else:
            tempExpLvlGroup.AddStudent(student)
    

    for expLvl in expLvlDict:
        projectDict = {}
        for student in expLvlDict[expLvl].studentList:
            tempProjectGroup = projectDict.get(student.projectType)
            if tempProjectGroup == None:
                projectDict[student.projectType] = Groups(student,0)
            else:
                tempProjectGroup.AddStudent(student)
        projectDictDict[expLvl] = projectDict        





    
    #sort into language groups
    threeCount = 0
    oneCount = 0
    totalStudentCount = 0      

    teamMatchingArray = []
    maxRounds = 3

    expLvlGroupList = []

    for s in studentList:
        s.groupList = []    

    for roundCounter in range(maxRounds):
        groupCounter = 1
        unplacedStudents = []
        for expLvl in projectDictDict:
            for project in projectDictDict.get(expLvl):
                expLvlAndProjectGroup = projectDictDict[expLvl].get(project)
                #get total number of students
                studentSum = 0
                threeCount = 0
                for student in expLvlAndProjectGroup.studentList:
                    studentSum += student.teammatesNum
                    totalStudentCount += student.teammatesNum
                    if student.teammatesNum == 3:
                        threeCount += 1
                    if student.teammatesNum == 1:
                        oneCount += 1    
                groupList = []
                matchingCriteria
                for student in expLvlAndProjectGroup.studentList:
                    group = Groups(student, groupCounter)
                    for teammate in expLvlAndProjectGroup.studentList:
                        if teammate != student and len(student.groupList) == roundCounter + 1 and len(student.groupList) < maxRounds:
                            #check if the students have already been together 
                            haveBeenTogether = False
                            for studentsInGroup in group.studentList:
                                for previousTeammates in studentsInGroup.previousTeammatesList:
                                    if previousTeammates == teammate:
                                        haveBeenTogether = True
                            if group.numStudent + teammate.teammatesNum <= groupMaxNum and haveBeenTogether == False and len(teammate.groupList) < maxRounds:
                                for studentsInGroup in group.studentList:
                                    teammate.previousTeammatesList.append(studentsInGroup)
                                    studentsInGroup.previousTeammatesList.append(teammate)
                                group.AddStudent(teammate)
                    if len(group.studentList) > 1 and group.numStudent > 2:
                        groupCounter += 1
                        groupList.append(group)
                        group.round = roundCounter
                    else:
                        group.removeStudents()

                expLvlGroupList += groupList

                #divide total students by 4 to get number of 4 person groups. also get remainder for extra group
               


        #languagegrouplist[0].sort(key=operator.attrgetter("groupnum"))
        #languagegrouplist[1].sort(key=operator.attrgetter("groupnum"))
        #languagegrouplist[2].sort(key=operator.attrgetter("groupnum"))


        #for lgl in languagegrouplist:
        #        for g in lgl:
        #            temph = []
        #            for s in g.studentlist: 
        #                temp = []
        #                temp.append((str)(s.name))
        #                temp.append((str)(g.groupnum))
        #                temp.append((str)(s.language))
        #                temp.append((str)(g.experiencesum))
        #                temp.append((str)(s.experiencelvl))
        #                temp.append((str)(g.numstudent))
        #                teamMatchingarray.append(temp)   
        #
                        
    groupArr = languageGroupList

    groupArr.sort(key=operator.attrgetter("groupNum"))

    groupPrintArr = []
    
    for group in groupArr:
        c = 0
        groupPrintArr.append(group.groupNum)
        for s in group.studentList:
            groupPrintArr.append((str)(s.name) + " (" + (str)(s.teammatesNum) + ")")
            c += 1
        while c < groupMaxNum:
            groupPrintArr.append("n/a")
            c += 1
            
    groupHeader = ["Group Number"]
    for s in range(1,groupMaxNum+1):
        groupHeader.append("Student #" + (str)(s))



    perRound = groupCounter/maxRounds
    for s in studentList:
        temp = []
        temp.append(s.name)
        c  = 0
        for g in s.groupList:
            #temp.append(g  - perRound * c)
            tempStr = (str)(g.groupNum) + " (" +(str)(g.round) + ")"
            temp.append(tempStr)
            c += 1
        teamMatchingArray.append(temp)
        
    #header = ["Student name", "Group Number", "Group Language", "Group Exp", "Student Exp", "Number of students"]
    header = ["Student Name"]
    for i in range(maxRounds):
        header.append("Group " + (str)(i + 1))

    header1 = ["Student Name", "Group Num", "Language", "Project Type"]
    unplacedArr = []
    for z in unplacedStudents:
        temp = []
        temp.append(z.name)
        temp.append(z.teammatesNum)
        temp.append(z.language)
        temp.append(z.projectType)
        unplacedArr.append(temp)

    detailedHeader = ["Group Number","Student Name", "Teammate Num", "Language", "Project Type", "Experience Level"]
    detailedInfoArr = []
    for g in groupArr:
        for s in g.studentList:
            s = [g.groupNum, s.name, s.teammatesNum, s.language, s.projectType, s.experienceLvl]
            detailedInfoArr.append(s)
    with open('/home/UFAD/grossj/SwampHacks/Swamphacks-Team-Matching/groupBreakdown.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(detailedHeader)
        writer.writerows(detailedInfoArr)


    unplacedArr = []
    for z in unplacedStudents:
        temp = []
        temp.append(z.name)
        temp.append(z.teammatesNum)
        temp.append(z.language)
        temp.append(z.projectType)
        unplacedArr.append(temp)

    with open('/home/UFAD/grossj/SwampHacks/Swamphacks-Team-Matching/unplacedStudents.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header1)
        writer.writerows(unplacedArr)

    with open('/home/UFAD/grossj/SwampHacks/Swamphacks-Team-Matching/results.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(teamMatchingArray)
                 
    with open('/home/UFAD/grossj/SwampHacks/Swamphacks-Team-Matching/groupInformation.csv', 'w') as csvfile1:
        writer1 = csv.writer(csvfile1)
        writer1.writerow(groupHeader)
        for i in range(0,len(groupPrintArr) - 4,5):
            temp = [groupPrintArr[i], groupPrintArr[i+1], groupPrintArr[i+2], groupPrintArr[i+3], groupPrintArr[i+4]]
            writer1.writerow(temp)

        
           
    return groupArr, studentList

 ##############################################################################

def teamCreatingAlgorithm(groupArray, studentList):
    # maxRounds = 3
    # with open("/home/UFAD/grossj/SwampHacks/Swamphacks-Team-Matching/responses.csv") as csvfile:
    #     reader = csv.reader(csvfile, delimiter=',') 
    #     g = type(reader)
    #     for row in reader:
    #         for student in studentList:
    #             if student.name == row[1] and row[1] != "What is your name?":
    #                 choices = [(int)(row[2]), (int)(row[3]), (int)(row[4])]
    #                 #check that the student's choices are valid
    #                 for groupNumber in choices:
    #                     for groupsStudentIn in student.groupList:
    #                         if groupNumber == groupsStudentIn.groupNum and student in groupsStudentIn.studentList:
    #                             student.groupChoiceList.append(groupsStudentIn)


    #create fake student group choices for simulation purposes
    for student in studentList:
        while len(student.groupChoiceList) != len(student.groupList):
            randGroup = student.groupList[random.randint(0, len(student.groupList)-1)]
            if randGroup not in student.groupChoiceList:
                student.groupChoiceList.append(randGroup)

    placedStudentList = []

    for student in studentList:
        teamMatcher(student, placedStudentList)
    count = 1
    for student in studentList:
        if len(student.groupList) != 0:
            count += 1
    print()
                    
    #iterate through every student

    # for student in studentList:
    #     #iterate through the students group rankings
    #     for studentGroupPick in student.groupChoiceList:
    #         choiceRank = 0
    #         #iterate through each other student in that group
    #         for teammate in studentGroupPick.studentList:
    #             unison = True
    #             #iterate through teammates and check if their first choices are also that group
    #             if teammate != student:

    #                 if teammate.groupChoiceList[0] ==
    studentList.sort(key=operator.attrgetter("name"),reverse=True)     
    matchedHeader = ["Student Name", "Group Num"]
    matchedArr = []
    for student in studentList:
        if student.assignedGroup == None:
            matchedArr.append([student.name, "Not Placed"])
        else:
            matchedArr.append([student.name, student.assignedGroup.groupNum])
    with open('/home/UFAD/grossj/SwampHacks/Swamphacks-Team-Matching/finalGroups.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(matchedHeader)
        writer.writerows(matchedArr)

def teamMatcher(student, placedStudentList):
    for choice in range(len(student.groupList)):    
        if student.assignedGroup == None:
            for index in range(len(student.groupList)):
                groupPick = student.groupChoiceList[index]
                unison = True
                for teammate in groupPick.studentList:
                    if teammate != student:
                        if teammate.groupChoiceList[choice].groupNum != groupPick.groupNum | teammate.groupChoiceList[0].round != groupPick.round :
                            unison = False
                if unison:
                    for student in groupPick.studentList:
                        student.assignedGroup = groupPick
                        placedStudentList.append(student)
                    return

            


    
                        





    
    
    
    
    # for group in groupArray:
    #     everyStudentAgrees = True
    #     for student in group.studentList:
    #         #check first choice
    #         if 
                




def printGroups(languageGroup):
    for g in languageGroup:
        print("Group #", {g.groupNum}, " \n")
        print("Number of students: " , {g.numStudent} , "\nExp Lvl: " , {g.experienceSum} , " \n \n ")

###############################################################################################################
with open("/home/UFAD/grossj/SwampHacks/Swamphacks-Team-Matching/Swamphacks Team Matching Form.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',') 
    g = type(reader)
    studentList = []
    for row in reader:
        studentList.append(Student(row[1], row[2], row[3], row[4], row[5], row[6]))
    
studentList.pop(0)
for student in studentList:
    if student.teammatesNum == "I am currently not in a team":
        student.teammatesNum = 1
    if student.experienceLvl == "Beginner":
        student.experienceLvl = 1
    elif student.experienceLvl == "Intermediate":
        student.experienceLvl = 2
    elif student.experienceLvl == "Advanced":
        student.experienceLvl = 3
    student.teammatesNum = int(student.teammatesNum)

groupArray, studentList = teamMatchingAlgorithm(studentList)
teamCreatingAlgorithm(groupArray, studentList)