import streamlit as st
import pandas as pd
import pymysql


def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="Temple123",
        database="placement"
    )


def execute_query(query):
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df    

st.title("Placement Eligibility App😎")
st.text("Hey there!")
st.text("Are you tired of manually searching for your students' data?🕵🏽‍♂️")
st.text("Fret not!") 
st.text("This app comes to your rescue to save your time.⏰") 
st.text("Fetch your required data within seconds and get going...💪🏽")

tab1, tab2 = st.tabs(["Quick filters📂", "Data insights📊"])

with tab1:
    mpcount = int(st.number_input("Mini projects count", step=1, format="%d", key = "mp"))
    if st.button("Search by Mini Projects"):
        query1 = f"""
        SELECT programming_id, student_id, language, mini_projects
        FROM programming_data
        WHERE mini_projects = {mpcount}
        """
        try:
            result_df = execute_query(query1)
            st.subheader("Students and their mini projects:")
            if not result_df.empty:
                st.dataframe(result_df)
            else:
                st.warning("No students match the mini projects criteria.")
        except Exception as e:
            st.error(f"Error: {e}")




    spcount = int(st.number_input("Number of solved problems", step=1, format="%d", key = "sp"))
    if st.button("Search by number of problems solved"):
        query2 = f"""
        SELECT programming_id, student_id, language, problems_solved
        FROM programming_data
        WHERE problems_solved = {spcount}
        """
        try:
            result_df = execute_query(query2)
            st.subheader("Students and the number of problems they solved:")
            if not result_df.empty:
                st.dataframe(result_df)
            else:
                st.warning("No students match the solved problems criteria.")
        except Exception as e:
            st.error(f"Error: {e}")

    
    
    icount = int(st.number_input("Internships count",  step=1, format="%d", key = "intern"))
    if st.button("Search by number of internships"):
        query3 = f"""
        SELECT placement_id, student_id, internships_completed
        FROM placement_data
        WHERE internships_completed = {icount}
        """
        try:
            result_df = execute_query(query3)
            st.subheader("Students and the number of internships they completed:")
            if not result_df.empty:
                st.dataframe(result_df)
            else:
                st.warning("No students match the solved problems criteria.")
        except Exception as e:
            st.error(f"Error: {e}")

    
    
    miscore = int(st.number_input("Mock interview score", step=1, format="%d", key = "mock"))
    if st.button("Search by mock interview score"):
        query4 = f"""
        SELECT placement_id, student_id, mock_interview_score
        FROM placement_data
        WHERE mock_interview_score = {miscore}
        """
        try:
            result_df = execute_query(query4)
            st.subheader("Students and their mock interview score:")
            if not result_df.empty:
                st.dataframe(result_df)
            else:
                st.warning("No students match the solved problems criteria.")
        except Exception as e:
            st.error(f"Error: {e}")

    
with tab2:
    queries = {"Students with critical thinking score > 90": "SELECT soft_skill_id, student_id, critical_thinking, teamwork, leadership FROM softskills_data WHERE critical_thinking > 90;",
               "Students who learned JAVA, SQL, & Python": "SELECT programming_id, student_id, language, problems_solved, latest_project_score FROM programming_data WHERE language = 'SQL, JAVA, PYTHON';",
               "Students who solved more than 450 problems": "SELECT programming_id, student_id, language, problems_solved, mini_projects FROM programming_data WHERE problems_solved > 450;",
               "Students who completed more than 5 internships": "SELECT placement_id, student_id, internships_completed, placement_status FROM placement_data WHERE internships_completed > 5;",
               "Students who are placed in MNOP company": "SELECT placement_id, student_id, placement_status, company_name, placement_package, placement_date FROM placement_data WHERE company_name = 'MNOP' AND placement_status = 'Placed';",
               "Students who have cleared 3 or more rounds of interview": "SELECT placement_id, student_id, mock_interview_score, interview_rounds_cleared FROM placement_data WHERE interview_rounds_cleared >= 3;",
               "Average presentation skills score": "SELECT AVG(presentation) AS average_presentation_skills_score FROM softskills_data;",
               "Average placement package": "SELECT AVG(placement_package) as average_placement_package FROM placement_data;",
               "Average mock interview score": "SELECT AVG(mock_interview_score) as average_mock_interview_score FROM placement_data;",
               "Students who are 'Placed' ": "SELECT placement_id, student_id, mock_interview_score, internships_completed, placement_status, company_name, placement_package, placement_date FROM placement_data WHERE placement_status = 'Placed';" 
    }
    
    selected_query = st.selectbox('Select a query:', list(queries.keys()))

    if st.button("Run Query"):
        with st.spinner("Fetching data..."):
            df = execute_query(queries[selected_query])
            st.success("Query executed successfully!")
            st.dataframe(df) 
                      


