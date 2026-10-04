import utils.functions as mainFunction
from nltk.sentiment import SentimentIntensityAnalyzer

import streamlit as st
import plotly.express as px
import nltk
nltk.download('vader_lexicon')
import datetime

# initialize
analyzer = SentimentIntensityAnalyzer()

st.set_page_config("Feelings Window")
user_diaries = mainFunction.retrieveDieries(st.session_state["current_user"])
# Retrieve Mood / text files
# txt


# 

st.header(
    f"You are in Feelings.py {st.session_state["current_user"].capitalize()}")
# 

# scores - checks each file and append
# run every when you wanted to run auto
@st.fragment(key="feeling")
def feeling():
    print("click")
    print("run")
    st.write("Check your mood fluctuation.")
    user_diaries = mainFunction.retrieveDieries(st.session_state["current_user"])
    score_y_axis = []
    date_x_axis = []
    for diary in user_diaries:
        
        data = analyzer.polarity_scores(diary[1])
        score_y_axis.append(data["pos"])
        # extracting date before appending to date_y_axis / remove '.txt'

        extract_date = diary[0].strip(".txt")
    
        year = int(extract_date[0:4])
        month = int(extract_date[5:7])
        day = int(extract_date[8:10])
        
        date_x_axis.append(datetime.datetime(year=year,month=month,day=day).strftime("%b %d %Y"))
        
    figurePos = px.line(x=date_x_axis, y=score_y_axis, labels={
        "x": "Date", "y": "Mood"})
    st.plotly_chart(figurePos)
    



# PLOT AREA
if len(user_diaries) == 0:
    st.header("No diaries plotted")
else:
    feeling()
    st.button("Refresh",on_click=lambda: st.rerun("feeling"))
       


