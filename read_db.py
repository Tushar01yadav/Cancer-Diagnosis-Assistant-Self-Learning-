import streamlit as st
import sqlite3

# Function to connect and read data
# def read_user_data():
#     conn = sqlite3.connect('users.db')
#     cursor = conn.cursor()
#
#     # Read all users
#     cursor.execute("SELECT * FROM users")  # Do NOT fetch passwords
#     data = cursor.fetchall()
#
#     conn.close()
#     return data
# users = read_user_data()
# print(users)
#
# user_id =1
# password ='Tushar619'
# conn = sqlite3.connect("users.db")
# c = conn.cursor()
# c.execute("SELECT password FROM users WHERE id=? AND password=?", (user_id, password))
# result = c.fetchone()
# conn.close()
# print(result)


def read_cancer_data():
    conn = sqlite3.connect('Cancer_data.db')
    z = conn.cursor()

    # Read all users
    z.execute("SELECT * FROM cancer ")  # Do NOT fetch passwords
    data = z.fetchall()

    conn.close()
    return data
Cancer = read_cancer_data()
print(len(Cancer))



