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
    {"student": "balu", "GPA": 5.7, "credits": 93, "course": "BCOM"},
    {"student": "prakash", "GPA": 9.0, "credits": 116, "course": "BCA"},
    {"student": "sony", "GPA": 7.1, "credits": 67, "course": "BCA"},
    {"student": "preethi", "GPA": 7.8, "credits": 73, "course": "BCA"},
    {"student": "latha", "GPA": 4.3, "credits": 99, "course": "BCOM"},
    {"student": "sweety", "GPA": 8.3, "credits": 110, "course": "BSC"},
    {"student": "chinni", "GPA": 9.0, "credits": 106, "course": "BCCA"},
    {"student": "rahul", "GPA": 5.9, "credits": 101, "course": "BCCA"},
    {"student": "lakshmi", "GPA": 8.3, "credits": 91, "course": "BZC"},
    {"student": "pranavi", "GPA": 8.4, "credits": 89, "course": "BZC"},
    {"student": "sekhar", "GPA": 8.3, "credits": 86, "course": "BCA"},
    {"student": "pujitha", "GPA": 7.1, "credits": 65, "course": "BSC"},
    {"student": "sindu", "GPA": 4.9, "credits": 79, "course": "BCCA"},
    {"student": "mahesh", "GPA": 8.3, "credits": 86, "course": "BCCA"},
    {"student": "ganesh", "GPA": 5.5, "credits": 118, "course": "BZC"},
    {"student": "sivaji", "GPA": 6.3, "credits": 108, "course": "BZC"},
]
# -- UI --
st.set_page_config(page_title="Academic Analytics", layout="wide")
st.title("Academic Analytics Dashboard")
st.markdown("students performance and grade")

# -- side bar --
st.sidebar.header("filter & sort")
# 1. search bar feature
search_query = st.sidebar.text_input("Search Student or Course", "").lower()
# 2. sort controls
sort_metric =st.sidebar.selectbox("sort by", ["GPA","credits"])
order = st.sidebar.radio("order", ["desending", "ascending"])

# -- data processing --

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
        color_discrete_sequence=px.colors.qualitative.Vivid
    )
    st.plotly_chart(fig,use_container_width=True)

# grade trends
st.divider()
st.subheader("Academic Trend Analysis")
trend_fig = px.bar(df, x="student", y="GPA", color="GPA", title="GPA by student")
st.plotly_chart(trend_fig, use_container_width=True)

# --- Course wise Analysis ---
st.divider()
st.subheader("Course-wise Performance")

# Grouping data using Pandas
# calculate the mean GPA and count the number of students per course
course_stats = df.groupby("course").agg({
    "GPA": "mean",
    "student": "count"
}).reset_index().rename(columns={"student": "student_count"})

# columns for side-by-side course charts
c1, c2 = st.columns(2)

with c1:
    # Bar chart for average GPA per course
    fig_avg_gpa = px.bar(
        course_stats, 
        x="course", 
        y="GPA", 
        title="Average GPA by Course",
        color="GPA",
        color_continuous_scale="Viridis"
    )
    st.plotly_chart(fig_avg_gpa, use_container_width=True)

with c2:
    # Bar chart for student Count per course
    fig_count = px.bar(
        course_stats, 
        x="course", 
        y="student_count", 
        title="Student Distribution by Course",
        labels={"student_count": "Number of Students"},
        color_discrete_sequence=["#62FF5A"]
    )
    st.plotly_chart(fig_count, use_container_width=True)