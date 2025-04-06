

#!/usr/bin/env python3
import json
import requests

# Set your RPC endpoint (e.g., Infura, Alchemy, or your own node)
RPC_ENDPOINT = "https://carrot.megaeth.com/rpc"  # <-- Replace with your RPC endpoint

def get_balance(address):
    """
    Fetch the native balance for the given address via JSON-RPC.
    Returns the balance in Ether as a float.
    """
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_getBalance",
        "params": [address, "latest"],
        "id": 1
    }
    try:
        response = requests.post(RPC_ENDPOINT, json=payload)
        response.raise_for_status()
        result = response.json().get("result")
        if result:
            # Convert balance from hex (Wei) to Ether
            balance_wei = int(result, 16)
            balance_eth = balance_wei / (10 ** 18)
            return balance_eth
    except Exception as e:
        print(f"Error fetching balance for {address}: {e}")
    return None

def main():
    try:
        with open("wallets.json", "r") as f:
            wallets = json.load(f)
    except Exception as e:
        print(f"Error loading wallets.json: {e}")
        return

    for wallet in wallets[::-1]:
        address = wallet.get("address")
        private_key = wallet.get("privateKey")
        balance = get_balance(address)
        print(f"\n\n\nAddress: {address}")
        print(f"Balance: {balance} ETH")
        print(f"PrivateKey: {private_key}")
        print("-" * 40)

if __name__ == "__main__":
    main()
