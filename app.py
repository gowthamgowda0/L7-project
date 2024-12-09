
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)
DB_NAME = "ice_cream_parlor.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS flavors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        is_seasonal BOOLEAN NOT NULL
    )""")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS allergens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE
    )""")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cart (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        flavor_id INTEGER NOT NULL,
        FOREIGN KEY (flavor_id) REFERENCES flavors (id)
    )""")
    conn.commit()
    conn.close()

@app.route('/flavors', methods=['GET', 'POST'])
def manage_flavors():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    if request.method == 'POST':
        data = request.json
        cursor.execute("INSERT INTO flavors (name, is_seasonal) VALUES (?, ?)",
                       (data['name'], data['is_seasonal']))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Flavor added successfully!'}), 201
    else:
        cursor.execute("SELECT * FROM flavors")
        flavors = cursor.fetchall()
        conn.close()
        return jsonify(flavors)

@app.route('/allergens', methods=['GET', 'POST'])
def manage_allergens():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    if request.method == 'POST':
        data = request.json
        try:
            cursor.execute("INSERT INTO allergens (name) VALUES (?)", (data['name'],))
            conn.commit()
        except sqlite3.IntegrityError:
            return jsonify({'message': 'Allergen already exists!'}), 400
        finally:
            conn.close()
        return jsonify({'message': 'Allergen added successfully!'}), 201
    else:
        cursor.execute("SELECT * FROM allergens")
        allergens = cursor.fetchall()
        conn.close()
        return jsonify(allergens)

@app.route('/cart', methods=['GET', 'POST'])
def manage_cart():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    if request.method == 'POST':
        data = request.json
        cursor.execute("INSERT INTO cart (flavor_id) VALUES (?)", (data['flavor_id'],))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Added to cart successfully!'}), 201
    else:
        cursor.execute("""
        SELECT cart.id, flavors.name FROM cart 
        JOIN flavors ON cart.flavor_id = flavors.id
        """)
        cart_items = cursor.fetchall()
        conn.close()
        return jsonify(cart_items)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
