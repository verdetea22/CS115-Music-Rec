#  Mikayla Mount, Joseph Carbonell
# CS115 
# I pledge my Honor that I have abided by the Stevens Honor System.

import os.path

userName = ""
userDict = {}
###################################################

def loadUsers(fileName):
    """Reads in a file of stores users' preferences stored
       in the file 'fileName'.
       Returns a dictionary containing a mapping of user
       names to a list of preferred artists
       Author: Joseph C (from textbook)
    """
    file = open(fileName, 'r')
    userDict = {}
    for line in file:
        [userName,bands] = line.strip().split(":")
        bandList = bands.split(",")
        bandList.sort()
        userDict[userName] = bandList
    file.close()
    return userDict

###################################################

def saveUserPreferences(userName, prefs, userMap, fileName):
    """Writes all of the user preferences to the file
       Returns nothing.
       Author: Joseph C (from textbook)
    """
    userMap[userName] = prefs
    file = open(fileName, "w")
    for user in userMap:
        toSave = str(user) + ":" + ",".join(userMap[user]) + \
                 "\n"
        file.write(toSave)
    file.close()
    
 ###################################################
    
def preference_input():
    """prompts user to enter their liked artists, replacing old preferences if they exist
        input userMap= list storing user data  []
        input userName = specific user id (string)
        author: Mikayla M
    """
    global userName, userDict
    
    prefs = []
    
    while True:

        band = input("Enter an artist that you like (Enter to finish)  : " )

        if  band!="":
            prefs.append(band.strip().title())
            
        else:
            break
    
    if userName !="":
        userDict[userName] = sorted(list(set(prefs)))


    
###################################################

def print_preference(userName, userMap) :
    """ returns users most current artist preferences
        input userMap= list storing user data  []
        input userName = specific user id (string)
        author: Mikayla M
  """
    
    if userName in userMap:
        bandList = userMap[userName]
        return ("Here are your liked artists: /n") +bandList

    else:
        bandList = []
        band = input("Enter an artist that you like, or press Enter to quit  : " )
    
    while band!="":
        bandList.append(band.strip().title())
        band = input("Enter another artist that you like, or press Enter to quit : " )
        
    bandList.sort()
    userMap[userName] = bandList

###################################################

def create_reccomendations():
    """ returns reccommended artists, if no preferences then return no rec
        input userMap= list storing user data  []
        input userName = specific user id (string)
        author: 
    """
    pass

###################################################

def most_popular():
    """returns most popular artist 
       input userMap= list storing user data  []
       author: 
    """
    pass

###################################################

def most_popular_stat():
    """returns how many people like the most popular artist
       input userMap= list storing user data  []
       author: 
    """
    pass

###################################################

def user_most_artists():
    """ returns user with the most preferences, one per line and sorted if more than one
        input userMap= list storing user data  []
        author: 
    """
    pass

###################################################

def menu():
    """returns menu options
    author: Mikayla M """""
    
    print("""Enter a letter to choose an option:
    e - Enter preferences
    r - Get recommendations
    p - Show most popular artists
    h - How popular is the most popular
    m - Which user has the most likes
    q - Save and quit""")
    
def main():
    """ main method for menu, files, database and username
        authors: Mikayla M & Joseph C
    """
    if userDict  !={}:
        userData = loadUsers('musicrecplus.txt')

    username = input("Hi  user! \nEnter your username, and use $ as a suffix if you would like your preferences to be private :  "    )   
    menu()

    menu_choice = input()

    while menu_choice != "q":
          
        if menu_choice == "e":
            preference_input()

        elif menu_choice == "r":
            create_reccomendations()
            
        elif menu_choice == "p":
            most_popular()

        elif menu_choice == "h":
            most_popular_stat()

        elif menu_choice == "m":
            user_most_artists()

        else :
            print("Invalid input, please choose an option, or press q to quit")

        menu()
        menu_choice = input() 

###################################################            

main()
