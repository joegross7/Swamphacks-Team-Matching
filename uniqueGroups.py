class Participant:
    def __init__(self, num):
        self.number = num
        self.previousPopList = []
        self.groupCount = 0

populationCount = []
for i in range(200):
    populationCount.append(Participant(i))

groupsCount = []



#check a number of different populations and group counts
# for g in groupsCount:
#     for c in range(3,200):
def uniqueGroups(groupCount, populationCount)
    g = groupCount
    c = populationCount
    population = []
    for i in range(c):
        population.append(Participant(i))
    groupList = []
    groupCount = 0
    #start formula
    loopNum = 0
    maxLoopNum = 10
    #while the group is not at capacity 
    for i in range(len(population)):
        for i in population:
            group = [i]
            loopNum = 0
            while len(group) < g and loopNum != maxLoopNum:
                #iterate through everyone trying to find a match for the group 
                for person in population:
                    if person != i:
                        if len(group) == g:
                            break
                        prevMatched = False
                        #iterate through each pop the person has been matched with and check if they are in the group you're trying to place them in
                        # for groupmate in group:
                        for prevPerson in person.previousPopList:
                            for groupmate in group:
                                if prevPerson.number == groupmate.number:
                                    prevMatched = True
                        if prevMatched == False and len(group) < g:
                            #add person to group
                            for groupMate in group:
                                person.previousPopList.append(groupMate)
                                groupMate.previousPopList.append(person)
                            group.append(person)
                            person.groupCount += 1

                            #iterate through group and add person to their pop list and them to the persons pop list
                loopNum += 1
                
            if len(group) == g:    
                groupList.append(group) 

    print("For a population of ", c, "in groups of ", g, "there are ", len(groupList), "unique groups formed")
    # for group in groupList:
    #     for pop in group:
    #         if pop != group[len(group) - 1]:
    #             print(pop.number, "and")
    #         else:
    #             print(pop.number,"\n")
    print()    

