months = 91
ReproRate = 1
lifespan = 20
ledger = []                           #this list will represent the numbers of the rabit population
totalpopulation = 0
thesavana = {}
                                            #this dictionary will act as the ledger that tracks how many rabit pairs there are                 #each time the loop runs it adds the new value into an unpopualted list that I designated as 'timeline' which represents months
for i in range(0, (months+1)):              #I am making a list based on the lifespan value. index 0 represents an immature rabbit pair, index 1 reps a month old mature pair,
    M = i                                   #I am making a nested list with the number of lists within a list. these lists will then occupty the dictionary for population
    ledger.append([0])                      #population ledger keeping
    for i in range(0,lifespan):
        ledger[M].append(0)                 #index 2 reps a 2 month old mature pair and the last index in the list represents rabbit heaven/hell for dead rabbits
                                            #My goal here is to create a dictionary where the key represents the month and the value represents the population ledger
for i in range(0,(months)):                 #the ledger was made in lines 8-9 in this code and now I am building a dictionary with keys numbered 1-6--to rep the months--
    thesavana[i+1]= ledger[i]               #then I am giving those "month keys" a value of instancelist which is the population ledger for that month.
                                            #LESSON LEARNED: do not make multiple keys equal to a single list. This will cause an issue when changing the values in the lists.
                                            #although the keys in the dict are different if the same list is assigned to different keys then changes in one key's list will be reflected in all dictionary key lists
#the next step is to transfer data between the monthly ledgers and transition the immatures to mature(1 month old) and month olds to 2 month old rabbits, etc
#I will have to do something in regards to the list length of the ledger. I will have to move across each ledger one index at a time between month and (month-1)


thesavana[1][0] = 1
print(thesavana)
for i in thesavana:
    B = i-1
    A = i
    if A > 1:
        for k in range(0,lifespan):
            X = k+1
            thesavana[A][X] = thesavana[B][k]             #here I am shifting the population by one list index value to represent aging by 1 month
            if k != 0 and k != lifespan:                    #This line represents the reproduction portion of the code that feeds into the next generation's monthly population ledger
                                                            #here I am saying that if i does not 0--0 represents index 0 which represents immature
                thesavana[A][0] += thesavana[B][k]                 #rabbit pairs--then these are rabbits that are mature and will reproduce. I also made the distinction
                                                            #that rabbits older than the lifespan will not participate in reproduction.

for i in range(0,lifespan):                              #this gets me to the last month ledger which ultimately accounts for my final population
    totalpopulation += thesavana[months][i]               #'lifespan' is in the range specifications becuase the last item in the list represents dead rabbits
print(totalpopulation)
