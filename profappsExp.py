#Project Name: Profitable App Profiles for the App Store and Google Play Markets
#A Data Analysis Project by Carl Nera 
#Version 1.1

#This file contains all the methods for Importing Data, Navigation and Data Analysis.

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


#Data Analysis Methods----

def table_frequency(dset,index):
    tbl = {};
    total = 0;

    for row in dset:
        total+= 1;
        val = row[index];
        if val in tbl:
            tbl[val] += 1;
        else:
            tbl[val] = 1;
    
    tbl_percentages = {};

    for key in tbl:
        perc = (tbl[key] / total) * 100;
        tbl_percentages[key] = perc;
    
    return tbl_percentages;

def display_table(dset,index):
    table = table_frequency(dset,index);
    tbl_disp = [];
    for key in table:
        key_val = (table[key], key);
        tbl_disp.append(key_val);
    
    tbl_sorted = sorted(tbl_disp,reverse=True);

    for ent in tbl_sorted:
        print(ent[1], ' : ' , ent[0]);

#Most Popular Apps Appstore

def genre_ios(dset,index):
    appstore_genre = table_frequency(dset,index);
    for genre in appstore_genre:
        total = 0;
        len_genre = 0;
        for app in dset:
            genre_appstore = app[11];
            if genre_appstore == genre:
                n_ratings = float(app[5]);
                total += n_ratings;
                len_genre += 1;
        avg_ratings = total / len_genre;
        print(genre, ' : ', avg_ratings);

def ios_specific_genre(dset,index,type_genre):
    for app in dset:
        if app[index] == type_genre:
            print(app[1], " : ", app[5]);

            
#Most Popular Apps Googleplay

def categories_gplay(dset,index):
    category_gplay = table_frequency(dset,index);
    for category in category_gplay:
        len_category = 0;
        total = 0;
        for app in dset:
            category_app = app[1];
            if category_app == category:
                no_installs = app[5];
                no_installs = no_installs.replace(',','');
                no_installs = no_installs.replace('+','');
                total += float(no_installs);
                len_category += 1;
        avg_installs = total / len_category;
        print(category, " : ", avg_installs);

def gplay_specific_genre(dset,type_genre,val1,val2,val3):
    for app in dset:
        if app[1] == type_genre and (app[5] == val1 or app[5] == val2 or app[5] == val3):
            print(app[0], ':', app[5]);
