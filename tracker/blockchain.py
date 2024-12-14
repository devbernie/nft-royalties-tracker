# tracker/blockchain.py

import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Use BASE_URL from .env file
BASE_URL = os.getenv("BASE_URL", "").strip()
if not BASE_URL:
    raise ValueError("BASE_URL environment variable is not set or empty.")

def get_headers():
    """
    Generate headers for API requests.
    """
    return {
        "Content-Type": "application/json"
    }


def get_transactions(address):
    """
    Retrieve transactions (UTxOs) related to a Cardano address using Koios API.
    Args:
        address (str): Cardano wallet address.
    Returns:
        list: List of transactions (UTxOs).
    """
    url = f"{BASE_URL}/address_info"
    payload = {"_addresses": [address]}

    try:
        response = requests.post(url, json=payload, headers=get_headers())
        response.raise_for_status()
        address_info = response.json()
        return address_info[0]["utxo_set"] if address_info else []
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Failed to fetch transactions: {e}")


def get_metadata(transaction_id):
    """
    Retrieve metadata of a transaction using Koios API.
    Args:
        transaction_id (str): Transaction ID on the blockchain.
    Returns:
        dict: Metadata of the transaction.
    """
    url = f"{BASE_URL}/tx_metadata"
    payload = {"_tx_hashes": [transaction_id]}

    try:
        response = requests.post(url, json=payload, headers=get_headers())
        response.raise_for_status()
        tx_metadata = response.json()
        return tx_metadata[0]["metadata"] if tx_metadata else {}
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Failed to fetch metadata for transaction {transaction_id}: {e}")


def get_policy_assets(policy_id):
    """
    Retrieve all assets under a specific policy ID using Koios API.
    Args:
        policy_id (str): Policy ID.
    Returns:
        list: List of assets.
    """
    url = f"{BASE_URL}/asset_list"

    try:
        response = requests.get(url, headers=get_headers())
        response.raise_for_status()
        assets = response.json()
        return [asset for asset in assets if asset["policy_id"]["value"] == policy_id]
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Failed to fetch assets for policy {policy_id}: {e}")


def is_nft_transaction(transaction):
    """
    Check if a transaction involves NFTs.
    Args:
        transaction (dict): Transaction data.
    Returns:
        bool: True if the transaction involves NFTs, False otherwise.
    """
    return "policy_id" in transaction or "asset" in transaction