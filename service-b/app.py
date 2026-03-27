from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/shipping")
def calculate_shipping():
    weight = float(request.args.get("weight", 0)) # [cite: 75]
    method = request.args.get("method", "reguler").lower()
    zone = int(request.args.get("zone", 1))

    # Variasi Logika 1: Metode Pengiriman 
    base_rate = 10 if method == "express" else 5
    cost = weight * base_rate
    
    # Variasi Logika 2: Multiplier Zona Wilayah 
    zone_multiplier = 1.0
    if zone == 2:
        zone_multiplier = 1.2
    elif zone == 3:
        zone_multiplier = 1.5
        
    final_cost = cost * zone_multiplier
    return jsonify({"cost": final_cost, "method": method, "zone": zone}) # [cite: 77]

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80) # [cite: 78]