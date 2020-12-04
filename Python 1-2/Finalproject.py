'''
Write a program, which can read 'System' csv files and return relevant information for a particular event id.
[The program should provide an option where user can enter a event id and its relevant information are retrieved from the csv file]
'''
import csv
data=[]
with open("System.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data.append(row)
#print(data)

Event_ID=input("Enter the event_id..")

col=[x[3] for x in data]
#print(col)
if Event_ID in col:

    for x in range(0,len(data)):

        if Event_ID==data[x][3]:

            print(data[x])

else:
    print("Opps ☹! Sorry There is No Event_ID like this please check it once and try again later. Thank you !😎")

