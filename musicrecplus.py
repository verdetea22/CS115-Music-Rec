#  Mikayla Mount, Joseph Carbonell
# CS115 
# I pledge my Honor that I have abided by the Stevens Honor System.

import os.path

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
 
def preference_input(db, username):
    """prompts user to enter their liked artists, replacing old preferences if they exist
        input db= database storing user data  (string)
        input username = specific user id (string)
        author: Mikayla M
    """
    pass



def print_preference(db, username):
    """ returns users most current artist preferences
        input db= database storing user data  (string)
        input username = specific user id (string)
        author: Mikayla M
    """
    pass



def delete_preference(db, username):
    """ returns users preferences and deletes specific artists based on input
        input db= database storing user data  (string)
        input username = specific user id (string)
        author: Mikayla M
    """
    pass


def create_reccomendations(db, username):
    """ returns reccommended artists, if no preferences then return no rec
        input db= database storing user data  (string)
        input username = specific user id (string)
        author: 
    """
    pass




def most_popular(db):
    """returns most popular artist 
       input db= database storing user data  (string)
       author: 
    """
    pass



def most_popular_stat(db):
    """returns how many people like the most popular artist
       input db= database storing user data  (string)
       author: 
    """
    pass



def user_most_artists(db):
    """ returns user with the most preferences, one per line and sorted if more than one
        input db= database storing user data  (string)
        author: 
    """
    pass




def main():
    """ main method for menu, files, database and username
        authors: Mikayla M & Joseph C
    """
    userData = loadUsers('musicrecplus.txt')
        
    

main()
