import uuid
from flask import Flask, jsonify, request
import random
from datetime import datetime

app = Flask(__name__)

# Generate random transaction data
def generate_transaction():
    return {
        "Transaction_ID": str(uuid.uuid4()),  # Add a unique Transaction_ID
        "Customer_ID": str(uuid.uuid4()),  # Assuming random UUIDs for customer
        "Timestamp": datetime.utcnow().isoformat(),
        "Transaction_Type": random.choice(["P2P", "FPS", "ATM", "Card Payment"]),
        "Amount": round(random.uniform(10, 5000), 2),
        "Merchant_ID": str(uuid.uuid4()),  # Assuming random UUIDs for merchant
        "Narration": random.choice(["Purchase", "Refund", "Transfer"]),
        "Fraudulent": random.choice([True, False]),
        "Fraud_Pattern_ID": random.randint(1, 100) if random.choice([True, False]) else None,
        "Failed_Pin_Attempts": random.randint(0, 3),
        "Transaction_Status": random.choice(["Success", "Failed"]),
    }

@app.route('/stream_data', methods=['POST'])
def stream_data():
    table = request.json.get("table")
    if table == "transactions":
        data = [generate_transaction() for _ in range(10)]  # Generate 10 rows
        return jsonify(data)
    return jsonify({"error": "Invalid table name"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
