
import os
import platform
import datetime

WINDOWS = "Windows"
JAVA = "Java"
LINUX = "Linux"

# Repetitive check to OS version
# will refactor once not get lazy.

current_working_directory = os.getcwd()
current_operating_system = platform.system()


def RetrieveValidUsers():
    # This function retrieves valid Users based that are currently residing in users folders
    if current_operating_system == WINDOWS:
        pathUsers = os.path.join(current_working_directory, "users\\")
        return os.listdir(pathUsers)

    elif current_operating_system == LINUX:
        pathUsers = os.path.join(current_working_directory, "users/")
        # print(os.listdir(users_path))
        return os.listdir(pathUsers)
    elif current_operating_system == JAVA:
        return "Unwanted OS"
    else:
        return "Unwanted OS"

###########


def PublishStory(parmUser, parmDiary):
    # This will Publsh the user diary
    current_date = str(datetime.datetime.now())
    current_date_extract = current_date[0:10] + ".txt"

    pathUsers = ""
    pathWrite = ""

    if current_operating_system == WINDOWS:
        pathUsers = os.path.join(
            current_working_directory, f"users\\{parmUser}")
        pathWrite = pathUsers + "\\"
    elif current_operating_system == LINUX:
        pathUsers = os.path.join(
            current_working_directory, f"users/{parmUser}")
        # print(os.listdir(users_path))
        pathWrite = pathUsers + "/"
    elif current_operating_system == JAVA:
        print("No current path set for Java")
    else:
        print("Unexpected OS")

    if current_date_extract in os.listdir(pathUsers):
        # means the file exist? do append?
        with open(f"{pathWrite}{current_date_extract}", mode="a") as file:
            file.write(parmDiary + "\n")
        return "Appended"
    else:
        # create?
        with open(f"{pathWrite}{current_date_extract}", mode="w") as file:
            file.write(parmDiary + "\n")
        return "Successful"

################


def createAccount(chosenName, chosenPassword):
    print("account creation")
    # this will create a directory
    # and inside of it, it will have a password txt
    # logic when entering username and password?
    # when user type valid username -- check ,traverse to his personal folder and find txt password
    # then retrieve that password for him
    pathUsers = ""
    pathWrite = ""
    if current_operating_system == WINDOWS:
        pathUsers = os.path.join(
            current_working_directory, "users")

    elif current_operating_system == LINUX:
        pathUsers = os.path.join(
            current_working_directory, f"users")
        # print(os.listdir(users_path))

    elif current_operating_system == JAVA:
        print("No current path set for Java")
    else:
        print("Unexpected OS")

    # make directory
    try:
        makedir = os.path.join(pathUsers, f"{chosenName}")
        os.mkdir(makedir)
        if current_operating_system == WINDOWS:
            pathWrite = makedir + "\\"
        elif current_operating_system == LINUX:
            pathWrite = makedir + "/"
    except FileExistsError as e:
        print(e)

    print(pathWrite)

    with open(f"{pathWrite}password.txt", mode="w") as file:
        file.write(chosenPassword)

    return "Sucess"

##########


def loginCheck(parmUser, parmPassword):
    # get teh user name
    # get the path
    # get the password for that user name
    # if the user_password match the user_password txt
    # go login
    print("LoginCheck")
    print(parmUser, parmPassword)
    pathUsers = ""
    pathWrite = ""
    if current_operating_system == WINDOWS:
        pathUsers = os.path.join(
            current_working_directory, f"users\\{parmUser}\\")
    elif current_operating_system == LINUX:
        pathUsers = os.path.join(
            current_working_directory, f"users/{parmUser}/")
        # print(os.listdir(users_path))
    elif current_operating_system == JAVA:
        print("No current path set for Java")
    else:
        print("Unexpected OS")

    if "password.txt" in os.listdir(pathUsers):
        # match the password here?
        with open(f"{pathUsers}password.txt") as readfile:
            password = readfile.read()
            print("This is the password? ", password)
        if parmPassword == password:
            return "Yes"
        else:
            return "No"
    else:
        return "Password not Set"

# retrieve dieries


def retrieveDieries(parmUser):
    # retrieve all txt-date file except password
    # return as tuples( date, content)
    print("retrieveDiaries")

    pathUsers = ""
    pathRead = ""
    if current_operating_system == WINDOWS:
        pathUsers = os.path.join(
            current_working_directory, f"users\\{parmUser}\\")
        pathRead = pathUsers
    elif current_operating_system == LINUX:
        pathUsers = os.path.join(
            current_working_directory, f"users/{parmUser}/")
        # print(os.listdir(users_path))
        pathRead = pathUsers
    elif current_operating_system == JAVA:
        print("No current path set for Java")
    else:
        print("Unexpected OS")

    diaries = os.listdir(pathRead)
    diaries.remove("password.txt")

    # print(diaries)
    content = []
    for diary in diaries:
        with open(f"{pathUsers}{diary}", mode="r") as readFile:
            data = readFile.read()
            content.append((diary, data))

    return content
