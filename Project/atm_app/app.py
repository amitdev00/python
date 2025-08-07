import streamlit as st
from utils import (create_table, insert_user, get_pin, get_account_info,
                    update_balance, update_pin, generate_account_number)

create_table()

def signup():
    st.header("Create New Account")
    name = st.text_input("Full Name")
    dob = st.text_input("Date of Birth (YYYY-MM-DD)")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    address = st.text_area("Address")
    account_type = st.selectbox("Account Type", ["Savings", "Current"])
    branch = st.text_input("Branch")
    initial_deposit = st.number_input("Initial Deposit", min_value=0.0)
    pin = st.text_input("Set PIN (4 digits)", type="password")
    confirm_pin = st.text_input("Confirm PIN", type="password")

    if st.button("Create Account"):
        if len(pin) != 4 or not pin.isdigit():
            st.error("PIN must be exactly 4 digits.")
            return
        if pin != confirm_pin:
            st.error("PINs do not match.")
            return
        acc_no = generate_account_number()
        user_data = (acc_no, name, dob, email, phone, address,
                         account_type, initial_deposit, branch, pin)
        if insert_user(user_data):
            st.success(
                f"Account created successfully! Your Account Number is {acc_no}")
        else:
            st.error("Account number already exists. Try again.")


def login():
    st.header("Login to Your Account")
    acc_no = st.text_input("Account Number", key="login_acc_no")
    pin = st.text_input("PIN", type="password", key="login_pin")

    if st.button("Login"):
        acc_no_clean = acc_no.strip()
        pin_clean = pin.strip()
        result = get_pin(acc_no_clean)

        if result:
            actual_pin = str(result[0]).strip()
            if pin_clean == actual_pin:
                st.session_state['logged_in'] = True
                st.session_state['acc_no'] = acc_no_clean
            else:
                st.error("Invalid PIN.")
        else:
            st.error("Invalid account number.")


def show_accountInfo(acc_no):
    info = get_account_info(acc_no)
    if not info:
        st.error("Account not found.")
        return

    st.header("Your Account Dashboard")

    tab1, tab2 = st.tabs(
        ["Profile Details", "Change PIN"])

    with tab1:
        st.subheader("Personal Information")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"Account Number: {info['account_number']}")
            st.markdown(f"Name: {info['name']}")
            st.markdown(f"Date of Birth: {info['dob']}")
        with col2:
            st.markdown(f"Email: {info['email']}")
            st.markdown(f"Phone: {info['phone']}")
            st.markdown(f"Address: {info['address']}")
        with col3:
            st.markdown(f"Account Type: {info['account_type']}")
            st.markdown(f"Balance: ₹{info['balance']:.2f}")
            st.markdown(f"Branch: {info['branch']}")

        st.subheader("Deposit Money")
        deposit = st.number_input(
            "Deposit Amount", min_value=0.0, key="deposit_amt")
        if st.button("Deposit"):
            if deposit > 0:
                update_balance(acc_no, deposit, is_deposit=True)
                st.success(f"Deposited ₹{deposit:.2f} successfully.")
                st.rerun()

        st.subheader("Withdraw Money")
        withdraw = st.number_input(
            "Withdraw Amount", min_value=0.0, key="withdraw_amt")
        if st.button("Withdraw"):
            if withdraw > info['balance']:
                st.error("Insufficient balance.")
            elif withdraw > 0:
                update_balance(acc_no, withdraw, is_deposit=False)
                st.success(f"Withdrew ₹{withdraw:.2f} successfully.")
                st.rerun()

    with tab2:
        st.subheader("Change PIN")
        old_pin = st.text_input("Old PIN", type="password")
        new_pin = st.text_input("New PIN (4 digits)", type="password")
        confirm_pin = st.text_input("Confirm New PIN", type="password")

        if st.button("Change PIN"):
            actual_pin = get_pin(acc_no)[0]
            if old_pin != actual_pin:
                st.error("Old PIN incorrect.")
            elif new_pin != confirm_pin:
                st.error("New PINs do not match.")
            elif len(new_pin) != 4 or not new_pin.isdigit():
                st.error("New PIN must be exactly 4 digits.")
            else:
                update_pin(acc_no, new_pin)
                st.success("PIN changed successfully.")
                st.rerun()


def logout():
    if st.button("Logout"):
        st.session_state['logged_in'] = False
        st.session_state['acc_no'] = None
        st.rerun()


def main():
    st.set_page_config(layout="wide")
    st.title("State Bank of India ATM")
    st.subheader("Welcomes You!")

    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
        st.session_state['acc_no'] = None

    if not st.session_state['logged_in']:
        col4, col5 = st.columns(2)
        with col4:
            with st.expander("Create New Account"):
                signup()
        with col5:
            with st.expander("Login to Your Account"):
                login()
    else:
        st.success(f"Logged in as Account No: {st.session_state['acc_no']}")
        logout()
        st.markdown("---")
        show_accountInfo(st.session_state['acc_no'])


if __name__ == "__main__":
    main()
