# Academic Analytics Dashboard

This is a simple, to visualize student performance and course trends using Python. My goal with this project is to make academic data easy to understand.

---

### What this tool does:

- **Organizes Student Records:** Uses a custom-built **Quick Sort** algorithm to rank students by GPA or Credits.
- **Visualizes Progress:** Uses Plotly to create clear charts so we can see the "GPA vs. Credits" relationship at a glance.
- **Course Insights (New!):** I have added a feature to group students by their course (BCA, BCOM, BZC, etc.) to see how different departments are performing on average.

---

## Tools I used

I chose these tools because they are reliable and helps focus on the data:

- **Python:** The foundation of the logic.
- **Streamlit:** To create a clean, humble UI that anyone can use.
- **Pandas:** For grouping the students by their specific courses.
- **Plotly Express:** To make the academic trends colorful and easy to read.
- **Quick Sort:** A recursive algorithm I implemented to ensure the sorting is handled with care.

---

## How to Run it Locally

If you would like to try this on your own machine, please follow these steps:

1.  **Clone the work:**
    ```bash
    git clone [https://github.com/yourusername/academic-analytics.git](https://github.com/yourusername/academic-analytics.git)
    ```
2.  **Install the necessary requirements:**
    ```bash
    pip install streamlit pandas plotly
    ```
3.  **Start the dashboard:**
    ```bash
    streamlit run app.py
    ```

---

## A Note on Improvement

I am still learning every day. The current sorting method is recursive, and the charts are just the beginning. If you feel there is a better way to write this logic and represent charts, you can contribute to this project
