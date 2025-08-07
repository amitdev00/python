import sqlite3
import random

conn = sqlite3.connect("bank.db", check_same_thread=False)
cursor = conn.cursor()

def create_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS users ( account_number TEXT PRIMARY KEY, name TEXT, dob TEXT,
        email TEXT, phone TEXT,  address TEXT, account_type TEXT, balance REAL,
        branch TEXT, pin TEXT)""")
    conn.commit()

def insert_user(data):
    cursor.execute('SELECT 1 FROM users WHERE account_number = ?', (data[0],))
    if cursor.fetchone():
        return False
    else:
        cursor.execute('INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', data)
        conn.commit()
        return True


def get_pin(account_number):
    cursor.execute('SELECT pin FROM users WHERE account_number = ?', (account_number,))
    return cursor.fetchone()

def get_account_info(acc_no):
    cursor.execute('SELECT account_number, name, dob, email, phone, address, account_type, balance, branch FROM users WHERE account_number = ?', (acc_no,))
    row = cursor.fetchone()
    if row:
        return {
            'account_number': row[0],
            'name': row[1],
            'dob': row[2],
            'email': row[3],
            'phone': row[4],
            'address': row[5],
            'account_type': row[6],
            'balance': row[7],
            'branch': row[8]
        }
    else:
        return {}


def update_balance(acc_no, amount, is_deposit=True):
    if is_deposit:
        cursor.execute('UPDATE users SET balance = balance + ? WHERE account_number = ?', (amount, acc_no))
    else:
        cursor.execute('UPDATE users SET balance = balance - ? WHERE account_number = ?', (amount, acc_no))
    conn.commit()

def update_pin(acc_no, new_pin):
    cursor.execute('UPDATE users SET pin = ? WHERE account_number = ?', (new_pin, acc_no))
    conn.commit()

def generate_account_number():
    return str(random.randint(10000000, 99999999))
