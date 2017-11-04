
from operator import itemgetter # this is used in order to sort our list by required key choice
import csv

lines = []

with open("MobilePhoneMasts.csv.sjtmdl") as file:  #opens csv file to be used
    for line in file:
        # The rstrip method gets rid of the "\n" at the end of each line
        lines.append(line.rstrip().split(","))  #imports contents of csv file into empty python list named "lines"
        
file.close()
#print(lines) #checking if csv has been imported into python list

#sortedlist is the name of the new list created, in ascending order of lease amount

sortedlist = sorted(lines, key=itemgetter(10))
#print(sortedlist) #display sortedlist to check

# as can be seen, sortedlist is used in most of the methods as the key attribute, so i defined sortedlist as a global variable#
#so it can easily be accesed by all the required methods, saving time and simpler code

#Displaying total rent for all items
def totalrent(sortedlist):      
    totals = []              #created empty list to input total
    thesum = 0               # setting initial sum to zero
    for x in sortedlist:     # iteration through each line in the sortedlist
        Rent = x[10]         # assigning the variable Rent with the value of the current list for that row
        totals.append(Rent)  # for each row,the Rent is appended to the totals list
    for y in totals:         #for each row in total list
        thesum += y          #the sum is the result of adding together the value of Rent from each row
    return float(thesum)     #displays thesum, which is the total rent for all items
#totalrent(sortedlist)


#Displaying list of first 5 data in ascending order
def ascd(sortedlist):           #sorted list is already arranged in order of ascending order of current rent via the index 10 of the
                                # 11th column
        count = 0               #setting count of zero for our loop
        ascend = []
        for x in sortedlist:    #iterating through each dictionary of our list
            ascend.append(x)    #each row is added to a new list called ascend
            count += 1          #the count is increased by one for every loop till count gets to 4
            if count >5:        #break command then stops the process at count =4, and no more entries are added
                break
        print(ascend)
#ascd(sortedlist)


#Displaying list of first 5 data in descending order
def sortedlistdes(sortedlist): 
    deslist= sorted(sortedlist, key=itemgetter(10), reverse = True) #our sorted list is now reversed in reference to desc value of current rent
    count = 0
    descend = []            #new empty list created
    for x in deslist:       #each row of descending list
        descend.append(x)   #each row is added to new empty list called descend
        count+= 1           #count is increased by one after each iteration
        if count >5:        #at countof 4, no more entries are added to descend
            break
    print(descend)          #displays the full descend list of 5 dictionaries, 5 rows, 5 colums
#sortedlistdes(sortedlist)

 


def addentry(sortedlist,entry):                #adding entry to sortedlist and display in browser
                                               #entry is the attr used that contains the added entries to increase the sortedlist size
    sortedlist.append(entry)                   #entry added to sortedlist
    with open("latestlist.txt", "a") as my_file:  # a textfile called latestlist is then opened and renamed in append(a) mode which retains every entry added
        for x in sortedlist:                   # for each line or row in the sortedlist
            data = my_file.write(str(x))       #each row is then added to the textfile via the write command
    print(data)	                               #requesting a print of the text file, but couldn't see it since in write mode, checked it by opening file manually
    my_file.close()                            #textfile is now closed in order not to cause problems

#addentry(sortedlist,sortedlist[4])            #runs method,with entry of 5th row in sortedlist added to the textfile(latestlist.txt) 

 
    
#def datalease(LeaseStartDate,LeaseEndDate):
    #from datetime import timezone; datetime_object = datetime_object.replace(tzinfo=timezone.utc)
  
    #for  x in newslist(mmast):
        #if (LeaseStartDate >= 01/06/1999 and LeaseEndDate <=31/08/2007):
            #print (x)

#datalease(01/06/199, 31/08/2007)

def countofmasts(sortedlist,TenantName):  #method with attr sortliste and Tennant Name
    mountcast = {}                        #empty list created to recieve the values
    count = 0
    for x in sortedlist:              
        mountcast.append(x(6))            #name of Tennant is added to mountcast list
        mountcast.append(count)           #checks
        if x[TenantName]== x[6]:
            count+=1
        print(mountcast)

#countofmasts(sortedlist,sortedlist[6])  

