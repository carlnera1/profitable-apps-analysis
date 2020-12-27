#Project Name: Profitable App Profiles for the App Store and Google Play Markets
#A Data Analysis Project by Carl Andrew Nera 
#Version 1.1

#The Project Scenario: A Software Company that builds Android and iOS mobile apps require a data analysis in order to help their team of developers to make data-driven decisions on building their new app.
#In the Company itself, they only build apps that are free to download thus their main source of income is through in-app ads. 
#This means that the company's revenue is largely influenced by the number of users of that particular mobile app.

#Goal:
#Now the goal of this Data Analysis project is to help the company to understand what kind of mobile apps that are likely to attract more users.

#This Project consists of 5 files (3 python programs & 2 Excel CSV for the Dataset)

#----------PROGRAM STARTS HERE----------#
from profappsDataCleaning import openCSV,clean_dup_googleplay,

#Initializing dataset containers using lists
dset_googleplay_header = []
dset_googleplay = []
dset_appstore_header = []
dset_appstore = []

#MAIN PROGRAM

#Load CSV Excel Datasets into dataset (dset) containers
dset_googleplay = openCSV('googleplaystore.csv')
dset_appstore = openCSV('AppleStore.csv')

#Separation of headers and removal from the main dset.
dset_googleplay_header = dset_googleplay[0]
dset_appstore_header = dset_appstore[0]
del dset_googleplay[0]
del dset_appstore[0]

#----DATASET CLEANING----#
Text_1 = "<After Importing all CSV Files, We check for false error. According to a discussion on Github, we found only 1 row in the google play dataset which is row 10472 as shown here:>"
Text_2 = "<Let's compare it to the header and another row.>\n"
Text_3 = "<Next, we eliminate duplicate entries, for this, our criteria is simple, We will only keep the record with the highest rating count>"

print("<Profitable App Profiles Project by Carl Nera>\n")
print(Text_1, "\n")
print(dset_googleplay[10472], "\n")
print(Text_2)
print(dset_googleplay[10472], "\n", dset_googleplay_header, "\n")
print(dset_googleplay[20], "\n<TOTAL NUMBER OF ROWS: ", len(dset_googleplay),">")
print("\n<Henceforth, we'll delete it.>\n")

#Deleting the Specific Row (10472)
del dset_googleplay[10472]
print("<TOTAL NUMBER OF ROWS AFTER: ", len(dset_googleplay)," >")

#Sorting and removing duplicate entries
print("When we explore the dataset for Google Play long enough, we may find some apps to be duplicated. \n")

for row in dset_googleplay:
    name = row[0]
    if name == 'Instagram':
        print(row)

print("\nIn order to remove it, we will distinguish which are duplicate apps and those that does not have.")
print("Our criteria is simple, we will only keep the record with the highest rating count\n")

#Initializing 2nd version of dset_googleplay
dset_googleplay_ver2 = []
dset_googleplay_ver2 = 