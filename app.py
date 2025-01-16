from flask import Flask,render_template
import sqlite3
app=Flask(__name__)

@app.route('/')
def index():
    Database='C:/Users/abine/OneDrive/Desktop/flask/flask-projects/data.db'
    con = sqlite3.connect(Database)
    cursor= con.cursor()
    cursor.execute(""" 
                   CREATE TABLE IF NOT EXISTS user (
                       id INTEGER PRIMARY KEY AUTOINCREMENT, 
                       name TEXT NOT NULL 
                   )
                   """)
    try:
        cursor.execute('create table stud_details(stud_id int,stud_name text,stud_email text,stud_phno int)')
    except:
        pass
    try:
        cursor.execute('insert into stud_details values(1,"abi","abi@gmail.com",6576576576)')
    except:
        pass
    cursor.execute('select * from stud_details')
    users=cursor.fetchall()
    con.commit()
    con.close()
    return render_template('index.html',users=users)
app.run(debug=True)