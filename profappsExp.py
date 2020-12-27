#Project Name: Profitable App Profiles for the App Store and Google Play Markets
#A Data Analysis Project by Carl Nera 
#Version 1.1

#This file contains all the methods for Importing Data & Navigating around it

#Opening CSV Files and Transferring Data to dataset containers
from csv import reader
def openCSV(filename):
    opened_file = open(filename,encoding="utf8");
    read_file = reader(opened_file);
    temp_dataset = list(read_file);
    return temp_dataset;

#Method to Explore and Navigate within Datasets
def explore_dset(dset,startpoint,endpoint,rows_col,act_slicer):
    if act_slicer:
        slicer = dset[startpoint:endpoint];
        for row in slicer:
            print(row,"\n");
    else:
        for row in dset:
            print(row, "\n");
    if rows_col:
        print("Number of Rows = ",len(dset));
        print("Number of Columns = ",len(dset[0]));