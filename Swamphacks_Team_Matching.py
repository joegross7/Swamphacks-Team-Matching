import csv
import operator
import math

class Student:
     def __init__(self, name, email, year, participated, experienceLvl,  teammatesNum, language, projectType):
        self.name = name
        self.email = email
        self.year = year
        self.participated = participated
        self.experienceLvl = experienceLvl
        self.teammatesNum = teammatesNum
        self.language = language
        self.projectType = projectType
        self.groupList = []

class Groups:
    def __init__(self, student, groupNum):
        self.groupNum = groupNum
        self.studentList = [student]
        self.experienceSum = student.experienceLvl;
        self.language = student.language
        self.numStudent = student.teammatesNum
        self.locked = False
        student.groupList.append(self.groupNum)
    def AddStudent(self, student):
        self.studentList.append(student)
        self.experienceSum += student.experienceLvl
        self.numStudent += student.teammatesNum
        student.groupList.append(self.groupNum)
        if self.numStudent >= 4:
            self.locked = True
        

class GroupsList:
    def __init__(self, groupList):
        self.groupList = groupList
        self.cu

def unholyAlgorithm(studentList):
    groupMaxNum = 4
    #create base groups
    javaStudentList = []
    pythonStudentList = []
    cStudentList = []
    #sort into language groups
    threeCount = 0
    oneCount = 0
    twoCount = 0
    totalStudentCount = 0
    for s in studentList:
        if s.language == "Python":
            pythonStudentList.append(s)
        elif s.language == "Java":
            javaStudentList.append(s)
        elif s.language == "C/C++":
            cStudentList.append(s)
        totalStudentCount += s.teammatesNum        
    
        
    #sort language groups by first team mate number then experience level
    pythonStudentList.sort(key=operator.attrgetter("teammatesNum", "experienceLvl"), reverse=True)
    javaStudentList.sort(key=operator.attrgetter('teammatesNum', "experienceLvl"), reverse=True)
    cStudentList.sort(key=operator.attrgetter('teammatesNum', "experienceLvl"), reverse=True)

    languageList = [javaStudentList.copy(), pythonStudentList.copy(), cStudentList.copy()]
    languageGroupList = []

    unholyArray = []
    maxRounds = 3

    for i in range(maxRounds):
        languageList = [javaStudentList.copy(), pythonStudentList.copy(), cStudentList.copy()]
        unplacedStudents = []
        groupCounter = 0
        for ll in languageList:
            #get total number of students
            studentSum = 0
            threeCount = 0
            for s in ll:
                studentSum += s.teammatesNum
                if s.teammatesNum == 3:
                    threeCount += 1
            #divide total students by 4 to get number of 4 person groups. also get remainder for extra group
            groupNum = math.ceil(studentSum/groupMaxNum)
            if threeCount > groupNum:
                groupNum = threeCount
            #if lots of groups of 3's, they set the max group num
            remainder =  studentSum % groupMaxNum
            languageGroup = []
            for c in range(groupNum):
                #create the required amount of groups for the specific language and initialize them with the first n students which are sorted by number of team mates
                groupCounter += 1 #global group number 
                #creating the groups with the first student in array then remove them 
                languageGroup.append(Groups(ll[0], groupCounter))
                #print("Group #", {languageGroup[len(languageGroup)-1].groupNum}, " \n")
                #print("Number of students: " , {languageGroup[len(languageGroup)-1].studentList[0].teammatesNum} , "\nExp Lvl: " , {languageGroup[len(languageGroup)-1].studentList[0].experienceLvl} , " \n \n ")
                ll.remove(ll[0])
            #while the languageList still has entities
            infiniteLoopStopper = 10
            loopCounter = 0
            counterEnable = False
            while len(ll) != 0 | loopCounter != infiniteLoopStopper:
                #iterate through the rest of the groups backwards and assign them to groups to get a total less than 4
                for g in reversed(languageGroup):
                    for s in ll:
                        studentInGroup = False
                        for sGroups in s.groupList:
                            if g.groupNum == sGroups:
                                studentInGroup = True
                        if s.teammatesNum + g.numStudent <= groupMaxNum and studentInGroup == False:
                            g.AddStudent(s)
                            #print("Group #", {g.groupNum}, " \n")
                            #print("Number of students: " , {g.numStudent} , "\nExp Lvl: " , {g.experienceSum} , " \n \n ")
                            ll.remove(s)
                            #QprintGroups(languageGroup)
                if len(ll) < 3:
                    counterEnable = True
                if counterEnable:
                    loopCounter += 1
                    
            for s in ll:
                unplacedStudents.append(s)

            #languageGroup.sort(key=operator.attrgetter("experienceSum"))

            languageGroupList.append(languageGroup)
            #printGroups(languageGroup)


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
        #                unholyarray.append(temp)   
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
        unholyArray.append(temp)
        
    #header = ["Student name", "Group Number", "Group Language", "Group Exp", "Student Exp", "Number of students"]
    header = ["Student Name"]
    for i in range(maxRounds):
        header.append("Group " + (str)(i + 1))

    with open('results.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(unholyArray)
                 
    with open('groupInformation.csv', 'w', newline='') as csvfile1:
        writer1 = csv.writer(csvfile1)
        writer1.writerow(groupHeader)
        for i in range(0,len(groupPrintArr) - 4,5):
            temp = [groupPrintArr[i], groupPrintArr[i+1], groupPrintArr[i+2], groupPrintArr[i+3], groupPrintArr[i+4]]
            writer1.writerow(temp)

        
       
    

    
    return groupList
    
def printGroups(languageGroup):
    for g in languageGroup:
        print("Group #", {g.groupNum}, " \n")
        print("Number of students: " , {g.numStudent} , "\nExp Lvl: " , {g.experienceSum} , " \n \n ")


with open('Swamphacks Team Matching Form.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',') 
    studentList = []
    for row in reader:
        studentList.append(Student(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
    
studentList.pop(0)
for student in studentList:
    if student.experienceLvl == "Beginner":
        student.experienceLvl = 1*((int)(student.teammatesNum))
    elif student.experienceLvl == "Intermediate":
        student.experienceLvl = 2*((int)(student.teammatesNum))
    elif student.experienceLvl == "Advanced":
        student.experienceLvl = 3*((int)(student.teammatesNum))
    if student.year == "Freshmen":
        student.year = 1
    elif student.year == "Sophomore":
        student.year = 2
    elif student.year == "Junior":
        student.year = 3
    elif student.year == "Senior":
        student.year = 4
    student.teammatesNum = (int)(student.teammatesNum)

unholyAlgorithm(studentList)
    




