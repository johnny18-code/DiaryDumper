
import os
import datetime as dt
import platform

os_name = platform.system()
current_directory = os.getcwd()


def createUserFolder(userParam):
    userName = str(userParam)

    try:
        if os_name == "Windows":
            os.makedirs(f"{current_directory}\\users\\{userName}")
            return "Success"
        elif os_name == "Linux":
            os.makedirs(f"{current_directory}/users/{userName}")
            return "Success"
        else:
            return platform.system()

    except FileExistsError as e:
        print(e)
        return "Failed"


def listUsers():
    os_name = platform.system()

    try:
        if os_name == "Windows":
            path = f"{current_directory}\\users\\"
            return os.listdir(path)
        elif os_name == "Linux":
            path = f"{current_directory}/users/"
            return os.listdir(path)
        else:
            return platform.system()
    except FileNotFoundError as e:
        # {current_directory}/users
        # f"{current_directory}/users/
        return {e}


def publish(diaryParm, userLibraryParm):
    print("Publish function")

    currentDate = str(dt.datetime.now())
    fileDate = currentDate[:10]

    if os_name == "Windows":
        path = os.path.join(current_directory, f"users\\{userLibraryParm}\\")
    elif os_name == "Linux":
        path = os.path.join(current_directory, f"users/{userLibraryParm}/")
    else:
        return platform.system()

    checkCurrentDateFile = f"{path}{fileDate}.txt"
    try:
        if os.path.exists(checkCurrentDateFile):
            print("current file exist")
            print("appending today")
            with open(checkCurrentDateFile, mode="a") as file:
                file.write(f"{diaryParm} \n")
                return "Success"
        else:
            # this will create a new file for today
            print("creating new file for today")
            with open(checkCurrentDateFile, mode="w") as file:
                file.write(f"{diaryParm} \n")
                return "Success"
    except FileNotFoundError as e:
        return "FNFE - Failed"
    except Exception as e:
        return "Failed"


def getUserFolderDate(userParm):
    listLoop = ""
    print("Get User data Folder")
    print("Return array of tupples")
    currentDate = str(dt.datetime.now())
    fileDate = currentDate[:10] + ".txt"
    returnDates = []
    returnContent = []

    joinUserFolder = os.path.join(current_directory, "users")
    joinSpecificUser = os.path.join(joinUserFolder, userParm)
    print(joinSpecificUser, fileDate)

    if os_name == "Windows":
        listLoop = os.listdir(f"{joinSpecificUser}\\")
    elif os_name == "Linux":
        listLoop = os.listdir(f"{joinSpecificUser}/")

    if len(listLoop) == 0:
        print("no data yet")
        returnDates.append(fileDate)
        returnContent.append("Today is kinda mild.")
        return (returnDates, returnContent)
    else:
        for content in listLoop:
            if os_name == "Windows":
                with open(f"{joinSpecificUser}\\{content}", "r") as readFile:
                    returnDates.append(content.strip(".txt"))
                    data = readFile.read()
                    returnContent.append(data)
            elif os_name == "Linux":
                with open(f"{joinSpecificUser}/{content}", "r") as readFile:
                    returnDates.append(content.strip(".txt"))
                    data = readFile.read()
                    returnContent.append(data)

        return (returnDates, returnContent)


#
# getUserFolderDate("da")
