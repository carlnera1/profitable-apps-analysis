#Project Name: Profitable App Profiles for the App Store and Google Play Markets
#A Data Analysis Project by Carl Andrew Nera 
#Version 1.1

#This file contains all the methods for Dataset Cleaning

#Opening CSV Files and Transferring Data to dataset containers
from csv import reader
def openCSV(filename):
    opened_file = open(filename,encoding="utf8");
    read_file = reader(opened_file);
    temp_dataset = list(read_file);
    return temp_dataset;

#Methods to Clean Duplicates in googleplay dataset

#Get max review count first
def maxRevCount(dset):
    revmax = {};
    for row in dset:
        name = row[0];
        nreviews = float(row[3]);
        if name in revmax and revmax[name] < nreviews:
            revmax[name] = nreviews;
        
        if name not in revmax:
            revmax[name] = nreviews;
    return revmax;
    
def clean_dup_googleplay(dset_gplay):

