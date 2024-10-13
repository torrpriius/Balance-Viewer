from flask import Flask, request, jsonify
from web3 import Web3
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(app.config['RPC_URL']))

# Check connection
if not web3.isConnected():
    raise ConnectionError("Failed to connect to the Base network. Check RPC_URL.")

@app.route('/balance', methods=['GET'])
def get_balance():
    address = request.args.get('address')
    
    if not address:
        return jsonify({"error": "Address not provided"}), 400
    
    if not web3.isAddress(address):
        return jsonify({"error": "Invalid address format"}), 400
    
    try:
        balance_wei = web3.eth.get_balance(address)
        balance_eth = web3.fromWei(balance_wei, 'ether')
        return jsonify({
            "address": address,
            "balance_wei": str(balance_wei),
            "balance_eth": str(balance_eth)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def index():
    return jsonify({"message": "Base Wallet Balance Viewer API"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=app.config['PORT'], debug=app.config['DEBUG'])
