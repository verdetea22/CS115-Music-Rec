#  Mikayla Mount, Joseph Carbonell, Kent Quach
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
       Author: Joseph C
    """
    userDict = {}
    if os.path.exists(fileName):
        if os.stat(fileName).st_size == 0:
            return userDict
        else:
            file = open(fileName, 'r')
            for line in file:
                [userName,bands] = line.strip().split(":")
                bandList = bands.split(",")
                bandList.sort()
                userDict[userName] = bandList
        file.close()
        return userDict
    else:
        file = open(fileName,'x')
        file.close()
        return userDict

###################################################

def saveUserPreferences(fileName):
    """Writes all of the user preferences to the file
       Returns nothing.
       Author: Joseph C
    """
    global userDict
    file = open(fileName, "w")
    for user in userDict:
        toSave = str(user) + ":" + ",".join(userDict[user]) + \
                 "\n"
        file.write(toSave)
    file.close()
    
 ###################################################
    
def preference_input():
    """prompts user to enter their liked artists, replacing old preferences if they exist
        author: Mikayla M edit by Joseph C
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
        input userDict = list storing user data  []
        input userName = specific user id (string)
        author: Kent Q (from textbook)
    """
    global userName, userDict
    if (userName in userDict.keys()) == False:
        return print("No preferences available at this time.")
    if len(userDict.keys()) == 1:
        return print("No preferences available at this time.")
    prefs = userDict.get(userName)
    bestUser = findBestUser()
    recommendations = drop(prefs, userDict.get(bestUser))
    for artist in recommendations:
        print(artist)

###################################################

def findBestUser():
    """ [HELPER FUNCTION] find the user whose tastes are closest to the current user. Return the best user's name (a string)
         author: Kent Q
    """
    global userName, userDict
    bestScore = -1
    prefs = userDict.get(userName)
    for user in userDict.keys():
        score = numMatches(prefs, userDict[user])
        if score > bestScore and userName != user:
            bestScore = score
            bestUser = user
    return bestUser

###################################################

def drop(list1, list2):
    """ [HELPER FUNCTION] return a new list that contains only the elements in list2 that were NOT in list1.
         author: Kent Q (from textbook)
    """
    list3 = []
    for item in list2:
        if ((item in list1) != True):
            list3 += [item]
    return list3
            

###################################################

def numMatches(list1, list2):
    """ [HELPER FUNCTION] return the number of elements that match between two sorted lists
         author: Kent Q (from textbook)
    """
    matches, i, j = 0, 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            matches += 1
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return matches

###################################################

def create_most_popular_list():
    """HELPER: returns list of artists sorted by most popular
       author: Joseph Carbonell
    """
    global userDict
    pop_dict = {}
    for user in userDict:
        if user[-1] != "$":
            for band in userDict[user]:
                if band in pop_dict:
                    pop_dict[band] += 1
                else:
                    pop_dict[band] = 1
    final_list = []
    if pop_dict:
        for key in pop_dict:
            final_list += [[pop_dict[key],key]]
        final_list.sort()
        final_list.reverse()
        return final_list
    else:
        return []

###################################################

def most_popular():
    """returns 3 most popular artists
       author: Joseph Carbonell
    """
    final_list = create_most_popular_list()
    if final_list != []:
        if len(final_list) < 3:
            for i in range(len(final_list)):
                print(final_list[i][1])
        else:
            for i in range(3):
                print(final_list[i][1])
    else:
        print("Sorry, no artists found.")
            
                
    

###################################################

def most_popular_stat():
    """returns how many people like the most popular artist
       author: Joseph Carbonell
    """
    final_list = create_most_popular_list()
    if final_list != []:
        print(final_list[0][0])
    else:
        print("Sorry, no artists found.")
    
    

###################################################

def user_most_artists():
    """ returns user with the most preferences, one per line and sorted if more than one
        input userMap= list storing user data  []
        author: Kent Q
    """
    global userDict
    
    len_likes = {}
    if len(userDict) != 0:
        for i in userDict:
            if i[-1] == '$':
                continue
            else:
                len_likes[i] = len(userDict[i])
        print(sorted(len_likes, key = len_likes.get, reverse = True)[0])
    else:
        print("Sorry, no user found.")

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
        authors: Mikayla M, Joseph C & Kent Q
    """
    global userName, userDict
    if userDict  == {}:
        userDict = loadUsers('musicrecplus.txt')

    userName = input("Hi  user! \nEnter your username, and use $ as a suffix if you would like your preferences to be private :  "    )   
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
    saveUserPreferences('musicrecplus.txt')

###################################################            

main()
