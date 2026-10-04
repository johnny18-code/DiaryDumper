
import streamlit as st
import os
import time
import platform

# Utilities

import utils.functions as mainFunction


valid_user = mainFunction.RetrieveValidUsers()


st.set_page_config("Main Page")


@st.fragment(key="create")
@st.dialog("Create Account")
def accountCreation():
    # task def on change check if user is valid.
    def check_name_on_change():
        check_name = st.session_state["preferred_name"]
        valid_user = mainFunction.RetrieveValidUsers()
        if check_name in valid_user:
            if "name_taken" not in st.session_state:
                st.session_state["name_taken"] = True

            else:
                st.session_state["name_taken"] = True

        else:
            if "name_taken" not in st.session_state:
                st.session_state["name_taken"] = False
            else:
                st.session_state["name_taken"] = False

    ########################################################################

    username: str = st.text_input(
        "Choose your name", on_change=check_name_on_change, key="preferred_name")
    password = st.text_input("Choose your password",  type="password")
    retype_password = st.text_input("Re-type password", type="password")

    if "name_taken" not in st.session_state:
        st.session_state["name_taken"] = False
    else:
        if st.session_state["name_taken"] == True:
            st.warning(
                "This username is already taken, please use another name")
        else:
            pass

    if st.button("Create the account"):

        if username in valid_user:
            st.warning(
                "This username is already taken, please use another name")
        elif username not in valid_user:

            if password != retype_password:
                st.warning(
                    "Password Mismatched: Please re-type your password ")
            else:
                st.write("Creating your account now.")

                accountCreated = mainFunction.createAccount(username, password)
                if accountCreated == "Sucess":
                    st.success("Your account is created")
                    time.sleep(4)
                    st.rerun()
                else:
                    st.error("Apologies, try sometime... unknown issue occured")
                    time.sleep(4)
                    st.rerun()


def HeroLoginScreen():
    st.header("Hello, DiaryDumper! ")

    st.text_input("Please enter your username: ", key="user_credentials")
    st.text_input("Please enter your password: ",
                  key="user_password", type="password")

    buttons = [st.button("Login"), st.button("Create Account")]
    if buttons[0]:
        # Login Check
        if st.session_state["user_credentials"] in valid_user:

            can_logged_in = mainFunction.loginCheck(
                st.session_state["user_credentials"], st.session_state["user_password"])

            if can_logged_in == "Yes":

                if "is_Login" not in st.session_state:
                    st.session_state["is_Login"] = True

                if "current_user" not in st.session_state:
                    st.session_state["current_user"] = st.session_state["user_credentials"]

                st.info("Logging you in...")

            elif can_logged_in == "No":
                st.error("Invalid Password")
            elif can_logged_in == "Password not Set":
                st.info("Password txt not set")
            else:
                st.error("Faced unknown issue, contact Johnny :(")

            time.sleep(3)
            st.rerun()

        else:
            print("Not a valid User")

    elif buttons[1]:
        # call the pop-up
        accountCreation()


# think of it like it acts like a page
def accountPage():

    st.header(f"Hello, {st.session_state["current_user"].capitalize()}! 👋🏻")
    diaryDump = st.text_area(
        "Ready to share your thoughts for today?", key="text_area")

    if st.button("Publish"):
        publishStory = mainFunction.PublishStory(
            st.session_state["current_user"], diaryDump)
        match publishStory:
            case "Appended":
                st.success("Your story got appended for today.")
            case "Successful":
                st.success("Your story got created for today.")
            case _:
                st.warning(
                    "Unknown error occured -- Account Page, try again later ")

        if "text_area" in st.session_state:
            del st.session_state["text_area"]

            if "text_area" not in st.session_state:
                st.session_state.text_area = ""

        time.sleep(1)
        st.rerun()

    elif st.button("Logout"):

        del st.session_state["is_Login"]
        del st.session_state["current_user"]
        st.rerun()
# end account page function


HeroLoginPage = st.Page(HeroLoginScreen)

accountPagePG = st.Page(accountPage, title="Main Page 😃")


feelingRout = ""
if platform.system() == "Windows":
    feelingRout = f"routes\\feelings.py"
elif platform.system() == "Linux":
    feelingRout = "routes/feelings.py"
else:
    feelingRout = "will error"


feelingsPage = st.Page(page=f"{feelingRout}",
                       title="Check your feelings stat ❤️")


if "is_Login" not in st.session_state:

    pg = st.navigation([HeroLoginPage])

else:

    pg = st.navigation(
        {"Account": [accountPagePG],
         "Feelings": [feelingsPage]

         })


pg.run()  # this will render the PG pages.
