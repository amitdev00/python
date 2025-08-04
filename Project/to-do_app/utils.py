from datetime import datetime
import sqlite3

def get_connection():
    return sqlite3.connect("todo.db", check_same_thread=False)

def create_table():
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS TODO_INFO (
            TASK_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            TASK_NAME TEXT,
            TASK_STATUS TEXT,
            CREATED_AT DATETIME
        )
    """)
    conn.commit()
    conn.close()

def add_task(task):
    conn = get_connection()
    c = conn.cursor()
    current_time = datetime.now()
    c.execute("INSERT INTO TODO_INFO (TASK_NAME, TASK_STATUS, CREATED_AT) VALUES (?, ?, ?)",
              (task, 'Incomplete', current_time))
    conn.commit()
    conn.close()

def get_tasks():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT TASK_ID, TASK_NAME, TASK_STATUS, CREATED_AT FROM TODO_INFO")
    tasks = c.fetchall()
    conn.close()
    return tasks

def update_status(task_id, new_status):
    conn = get_connection()
    c = conn.cursor()
    c.execute("UPDATE TODO_INFO SET TASK_STATUS = ? WHERE TASK_ID = ?", (new_status, task_id))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute("DELETE FROM TODO_INFO WHERE TASK_ID = ?", (task_id,))
    conn.commit()
    conn.close()
