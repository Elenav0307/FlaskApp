from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def products():

    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()

    conn.close()

    return render_template('products.html', products=rows)


if __name__ == '__main__':
    app.run(debug=True)