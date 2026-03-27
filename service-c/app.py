from flask import Flask, request, jsonify

app = Flask(__name__)

promos = {
    "KAMPUS2026": {"discount_value": 50},
    "GRATISONGKIR": {"discount_value": 15}
}

@app.route("/api/promo/<code>")
def check_promo(code):
    promo = promos.get(code.upper())
    if promo:
        return jsonify({"valid": True, "discount": promo["discount_value"]})
    return jsonify({"valid": False, "discount": 0})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)