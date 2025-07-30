import os
import sqlite3
from time import time
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import base64

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

import cancer_model


if "page" not in st.session_state:
    st.session_state.page = "home"
def go_home():
    st.session_state.page = "home"
def go_Check():
    st.session_state.page = "Check"
def go_login()  :
    st.session_state.page = "login"


if st.session_state.page == "home":
    def get_base64_of_bin_file(bin_file):
     with open(bin_file, 'rb') as f:
        data = f.read()
     return base64.b64encode(data).decode()

    image_file = "background.jpg"  # your local image file path
    img_base64 = get_base64_of_bin_file(image_file)

    page_bg_img = f"""
     <style>
     [data-testid="stAppViewContainer"] {{
     background-image: url("data:image/jpg;base64,{img_base64}");
     background-size: cover;
     background-position: center;
     background-repeat: no-repeat;
     background-attachment: fixed;
     }}
     </style>
     """

    st.markdown(page_bg_img, unsafe_allow_html=True)



    st.markdown(
    "<h1 style='text-align: center; '> 🧬 Cancer Diagnosis Assistant ✙ </h1>",
    unsafe_allow_html=True)

    st.write("")
    st.markdown(
    "<h1 style='text-align: center; '> 👨🏻‍ Your Personalized Doctor  </h1>",
    unsafe_allow_html=True)
    # st.markdown(
    # """
    # <div style='text-align: center;'>
    #     <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQyWcQlyp15pMY57rLt64_AdFAG54G-WNOMqw&s" width="70"/>
    # </div>
    # """,
    # unsafe_allow_html=True)
    st.write("")
    st.write("Register Account")
    # st.markdown(
    #     "<h3 style='text-align: center;'>"
    #     "<span style='color: yellow;'>Hello!</span>"
    #     "</h3>",
    #     unsafe_allow_html=True)
    col1, col2 = st.columns([2, 2])
    with col1:

        name = st.text_input("Enter your name")
        st.write("")
    with col2:
        age = st.number_input("Enter your age", min_value=0, max_value=100)
        st.write("")
    with col1:
        City = st.text_input("Enter your City")
        st.write("")
    with col2:
        Another = st.number_input("Weight ", min_value=0, max_value=100)
        st.write("")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        Password: str | None = st.text_input("Create Your Password  ", type="password")
        Checked_Password = st.text_input("Renter Your Password  ", type="password")

        st.write("")


    # Create three columns (left, center, right)
    col1, col2, col3 = st.columns([2.3, 2, 1])
    with col2:
        submit = st.button("Sign Up",key='1')
    # Place the button in the center column



    conn = sqlite3.connect("users.db")
    c = conn.cursor()

        # Create table if not exists
    c.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                city TEXT,
                password TEXT
            )
            ''')

    if submit:
     if not (name.strip() and City.strip() and Password.strip() and Checked_Password.strip()) or age == 0 or Another == 0:  # check if empty or just spaces
         st.warning(" Fields cannot be empty! Please enter a value.")

     else :
         if Password == Checked_Password :

        # Insert data
           c.execute('INSERT INTO users (name, age, city, password) VALUES (?, ?, ?, ?)',
                  (name, age, City, Checked_Password))

           conn.commit()
           user_id = c.lastrowid
           conn.close()
           st.success(f"Hello {name}, You are now Registered, Your Registration id is : {user_id}")
           
           st.session_state.page = "Check"
           st.rerun()
         elif Password != Checked_Password :
              st.warning("Password Incorrect")
    login = st.button("Already have a Registered ID?",on_click=go_login)
elif st.session_state.page == "login":
    def get_base64_of_bin_file(bin_file):
     with open(bin_file, 'rb') as f:
        data = f.read()
     return base64.b64encode(data).decode()

    image_file = "background.jpg"  # your local image file path
    img_base64 = get_base64_of_bin_file(image_file)

    page_bg_img = f"""
     <style>
     [data-testid="stAppViewContainer"] {{
     background-image: url("data:image/jpg;base64,{img_base64}");
     background-size: cover;
     background-position: center;
     background-repeat: no-repeat;
     background-attachment: fixed;
     }}
     </style>
     """

    st.markdown(page_bg_img, unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'> Login page </h1>", unsafe_allow_html=True)
    st.write("")
    user_id :str | None = st.text_input("Enter Your Registration ID  ")
    password: str | None =st.text_input("Enter Your Password ", type="password")
    result = ''



    st.write("")
    col1, col2, col3 = st.columns([1.8, 2, 1])
    with col2 :
        Sign_in = st.button("Sign in",key='2')
        st.button(" Home ", on_click=go_home)

    if Sign_in :
        if not (user_id.strip() and password.strip()):
            st.warning("Please register or login first to access symptom checking.")
        else :
         conn = sqlite3.connect("users.db")
         c = conn.cursor()
         c.execute("SELECT password FROM users WHERE id=? AND password=?", (user_id, password))
         result = c.fetchone()
         conn.close()
        if result == None :
         st.warning("user not found")

        elif result == (password,):
        
            st.success(f"welcome Back ")
            st.session_state.page = "Check"
            st.rerun()





elif st.session_state.page == "Check":
    def get_base64_of_bin_file(bin_file):
     with open(bin_file, 'rb') as f:
        data = f.read()
     return base64.b64encode(data).decode()
     conn = sqlite3.connect("Cancer_data.db")
     z = conn.cursor()
     z.execute(''' CREATE TABLE IF NOT EXISTS cancer
                   (
                       Worst_Area
                       FLOAT,
                       Worst_Concave_Points
                       FLOAT,
                       Mean_Concave_Points
                       FLOAT,
                       Worst_Radius
                       FLOAT,
                       Worst_Perimeter
                       FLOAT,
                       Mean_Perimeter
                       FLOAT,
                       Label
                       float
                   )''')

    image_file = "background.jpg"  # your local image file path
    img_base64 = get_base64_of_bin_file(image_file)

    page_bg_img = f"""
     <style>
     [data-testid="stAppViewContainer"] {{
     background-image: url("data:image/jpg;base64,{img_base64}");
     background-size: cover;
     background-position: center;
     background-repeat: no-repeat;
     background-attachment: fixed;
     }}
     </style>
     """

    st.markdown(page_bg_img, unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center;'> 🧬 Cancer Diagnosis Assistant </h1>", unsafe_allow_html=True)

    st.markdown(
        "<h2 style='text-align: center;'>"
        "<span style='color: white;'>  👨🏻  Enter All The Fields Carefully</span>"
        "</h2>",
        unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.write("")
    col1, col2 = st.columns([2, 2])
    with col1:
        a = st.number_input("Enter Worst Area  ", min_value=0.0, key="1")
    with col2:
        b = st.number_input("Enter Worst Concave Points ", min_value=0.0, key="2")
    with col1:
        c = st.number_input("Enter Mean Concave Points", min_value=0.0, key="3")
    with col2:
        d = st.number_input("Enter Worst Radius :", min_value=0.0, key="4")
    with col1:
        e = st.number_input("Enter Worst Perimeter :", min_value=0.0, key="5")
    with col2:
        fo = st.number_input("Enter Mean Perimeter", min_value=0.0, key="6")

    st.write("")

    data = [a, b, c, d, e, fo]
    input_data = np.array([data])


    col1, col2, col3 = st.columns([4, 4, 1])
    with col2:
        predict = st.button("Predict")
    try:
     with open("rfe_model.pkl", "rb") as f:
        model = pickle.load(f)
    except FileNotFoundError:
     st.error("Model file not found.")
     st.stop()



    if predict :
        if not all([a, b, d, e, fo]):
            st.warning(" Fields cannot be empty! Please enter a value.")
        else:
          input_data = np.array([[a, b, c, d, e, fo]])
          output = model.predict(input_data)
          probability = model.predict_proba(input_data)
          st.write(f"Prediction: **{output[0]}**")

          if output[0] == 1:
            st.error(f"🧬 Result: Malignant (Cancerous) with {round(probability[0][1]*100, 2)}% confidence.")
          else:
           st.write(f"🧬 Result: Benign (Non-cancerous) with {round(probability[0][0]*100, 2)}% confidence.")
           conn = sqlite3.connect("Cancer_data.db")
           z = conn.cursor()
           z.execute("INSERT INTO cancer(Worst_Area, Worst_Concave_Points, Mean_Concave_Points, Worst_Radius, Worst_Perimeter, Mean_Perimeter, Label) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (a, b, c, d, e, fo, float(output[0])))

           conn.commit()
           conn.close()


    st.markdown("---")
    col1, col2, col3 = st.columns([4, 4, 1])
    with col2:
        st.button("Go Home", on_click=go_home)

    conn = sqlite3.connect("Cancer_data.db")
    z = conn.cursor()
    z.execute("SELECT Worst_Area, Worst_Concave_Points, Mean_Concave_Points, Worst_Radius, Worst_Perimeter, Mean_Perimeter FROM cancer")
    rows = z.fetchall()
    z.execute("SELECT label FROM cancer")
    y_rows = z.fetchall()






    if len(rows) >= 5:
        st.info("📊 5 new inputs collected. Appending to training dataset...")
        ##add from here
        new_columns = ['Worst_Area', 'Worst_Concave_Points', 'Mean_Concave_Points',
                       'Worst_Radius', 'Worst_Perimeter', 'Mean_Perimeter']
        cancer_model.X_selected.columns = new_columns

        columns = ['Worst_Area', 'Worst_Concave_Points', 'Mean_Concave_Points',
                   'Worst_Radius', 'Worst_Perimeter', 'Mean_Perimeter']

        df_new = pd.DataFrame(rows, columns=columns)

        df_new_y = pd.DataFrame(y_rows, columns=['target'])

        combined_df_y = pd.concat([cancer_model.y, df_new_y], ignore_index=True)
        combined_df_y = combined_df_y.drop(columns='target')
        combined_df_y = combined_df_y.rename(columns={0: 'target'})
        combined_df = pd.concat([cancer_model.X_selected, df_new], ignore_index=True)
        combined_df_y = combined_df_y.fillna(0)
        st.write("New Data points appended to dataset✅")
        st.write("Retraining Training the  Model.....")
        X_train, X_test, y_train, y_test = train_test_split(combined_df, combined_df_y, test_size=0.2, random_state=42)

        # Train RandomForestClassifier on selected features
        clf = RandomForestClassifier(random_state=42)
        clf.fit(X_train, y_train)
        # Evaluate
        y_pred = clf.predict(X_test)
        st.write("Model has retrained✅ ")
        st.write("Accuracy of model after retraining :")
        st.write(accuracy_score(y_test, y_pred))
        with open('rfe_model.pkl', 'wb') as f:
            pickle.dump(clf, f)
        # Delete DB data to avoid duplication on next run
        z.execute("DELETE FROM cancer")
        conn.commit()



        # Create DataFrame from DB rows
        # df_new = pd.DataFrame(rows, columns=[
        #     'Radius_Mean', 'Concavity_Mean', 'Concavity_Worst', 'Radius_se',
        #     'Compactness_Worst', 'Compactness_Mean'
        # ])
        #
        # y_df = pd.DataFrame(y, columns=['label'])
        #
        #
        # # Add predicted labels to DataFrame
        # df_new['label'] = output[0]
        #
        # # Append to dataset.csv (create if it doesn't exist)
        # X_combined = pd.concat([cancer_model.X_selected , df_new], ignore_index=True)
        # Y_combined = pd.concat([cancer_model.y, y_df], ignore_index=True)
        # # Combine features and labels into one DataFrame
        # df_combined = pd.concat([X_combined, Y_combined], axis=1)
        #
        # # Drop rows where either X or Y has NaN
        # df_combined = df_combined.dropna()
        #
        # # Separate back into X and Y
        # X_clean = df_combined.iloc[:, :-1]  # all columns except last one
        # y_clean = df_combined.iloc[:, -1]  # last column (label)
        # st.write(X_clean)
        # st.write(y_clean)
        # Clean DB after appending (optional but avoids duplication)
        z.execute("DELETE FROM cancer")
        conn.commit()
