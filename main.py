'''You are tasked with creating a Data Entry application using
Streamlit for managing employee and department data.
The application should consist of three pages, each serving specific functionalities.
● The Employee data entry page should allow users to input information such
as Employee Number (Empno), Employee Name (Ename), Job, and
Department Number (Deptno).
● The Department data entry page should enable users to input data for
departments, including Department Number (Deptno), Department
Name(dname), and Location(loc).
● Finally, the third page should visualize the joined employee and department
data table based on the common 'Deptno' field.
'''

import os
import streamlit as st
import pandas as pd

employee_data = pd.read_csv('employee.csv') if os.path.exists(
    'employee.csv') else pd.DataFrame(columns=["Empno", "Ename", "Job", "Deptno"])
department_data = pd.read_csv('department.csv') if os.path.exists(
    'department.csv') else pd.DataFrame(columns=["Deptno", "Dname", "Loc"])


# Page 1: Employee Data Entry
def employee_data_entry():
    st.header("Employee Data Entry")
    empno = st.text_input("Employee Number (Empno)")
    ename = st.text_input("Employee Name (Ename)")
    job = st.text_input("Job")
    deptno = st.text_input("Department Number (Deptno)")

    if st.button("Add Employee"):
        if empno and ename and job and deptno:
            # Add data to employee_data DataFrame
            employeedata = employee_data.append(
                {"Empno": empno, "Ename": ename, "Job": job, "Deptno": deptno}, ignore_index=True)
            employeedata.to_csv('employee.csv', index=False)
            st.success(f"Employee '{ename}' added successfully!")
        else:
            st.error("All fields are required.")

# Page 2: Department Data Entry
def department_data_entry():
    st.header("Department Data Entry")
    deptno = st.text_input("Department Number (Deptno)")
    dname = st.text_input("Department Name (Dname)")
    loc = st.text_input("Location (Loc)")

    if st.button("Add Department"):
        if deptno and dname and loc:
            # Add data to department_data DataFrame
            departmentdata = department_data.append(
                {"Deptno": deptno, "Dname": dname, "Loc": loc}, ignore_index=True)
            departmentdata.to_csv('department.csv', index=False)
            st.success(f"Department '{dname}' added successfully!")
        else:
            st.error("All fields are required.")


# Page 3: Display Joined Data
def display_joined_data():
    st.header("Joined Employee and Department Data")
    joined_data = pd.merge(
            employee_data, department_data, on="Deptno", how="inner")
    st.dataframe(joined_data)


# Main Application
def main():
    st.title("Data Entry Application")

    # Add navigation menu for different pages
    page = st.sidebar.selectbox("Select a Page", ["Employee Data Entry", "Department Data Entry", "Display Joined Data"])

    if page == "Employee Data Entry":
        employee_data_entry()
    elif page == "Department Data Entry":
        department_data_entry()
    elif page == "Display Joined Data":
        display_joined_data()

if __name__ == "__main__":
    main()
