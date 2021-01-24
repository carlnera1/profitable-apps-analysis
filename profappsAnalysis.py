#Project Name: Profitable App Profiles for the App Store and Google Play Markets
#A Data Analysis Project by Carl Andrew Nera 
#Version 1.1

#This file contains all the methods for Dataset Analysis

from profappsExp import display_table, genre_ios, ios_specific_genre, categories_gplay, gplay_specific_genre;

def common_apps_by_genre(dset_googleplay,dset_appstore):
    print("Our goal in this data analysis is to determine what kinds of apps that are likely to attract more users both in google play and app store");
    print("First off, we will use a frequency table function which will display our genre percentage in ascending order.");

    print("\n<Frequency Table analysis based on common apps by genre>\n>>AppStore");
    display_table(dset_appstore,11);

    print("\n--Analysis--"); #ANALYSIS

    print("As we can see here that more than half of the apps are Games (58.16%) followed by Entertainment (7.88%), Photo & video apps (4.97%) and the rest.");
    print("This means that the Appstore is primarily dominated by apps that are designed for fun while apps that are designed for education or practical purposes are quite a few.");
    print("However, this does not mean that this genre has the greatest number of users.");
    print("\n--End Analysis--\n");
    print("Let's continue on with the analysis on googleplay on both genres and category");
    
    print(">>Google Play - Category");
    display_table(dset_googleplay,1);
    print("\n>>Google Play - Genres");
    display_table(dset_googleplay,9);
    print("\n--Analysis--");
    print("Starting with the Categories table, we can see that there are not much apps that are designed for fun are present. However there are a good number of apps that are designed for practical purposes [family (18.9%), tools (8.46%), business(4.59%), etc.]");
    print("Practical apps have a better representation when we look at the Genres table.");
    print("Though the differences between the Genres and Category tables are not much refined however one thing we noticed is that the Genres columns is much more granular thus we will work with the Category column from now on.");
    
    print("\n--End Analysis--\n"); #ANALYSIS  

def popular_apps_appstore(dset_appstore,index):
    print("\n<Analysis on Most Popular Apps by Genre on App Store>");
    print("To find out which genres in the Appstore is the most popular(or have more users) is to calculate the number of installs for each genre.");
    print("However, this information is not available on this dataset unlike on the Googleplay dataset.\nA workaround for this is that we will take the total number of users as proxy (rating_count_tot column).");
    
    print("\n>>AppStore");
    genre_ios(dset_appstore,index);

    print("\n--Analysis--"); #ANALYSIS

    print("As we can see here that the navigation apps has the highest number of user reviews followed by social networking.");
    print("However, these navigation apps may be influenced by certain apps like WAZE and GOOGLE MAPS. See below:\n");
    
    ios_specific_genre(dset_appstore,index,'Navigation');
    
    print("\nThis applies to Social Networking apps as well like FACEBOOK and other social media apps. See below:\n");
    ios_specific_genre(dset_appstore,index,'Social Networking');
    
    print("Our goal is to find popular genres so it seems that navigation and social networking apps are popular than they really are.");
    print("The average number of ratings seems to be skewed by a very few apps which have hundreds of thousands of user ratings.");
    print("On the other hand, let's take a look at the reference apps below which has around 74942 user ratings.");
    ios_specific_genre(dset_appstore,index,'Reference');

    print("\nAs we can see here, It is skewed up by certain apps like the BIBLE and DICTIONARY.COM. However, this genre may show some potential. One thing is that we can make an app derived from a popular book. Aside from the raw book itself, we can add features like an audiobook version, daily quotes, etc.");
    print("This idea seems to fit well because the App Store is particularly dominated by fun and entertainment apps.");
    print("Although the app store is saturated by for fun apps, building a practical app may have more chance to stand out in the App Store");
    
    print("\n--End Analysis--\n"); #ANALYSIS

def popular_apps_googleplay(dset_googleplay,index1,index2):
    print("\n<Analysis on Most Popular Apps by Genre on App Store>");
    print("To find out which genres in the Appstore is the most popular(or have more users) is to calculate the number of installs for each genre.");
    print("There are good news and bad news about this. The good news is that there are data about the number of installs for each upp. The bad news however is that the numbers aren't as precise enough.See below:");
    display_table(dset_googleplay,5);
    print("\nAs we can see here that most of the values are open-ended thus are not precise. ");
    print("However, we don't need very precise data for our purposes therefore we'll only get the idea of which app genres that are likely to attract the most users.");
    print("So what we are going to do here is that we will leave the data as it is. However, in order to perform computations, we'll need to convert each install number into float.");
    print("Here's is the table analysis with the installs converted.See below:\n>>Googleplay\n");
    categories_gplay(dset_googleplay,index1);
    
    print("\n--Analysis--"); #ANALYSIS
    
    print("Alright, we can see here that on average, communication apps have the most installs at 38,456,119. As always it is skewed up by few apps like FACEBOOK, SKYPE, WHATSAPP and more. Let's take a look below as an example:");
    gplay_specific_genre(dset_googleplay,'COMMUNICATION','1,000,000,000+','500,000,000', '100,000,000');

    print("When we remove all the communication apps that have over 100m installs, the average will be reduced around 10x");

    under_100m = [];

    for app in dset_googleplay:
        no_installs = app[5];
        no_installs = no_installs.replace(',','');
        no_installs = no_installs.replace('+','');
        if (app[1] == 'COMMUNICATION') and (float(no_installs) < 100000000):
            under_100m.append(float(no_installs));
    print(sum(under_100m) / len(under_100m));

    print("\nWe can see the same pattern as well from other genres like video players, social apps, and photography apps where the market is dominated by large apps(example is Youtube and Google Play Movies).");
    print("On the other hand, the books and reference genre looks fairly popular as well (average of 8,767,811).It is interesting to explore this more as we found this genre has some potential to work well on the Appstore.See below:");
    
    for app in dset_googleplay:
        if app[1] == 'BOOKS_AND_REFERENCE':
            print(app[0], ':', app[5]);
    
    print("\nThis genre includes a good number of apps like ebooks, libraries, dictionaries, and more. It also seems that there's a small number of extremely popular apps that skewed the average:\n");

    gplay_specific_genre(dset_googleplay,'BOOKS_AND_REFERENCE','1,000,000,000+','500,000,000+','100,000,000+');

    print("\nIt seems that there are only a few popular apps, so this market still shows potential. Let's try to check some apps that is somewhere in the middle in terms of popularity. This is between 1,000,000 to 100,000,000 installs:\n");

    for app in dset_googleplay:
        if app[1] == 'BOOKS_AND_REFERENCE' and (app[5] == '1,000,000+' or app[5] == '5,000,000+' or app[5] == '10,000,000+' or app[5] == '50,000,000+'):
            print(app[0], ':', app[5]);

    print("\nAs we can see here that the market is already full of libraries therefore on our app, we need to add some special features in order to differentiate it from the rest.");  
    print("\n--End Analysis--"); #ANALYSIS
    print("""\nPlease select option '4' for the conlusion of the analysis.""");

def analysis_conclusion():
    print("\n<Profitable App Profiles for the App Store and Google Play Market - CONCLUSION>");
    print("In this data analysis, we concluded that creating a book app (referencing from a more recent but popular book) could be profitable for both Google Play and the App Store markets.");
    print("Of course, the book app will include additional features that will further distinguish it from the rest of the apps already in that specific genre.");
    print("Features such as daily quotes from the book, an audio version, quizzes and more.\n");

def analysis_dataset(u_input,dset_googleplay,dset_appstore):
    if (u_input == '1'):
        common_apps_by_genre(dset_googleplay,dset_appstore);
    elif (u_input == '2'):
        popular_apps_appstore(dset_appstore,11);
    elif (u_input == '3'):
        popular_apps_googleplay(dset_googleplay,1,9);
    elif (u_input == '4'):
        analysis_conclusion();