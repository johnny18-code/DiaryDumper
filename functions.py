
import os
import datetime as dt


def createUserFolder(userParam):
    userName = str(userParam)
    current_directory = os.getcwd()
    try:
        os.makedirs(f"{current_directory}\\users\\{userName}")
        return "Success"
    except FileNotFoundError as e:
        print(e)
        return "Failed"


def listUsers():
    current_directory = os.getcwd()
    path = f"{current_directory}\\users\\"

    return os.listdir(path)


def publish(diaryParm, userLibraryParm):
    print("Publish function")

    currentDate = str(dt.datetime.now())
    fileDate = currentDate[:10]

    workingDirectory = os.getcwd()

    path = os.path.join(workingDirectory, f"users\\{userLibraryParm}\\")
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
        return "Failed"


def getUserFolderDate(userParm):
    print("Get User data Folder")
    print("Return array of tupples")
    currentDate = str(dt.datetime.now())
    fileDate = currentDate[:10] + ".txt"
    returnDates = []
    returnContent = []
    cwd = os.getcwd()
    joinUserFolder = os.path.join(cwd, "users")
    joinSpecificUser = os.path.join(joinUserFolder, userParm)
    print(joinSpecificUser, fileDate)

    listLoop = os.listdir(f"{joinSpecificUser}\\")
    if len(listLoop) == 0:
        print("no data yet")
        returnDates.append(fileDate)
        returnContent.append("Today is kinda mild.")
        return (returnDates, returnContent)
    else:
        for content in listLoop:
            with open(f"{joinSpecificUser}\\{content}", "r") as readFile:
                returnDates.append(content.strip(".txt"))
                data = readFile.read()
                returnContent.append(data)

        return (returnDates, returnContent)


#
# getUserFolderDate("da")
