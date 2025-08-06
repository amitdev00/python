import sqlite3
import streamlit as st

conn = sqlite3.connect("bank.db", check_same_thread=False)
cursor = conn.cursor()

def create_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        account_number TEXT PRIMARY KEY,
                        name TEXT,
                        dob TEXT,
                        email TEXT,
                        phone TEXT,
                        address TEXT,
                        account_type TEXT,
                        balance REAL,
                        branch TEXT,
                        pin TEXT
                      )''')
    conn.commit()

def validate_signup():
    st.write("Signup form here (implement as needed)")

def validate_login():
    acc_no = st.text_input("Account Number", key="login_acc_no")
    pin = st.text_input("PIN", type="password", key="login_pin")
    if st.button("Login"):
        cursor.execute('SELECT pin FROM users WHERE account_number = ?', (acc_no,))
        result = cursor.fetchone()
        if result and result[0] == pin:
            return acc_no
        else:
            st.error("Invalid account number or PIN.")
    return None

def get_account_info(acc_no):
    cursor.execute('SELECT account_number, name, dob, email, phone, address, account_type, balance, branch FROM users WHERE account_number = ?', (acc_no,))
    row = cursor.fetchone()
    if row:
        keys = ['account_number', 'name', 'dob', 'email', 'phone', 'address', 'account_type', 'balance', 'branch']
        return dict(zip(keys, row))
    else:
        return {}

def show_transactions(acc_no):
    st.write("Transaction history here (implement as needed)")

def change_pin_ui(acc_no):
    st.write("Separate PIN change UI here (optional if inside show_account_info)")

def show_account_info(acc_no):
    cursor.execute('SELECT name, account_type, balance FROM users WHERE account_number = ?', (acc_no,))
    user = cursor.fetchone()
    if user:
        name, acc_type, balance = user
        st.write(f"**Name:** {name}")
        st.write(f"**Account Number:** {acc_no}")
        st.write(f"**Account Type:** {acc_type}")
        st.write(f"**Balance:** ₹{balance:.2f}")

        st.subheader("Deposit Money")
        deposit = st.number_input("Deposit Amount", min_value=0.0, key="deposit_amt")
        if st.button("Deposit", key="btn_deposit"):
            if deposit > 0:
                cursor.execute('UPDATE users SET balance = balance + ? WHERE account_number = ?', (deposit, acc_no))
                conn.commit()
                st.success(f"Deposited ₹{deposit:.2f} successfully.")
                st.experimental_rerun()

        st.subheader("Withdraw Money")
        withdraw = st.number_input("Withdraw Amount", min_value=0.0, key="withdraw_amt")
        if st.button("Withdraw", key="btn_withdraw"):
            if withdraw > balance:
                st.error("Insufficient balance.")
            elif withdraw > 0:
                cursor.execute('UPDATE users SET balance = balance - ? WHERE account_number = ?', (withdraw, acc_no))
                conn.commit()
                st.success(f"Withdrew ₹{withdraw:.2f} successfully.")
                st.experimental_rerun()

        st.subheader("Change PIN")
        old = st.text_input("Old PIN", type="password", key="old_pin")
        new = st.text_input("New PIN", type="password", key="new_pin")
        confirm_new = st.text_input("Confirm New PIN", type="password", key="confirm_new")
        if st.button("Change PIN", key="btn_change_pin"):
            cursor.execute('SELECT pin FROM users WHERE account_number = ?', (acc_no,))
            actual_pin = cursor.fetchone()[0]
            if old != actual_pin:
                st.error("Old PIN incorrect.")
            elif new != confirm_new:
                st.error("New PINs do not match.")
            elif len(new) < 4 or not new.isdigit():
                st.error("New PIN must be at least 4 digits.")
            else:
                cursor.execute('UPDATE users SET pin = ? WHERE account_number = ?', (new, acc_no))
                conn.commit()
                st.success("PIN changed successfully.")
                st.experimental_rerun()
    else:
        st.error("Account not found.")
