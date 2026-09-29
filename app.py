# This is check if the username already existing
# if not then create?


from nltk.sentiment import SentimentIntensityAnalyzer
import functions as SubMod
from ast import Sub
from numpy import positive
from streamlit.delta_generator import DeltaGenerator


import time
import streamlit as st
import datetime
import plotly.express as px
import nltk
nltk.download('vader_lexicon')

analyzer = SentimentIntensityAnalyzer()
# sub-mod

currentDate = datetime.datetime.now().strftime("%d %B, %Y")
userList = SubMod.listUsers()
st.write(userList)
positiveScores = []


@st.dialog("Creating wonder name~", on_dismiss="rerun")
def checkUser():

    createUser = st.text_input("Decide your name")
    # debug start
    debugResult = SubMod.debugPullDirectories(createUser)
    st.write(debugResult)
    # debug end
    if st.button("Create user account"):
        time.sleep(1.3)
        st.write("Checking user name...")
        time.sleep(1.3)
        st.write("Give me some time...")
        time.sleep(1.3)
        st.write("Here I go!")
        time.sleep(1.3)
        if createUser not in userList:
            st.write("This name can be used :)")
            time.sleep(1)
            st.write(f"{createUser} is registered. Do not forget it!!!")
            # call createPersonal folder
            createFolder = SubMod.createUserFolder(createUser)
            if createFolder == "Success":
                st.write("Folder Created")
                st.write("You can close this modal and try to login!")
                # just return success
                return createFolder
            else:
                st.error("Failed on creating folder")
        else:
            st.error("Toink, please use another name")


if "userLoggedIn" not in st.session_state:
    st.header("Welcome, Diary Dumper!", text_alignment="center")
    userInput = st.text_input("Place your wondername")
    if st.button("Login"):
        if userInput in userList:
            # logging you in~
            print("here")
            if "current_user" not in st.session_state:
                st.session_state["current_user"] = userInput
                st.session_state["userLoggedIn"] = True
                st.rerun()
        else:
            st.warning(
                "If you want to use this name, create account using this!")
            time.sleep(5)
            st.rerun()
    elif st.button("Create account"):
        result = checkUser()
        if result == "Success":
            st.rerun()


else:
    st.header(f"Bonjour! {st.session_state["current_user"].capitalize()} 👋🏻")
    # call user data?
    userContent = SubMod.getUserFolderDate(st.session_state["current_user"])
    diaryInput = st.text_area(
        label=currentDate, placeholder="Ready to share your thoughts for today?", key="text_area")
    print(diaryInput)
    if st.button("Publish"):
        print("Writing to your directory~")
        publishResult = SubMod.publish(
            diaryInput, st.session_state["current_user"])
        if publishResult == "Success":
            st.success("Your feelings have been recorded ☺️")
            time.sleep(2)
            st.rerun()

        else:
            st.error("Sorry, but we have encountered error 🙁")
            time.sleep(2)
            st.rerun()

    for para in userContent[1]:
        score = analyzer.polarity_scores(para)
        positiveScores.append(score["pos"])

    # plot here?
    st.subheader("Mood Tone")
    figurePos = px.line(x=userContent[0], y=positiveScores, labels={
                        "x": "Date", "y": "Positivity!"})
    # to show hte chart in Streamlit
    st.plotly_chart(figurePos)

    # logout
    if st.button("Logout", type="secondary"):
        st.write("Logging you out...")
        del st.session_state["userLoggedIn"]
        del st.session_state["current_user"]
        del st.session_state["text_area"]
        time.sleep(5)
        st.rerun()


# plotting now
