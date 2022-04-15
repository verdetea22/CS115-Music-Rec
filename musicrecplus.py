#  Mikayla Mount, Joseph Carbonell
# CS115 
# I pledge my Honor that I have abided by the Stevens Honor System.

import os.path
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
    
def preference_input(userName, userMap):
    """prompts user to enter their liked artists, replacing old preferences if they exist
        input userMap= list storing user data  []
        input userName = specific user id (string)
        author: Mikayla M
    """
    bandList = []
    band = input("Enter an artist that you like, or press Enter to quit  : " )
    
    while band!="":
        bandList.append(band.strip().title())
        band = input("Enter another artist that you like, or press Enter to quit : " )
        
    bandList.sort()
    userMap[userName] = bandList

    return userMap
    
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

def delete_preference(userName, userMap):
    """ returns users preferences and deletes specific artists based on input
        input userMap= list storing user data  []
        input userName = specific user id (string)
        author: Mikayla M
    """
    pass

###################################################

def create_reccomendations(userName, userMap):
    """ returns reccommended artists, if no preferences then return no rec
        input userMap= list storing user data  []
        input userName = specific user id (string)
        author: 
    """
    pass

###################################################

def most_popular(userMap):
    """returns most popular artist 
       input userMap= list storing user data  []
       author: 
    """
    pass

###################################################

def most_popular_stat(userMap):
    """returns how many people like the most popular artist
       input userMap= list storing user data  []
       author: 
    """
    pass

###################################################

def user_most_artists(userMap):
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
    #userData = loadUsers('musicrecplus.txt')
    username = input("Hi  user! \nEnter your username, and use $ as a suffix if you would like you preferences to be private :  "    )   
    menu()
                   
                     
                        

###################################################            

main()
