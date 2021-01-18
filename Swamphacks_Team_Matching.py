import csv
import operator
import math

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


class Groups:
    def __init__(self, student, groupNum):
        self.groupNum = groupNum
        self.studentList = [student]
        self.experienceSum = student.experienceLvl;
        self.language = student.language
        self.numStudent = student.teammatesNum
        student.groupList.append(self.groupNum)
        self.projectType = student.projectType

    def AddStudent(self, student):
        self.studentList.append(student)
        self.experienceSum += student.experienceLvl
        self.numStudent += student.teammatesNum
        student.groupList.append(self.groupNum)

        

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
    languageDict = {}
    projectDictDict = {}
    for student in studentList:
        templanguageGroup = languageDict.get(student.language)
        if templanguageGroup == None:
            languageDict[student.language] = Groups(student,0)
        else:
            templanguageGroup.AddStudent(student)
    

    for languageGroup in languageDict:
        projectDict = {}
        for student in languageDict[languageGroup].studentList:
            tempProjectGroup = projectDict.get(student.projectType)
            if tempProjectGroup == None:
                projectDict[student.projectType] = Groups(student,0)
            else:
                tempProjectGroup.AddStudent(student)
        projectDictDict[languageGroup] = projectDict        





    
    #sort into language groups
    threeCount = 0
    oneCount = 0
    totalStudentCount = 0      

    teamMatchingArray = []
    maxRounds = 3

    languageGroupList = []

    for s in studentList:
        s.groupList = []    

    groupCounter = 1

    for roundCounter in range(maxRounds):
        unplacedStudents = []
        groupCounter = 0
        for language in projectDictDict:
            for project in projectDictDict.get(language):
                languageAndProjectGroup = projectDictDict[language].get(project)
                #get total number of students
                studentSum = 0
                threeCount = 0
                for student in languageAndProjectGroup.studentList:
                    studentSum += student.teammatesNum
                    totalStudentCount += student.teammatesNum
                    if student.teammatesNum == 3:
                        threeCount += 1
                    if student.teammatesNum == 1:
                        oneCount += 1    
                groupList = []
                for student in languageAndProjectGroup.studentList:
                    group = Groups(student, groupCounter)
                    groupCounter += 1
                    for teammate in languageAndProjectGroup.studentList:
                        if teammate != student and len(student.groupList) < maxRounds:
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
                    if len(group.studentList) > 1:
                        groupList.append(group)
                    else:
                        student.groupList.pop(len(student.groupList)-1)

                languageGroupList.append(groupList)

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
                        
    groupArr = languageGroupList[0]
    for x in range(1, len(languageGroupList)):
        groupArr += languageGroupList[x]
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
            temp.append(g)
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

    detailedHeader = ["Student Name", "Teammate Num", "Language", "Project Type"]
    detailedInfoArr = []
    for g in groupArr:
        for s in g.studentList:
            s = [g.groupNum, s.name, s.teammatesNum, s.language, s.projectType]
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

        
       
    

    
    return 1
    
def printGroups(languageGroup):
    for g in languageGroup:
        print("Group #", {g.groupNum}, " \n")
        print("Number of students: " , {g.numStudent} , "\nExp Lvl: " , {g.experienceSum} , " \n \n ")


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
        student.experienceLvl = 1*((int)(student.teammatesNum))
    elif student.experienceLvl == "Intermediate":

        student.experienceLvl = 2*((int)(student.teammatesNum))
    elif student.experienceLvl == "Advanced":
        student.experienceLvl = 3*((int)(student.teammatesNum))
    student.teammatesNum = int(student.teammatesNum)

teamMatchingAlgorithm(studentList)
    






#  test = (float(studentSum)/groupMaxNum)
#                 groupNum = int(math.ceil(test))
#                 if threeCount > groupNum:
#                     groupNum = threeCount
#                 #if lots of groups of 3's, they set the max group num
#                 remainder =  studentSum % groupMaxNum
#                 languageStudentList = []
#                 for s in languageAndProjectGroup.studentList:
#                     languageStudentList.append(s)
#                 languageStudentList.sort(key=operator.attrgetter("teammatesNum"),reverse=True)    
#                 groupList_ = []
#                 T = []
#                 for i in range(groupNum):
#                     #create the required amount of groups for the specific language and initialize them with the first n students which are sorted by number of team mates
#                     groupCounter += 1 #global group number 
#                     #creating the groups with the first student in array then remove them 
#                     groupList_.append(Groups(languageStudentList[0], groupCounter))
#                     languageStudentList.pop(0)
#                 loopCounter = 0
#                 counterEnable = False
#                 while len(languageStudentList) != 0 | loopCounter < groupNum:
#                     beginningLength = len(languageStudentList)
#                     #iterate through the rest of the groups backwards and assign them to groups to get a total less than 4
#                     for g in reversed(groupList_):
#                         for s in languageStudentList:
#                             studentInGroup = False
#                             for sGroups in s.groupList:
#                                 if g.groupNum == sGroups:
#                                     studentInGroup = True
#                             if s.teammatesNum + g.numStudent <= groupMaxNum and studentInGroup == False and s.language == s.language and s.projectType == g.projectType:
#                                 g.AddStudent(s)
#                                 #print("Group #", {g.groupNum}, " \n")
#                                 #print("Number of students: " , {g.numStudent} , "\nExp Lvl: " , {g.experienceSum} , " \n \n ")
#                                 languageStudentList.remove(s)
#                                 #QprintGroups(languageGroup)
#                     fullGroupTally = 0
#                     for group in groupList_:
#                         if g.numStudent >= 3:
#                             fullGroupTally += 1
#                     if len(languageStudentList) == beginningLength:         
#                         loopCounter += 1
                        
#                 for s in languageStudentList:
#                     unplacedStudents.append(s)

#                 #languageGroup.sort(key=operator.attrgetter("experienceSum"))
                
#                 languageGroupList.append(groupList_)
#                 #printGroups(languageGroup)