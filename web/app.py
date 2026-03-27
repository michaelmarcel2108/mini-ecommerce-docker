from flask import Flask, jsonify, request
import requests
import os

app = Flask(__name__)

SERVICE_A_URL = os.getenv("SERVICE_A_URL", "http://localhost:8081/api/products") # [cite: 272]
SERVICE_B_URL = os.getenv("SERVICE_B_URL", "http://localhost:8082/api/shipping") # [cite: 273]
SERVICE_C_URL = os.getenv("SERVICE_C_URL", "http://localhost:8083/api/promo")

@app.route("/checkout/<int:product_id>")
def checkout(product_id):
    promo_code = request.args.get("promo", "")
    shipping_method = request.args.get("method", "reguler")
    
    # 1. Panggil Service A (Katalog dari DB) [cite: 277]
    product_resp = requests.get(f"{SERVICE_A_URL}/{product_id}")
    if product_resp.status_code != 200:
        return jsonify({"error": "Product not found"}), 404
    product = product_resp.json()

    # 2. Panggil Service B (Ongkos Kirim Dinamis) [cite: 278, 279, 280, 281]
    shipping = requests.get(
        SERVICE_B_URL,
        params={"weight": product["weight"], "method": shipping_method, "zone": 2}
    ).json()

    # 3. Panggil Service C (Promo - Bonus)
    promo_discount = 0
    if promo_code:
        promo_resp = requests.get(f"{SERVICE_C_URL}/{promo_code}").json()
        promo_discount = promo_resp.get("discount", 0)

    # Kalkulasi Total [cite: 282]
    total = product["price"] + shipping["cost"] - promo_discount

    return jsonify({
        "product": product["name"], # [cite: 284]
        "base_price": product["price"], # [cite: 285]
        "shipping": shipping["cost"], # [cite: 286]
        "promo_discount": promo_discount,
        "total_to_pay": max(0, total) # [cite: 287]
    }) # [cite: 288]

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80) # [cite: 289]