def read_file(filename):
    myfile = open(filename,"r")
    contents =myfile.read()
    myfile.close()
    return contents


def read_file_v2(filename):
    with open(filename, "r") as f:
        return f.read()
    

def read_file_v3(filename):
    with open(filename, "r") as f:
        return f.readlines()


def read_file_v4(filename):
    with open(filename, "r") as f:
        for line in f:
            print(line.strip())

"""three groups of each user with their artist preferences w strip()"""
            

def write_file(string, filename):
    myfile  = open(filename, "w")
    myfile.write(string)
    myfile.close()

    """ w for writing mode """
    
def append_file(string, filename):
    myfile = open(filename,  "a")
    myfile.write(string)
    myfile.append(string)
    myfile.close()

    """ a for append """

x = "welcome to hell"
x.split(" ")
""" results ["welcome",  "to", "hell"]  """
l=["welcome",  "to", "hell"]
"-".join(l)
"""results in "welcome-to-hell" """


""" take in file, take name as  dictionary id and the music  pref as list elements"""
def read_pref(filename):
    dic ={}
    with open(filename, "r") as f:
        for line in f:
            [username, singers] = line.strip().split(":")
            singersList = singers.split(",")
            dic[username] = singersList
    return dic
    

