from flask import Flask, jsonify, request
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "db"),
        user="root",
        password="rootpassword",
        database="ecommerce_db"
    )

@app.route("/api/products/<int:id>")
def get_product(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products WHERE id = %s", (id,))
    product = cursor.fetchone()
    conn.close()
    
    if product:
        # Variasi Logika 2: Diskon 10% jika stok > 10 
        if product['stock'] > 10:
            product['price'] = int(product['price'] * 0.9)
            product['discount_applied'] = True
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

# Variasi Logika 1: Filter berdasarkan kategori 
@app.route("/api/products/category/<string:category>")
def get_products_by_category(category):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products WHERE category = %s", (category,))
    products = cursor.fetchall()
    conn.close()
    return jsonify(products)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80) # [cite: 61]