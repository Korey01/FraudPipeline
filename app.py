
from flask import Flask, jsonify
import random
import uuid
from datetime import datetime

# Create the Flask application
app = Flask(__name__)

# Function to generate a random transaction
def generate_random_transaction():
    return {
        "Customer_ID": str(uuid.uuid4()),
        "Timestamp": datetime.utcnow().isoformat() + 'Z',
        "Transaction_Type": random.choice(["P2P", "FPS", "ATM", "Card Payment"]),
        "Amount": round(random.uniform(1.0, 5000.0), 2),
        "Merchant_ID": str(uuid.uuid4()),
        "Narration": random.choice(["Gift for mom", "Online purchase", "Bill payment"]),
        "Fraudulent": random.choice([True, False]),
        "Fraud_Pattern_ID": random.choice([None, str(uuid.uuid4())]),
        "Failed_Pin_Attempts": random.randint(0, 3),
        "Transaction_Status": random.choice(["Success", "Failed"])
    }

# Define the API endpoint
@app.route('/api/transaction', methods=['GET'])
def get_transaction():
    transaction = generate_random_transaction()
    return jsonify(transaction)

# Run the application (used for local testing)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
