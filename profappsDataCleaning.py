#Project Name: Profitable App Profiles for the App Store and Google Play Markets
#A Data Analysis Project by Carl Nera 
#Version 1.1

#This file contains all the methods for Dataset Cleaning

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

#Duplicate Cleaning begins here
def clean_dup_gplay(dset_gplay):
    rvmax = maxRevCount(dset_gplay);
    dset_gplay_cleaned = [];
    dset_gplay_alreadyadded = [];
    for row in dset_gplay:
        name = row[0];
        n_reviews = float(row[3]);
        if (n_reviews == rvmax[name]) and (name not in dset_gplay_alreadyadded):
            dset_gplay_cleaned.append(row);
            dset_gplay_alreadyadded.append(name);
    return dset_gplay_cleaned;

#Methods to clean and remove Non-English Apps for googleplay and appstore

def if_english_app(appname):
    n_ascii = 0;
    for character in appname:
        if ord(character) > 127:
            n_ascii += 1;
    if n_ascii > 3:
        return False;
    else:
        return True;

def english_apps(dset,index):
    new_dset = [];
    for row in dset:
        name = row[index];
        if(if_english_app(name)):
            new_dset.append(row);
    return new_dset;



