#!/bin/env python3

from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)


def get_all():
    conn = mysql.connector.connect(
        host='localhost',
        user='kennyaga',
        password='admin',
        database='compoint_db')

    cursor = conn.cursor()#dictionary=True)
    cursor.execute("SELECT * FROM inventory")  # Replace with your table
    data = cursor.fetchall()
    conn.close()
    return data


@app.route("/")
def landing():
    data = get_all()
    return render_template("index.html", data=data)

@app.route("/add", methods=['POST'])
def add():
    pass
    

if __name__ == "__main__":
    app.run(debug=True)