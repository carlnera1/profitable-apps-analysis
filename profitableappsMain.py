#Project Name: Profitable App Profiles for the App Store and Google Play Markets
#A Data Analysis Project by Carl Andrew Nera 
#Version 1.1

#The Project Scenario: A Software Company that builds Android and iOS mobile apps require a data analysis in order to help their team of developers to make data-driven decisions on building their new app.
#In the Company itself, they only build apps that are free to download thus their main source of income is through in-app ads. 
#This means that the company's revenue is largely influenced by the number of users of that particular mobile app.

#Goal:
#Now the goal of this Data Analysis project is to help the company to understand what kind of mobile apps that are likely to attract more users.

#This Project consists of 6 files (4 python programs & 2 Excel CSV for the Dataset)

from profappsExp import openCSV, explore_dset
from profappsDataCleaning import clean_dup_gplay, english_apps, free_apps
from profappsAnalysis import analysis_dataset

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

#Initializing 2nd version of dset_googleplay with the method returning the new dataset.
dset_googleplay_ver2 = clean_dup_gplay(dset_googleplay)

print("\Output Below:")

for row in dset_googleplay_ver2:
    name = row[0]
    if name == 'Instagram':
        print(row)

print("\nAs you can see, there's only 1 app record of Instagram left same applies for other apps that has duplicate entries.\n")
explore_dset(dset_googleplay_ver2,0,3,True,True)

#---NEXT TASK: Removing Non-English Apps---#
print("Next on our step in Datacleaning is to eliminate non-english apps on our datasets\nAs we navigate around both datasets, we notice that some of the names are not written in the english language and are not directed toward an English-speaking audience")
print("\nLet's see examples below:\nAPPSTORE:\n")

explore_dset(dset_appstore,810,815,True,True)

print("\nANDROID:\n")

explore_dset(dset_googleplay_ver2,4410,4415,True,True)

print("\nFor this reason, we will remove these apps from the set.")
print("\nHowever, in order to reduce the impact of data loss, we will only remove app if its name has more than 3 non-ASCII characters\n")

#Initializing new empty datasets for googleplay and appstore (ver3 & ver2 respectively) with a method returning the new dataset.

dset_googleplay_ver3 = english_apps(dset_googleplay_ver2,0)
dset_appstore_ver2 = english_apps(dset_appstore,1)

print("Result of the Process:\nGoogleplay\n");
explore_dset(dset_googleplay_ver3,0,3,True,True)
print("\nAppstore\n")
explore_dset(dset_appstore_ver2,0,3,True,True)

#Next Task: Isolating Free Apps
print("\nThe last step on our data cleaning process is to isolate the free apps which is what we need for our analysis.\nData Cleaning Process below:\n")

#Initializing new empty datasets for googleplay and appstore (final versions) with a method returning the new dataset. 
dset_googleplay_ver_final = []
dset_appstore_ver_final = []
dset_googleplay_ver_final = free_apps(dset_googleplay_ver3,7)
dset_appstore_ver_final = free_apps(dset_appstore_ver2,4)

print("Result of the Process:\nGoogleplay\n")
explore_dset(dset_googleplay_ver_final,0,10,True,True)
print("\nAppstore\n")
explore_dset(dset_appstore_ver_final,0,10,True,True)

print("That should be enough thus concludes our data cleaning process. Moving onto our Data Analysis below:")

print("\n\nPROFITABLE APPS ANALYSIS\n")

list_choices = ["1 - Most Common Apps by Genre" , "2 - Most Popular Apps by Genre in the App Store", "3 - Most Popular Apps by Genre on Google Play", "4 - Exit"];
loop = True
while loop:
    for choices in list_choices:
        print(choices , "\n")
    choice = input("\nChoose from one of the data analysis below:")
    if choice == '4':
        loop = False
        print("Thank you for using this Data Analysis Program.")
    else:
        analysis_dataset(choice)
    