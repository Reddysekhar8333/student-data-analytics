import pandas as pd
import streamlit as st
import plotly.express as px

# data sorting
def quick_sort(data,key,reverse=False):
    if len(data) <= 1:
        return data
    pivot = data[len(data)//2][key]
    if not reverse:
        left = [x for x in data if x[key] < pivot]
        right = [x for x in data if x[key] > pivot]
    else:
        left = [x for x in data if x[key] > pivot]
        right = [x for x in data if x[key] < pivot]
    middle = [x for x in data if x[key] == pivot]
    # recursive calls
    return quick_sort(left,key,reverse) + middle + quick_sort(right,key,reverse)

# data
data = [
    {"student": "reddy", "GPA": 9.8, "credits": 120, "course": "BCA"},
    {"student": "venky", "GPA": 8.3, "credits": 90, "course": "BSC"},
    {"student": "balu", "GPA": 8.7, "credits": 93, "course": "BCOM"},
    {"student": "prakash", "GPA": 9.0, "credits": 116, "course": "BCA"},
    {"student": "sony", "GPA": 7.1, "credits": 67, "course": "BCA"},
    {"student": "ramya", "GPA": 7.8, "credits": 73, "course": "BCA"},
    {"student": "latha", "GPA": 9.3, "credits": 99, "course": "BCOM"},
    {"student": "sweety", "GPA": 9.3, "credits": 110, "course": "BSC"},
    {"student": "chinni", "GPA": 9.0, "credits": 106, "course": "BCCA"},
    {"student": "rahul", "GPA": 8.9, "credits": 101, "course": "BCCA"},
    {"student": "lakshmi", "GPA": 8.3, "credits": 91, "course": "BZC"},
    {"student": "pranavi", "GPA": 8.4, "credits": 89, "course": "BZC"},
    {"student": "sekhar", "GPA": 8.3, "credits": 86, "course": "BCA"},
    {"student": "pujitha", "GPA": 7.1, "credits": 65, "course": "BSC"},
    {"student": "sindu", "GPA": 7.9, "credits": 79, "course": "BCCA"},
    {"student": "mahesh", "GPA": 8.3, "credits": 86, "course": "BCCA"},
    {"student": "ganesh", "GPA": 9.5, "credits": 118, "course": "BZC"},
    {"student": "sivaji", "GPA": 9.3, "credits": 108, "course": "BZC"},
]
# -- UI --
st.set_page_config(page_title="Academic Analytics", layout="wide")
st.title("Academic Analytics Dashboard")
st.markdown("students performance and grade")

# side bar
st.sidebar.header("filter & sort")
sort_metric =st.sidebar.selectbox("sort by", ["GPA","credits"])
order = st.sidebar.radio("order", ["desending", "ascending"])

# data processing
is_reversed = True if order == "desending" else False
sorted_data = quick_sort(data, sort_metric, reverse=is_reversed)
df = pd.DataFrame(sorted_data)

# dash board
col1, col2 = st.columns([1,1])
with col1:
    st.subheader("student ranking")
    st.table(df)
with col2:
    st.subheader("GPA vs credits")
    fig = px.scatter(
        df,x="credits", y="GPA", color="course", size="GPA", hover_name="student", 
        color_discrete_sequence=px.colors.qualitative.Pastel 
    )
    st.plotly_chart(fig,use_container_width=True)

# grade trends
st.divider()
st.subheader("Academic Trend Analysis")
trend_fig = px.bar(df, x="student", y="GPA", color="GPA", title="GPA by student")
st.plotly_chart(trend_fig, use_container_width=True)

