import streamlit as st
from utils import create_table, add_task, get_tasks, update_status, delete_task

st.set_page_config(layout="wide")

def main():
    st.title(" Streamlit To-Do App (SQLite3)")

    create_table()

    new_task = st.text_input("Enter a new task:", key="new_task_input")
    if st.button("Add Task"):
        if new_task.strip():
            add_task(new_task.strip())
            st.success(f"Task '{new_task}' added successfully!")
            st.rerun()
        else:
            st.warning("Task cannot be empty.")

    st.header("Task List")
    tasks = get_tasks()

    if not tasks:
        st.info("No tasks yet. Add a task above.")
    else:
        for task in tasks:
            task_id, task_name, task_status, created_at = task
            col1, col2, col3, col4 = st.columns([2, 4, 2, 1])

            with col1:
                st.write(f"ID: {task_id}  \nCreated at: {created_at.split('.')[0]}")

            with col2:
                st.write(f"Task Name: {task_name}")

            with col3:
                new_status = "Complete" if task_status == "Incomplete" else "Incomplete"
                if st.button(f"Mark as {new_status}", key=f"status_{task_id}"):
                    update_status(task_id, new_status)
                    st.success(f"Marked as {new_status.lower()}")
                    st.rerun()

            with col4:
                if st.button("X", key=f"delete_{task_id}"):
                    delete_task(task_id)
                    st.success("Task deleted.")
                    st.rerun()

            st.markdown("---")

if __name__ == "__main__":
    main()
