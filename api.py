#!/bin/env python3

from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


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


@app.route("/add_product", methods=['GET'])
def add_product():
    return render_template("add.html")

@app.route("/add", methods=['POST'])
def add_to_db():
    if request.method == 'POST':
        product = request.form['product']
        category = request.form['category']
        specifications = request.form['specifications']
        buying_price = request.form['buying_price']
        selling_price = request.form['selling_price']

        conn = mysql.connector.connect(
            host='localhost',
            user='kennyaga',
            password='admin',
            database='compoint_db'
        )
        cursor = conn.cursor()
        cursor.execute("INSERT INTO inventory (Product, Category, Specifications, Selling_price, Buying_price) VALUES (%s, %s, %s, %s, %s)", (product, category, specifications, selling_price, buying_price))
        conn.commit()
        conn.close()
    # Quantity is not being added, will be handled later, as well as mechanism for comparing similar products during addition

    return redirect(url_for('landing'))

@app.route("/delete/<int:id>")
def delete_product(id):
    conn = mysql.connector.connect(
        host='localhost',
        user='kennyaga',
        password='admin',
        database='compoint_db'
    )
    cursor = conn.cursor()
    cursor.execute("DELETE FROM inventory WHERE id = %s", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('landing'))


@app.route("/update/<int:id>", methods=['GET', 'POST'])
def update_product(id):
    conn = mysql.connector.connect(
        host='localhost',
        user='kennyaga',
        password='admin',
        database='compoint_db'
    )
    cursor = conn.cursor()
    if request.method == 'POST':
        product = request.form['product']
        category = request.form['category']
        specifications = request.form['specifications']
        buying_price = request.form['buying_price']
        selling_price = request.form['selling_price']
        cursor.execute("UPDATE inventory SET Product = %s, Category = %s, Specifications = %s, Buying_price = %s, Selling_price = %s WHERE id = %s",
                       (product, category, specifications, buying_price, selling_price, id))
        conn.commit()
        return redirect(url_for('landing'))
    cursor.execute("SELECT * FROM inventory WHERE id = %s", (id,))
    product = cursor.fetchone()
    conn.close()
    return render_template("update.html", product=product)

if __name__ == "__main__":
    app.run(debug=True)