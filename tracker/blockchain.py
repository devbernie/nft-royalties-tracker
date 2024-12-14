import requests
import os
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

API_KEY = os.getenv("MAESTRO_API_KEY")
API_ENV = os.getenv("API_ENV", "preprod")  # Default to 'preprod' if not specified
BASE_URL = f"https://{API_ENV}.gomaestro-api.org/v1"  # Dynamic API endpoint based on environment


def get_transactions(address):
    """
    Retrieve transactions related to a Cardano address using Maestro API.
    Args:
        address (str): Cardano wallet address.
    Returns:
        list: List of transactions.
    """
    headers = {"Authorization": f"Bearer {API_KEY}"}
    url = f"{BASE_URL}/addresses/{address}/utxos"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Failed to fetch transactions: {e}")


def get_metadata(transaction_id):
    """
    Retrieve metadata of a transaction using Maestro API.
    Args:
        transaction_id (str): Transaction ID on the blockchain.
    Returns:
        dict: Metadata of the transaction.
    """
    headers = {"Authorization": f"Bearer {API_KEY}"}
    url = f"{BASE_URL}/transactions/{transaction_id}/metadata"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Failed to fetch metadata for transaction {transaction_id}: {e}")


def get_policy_assets(policy_id):
    """
    Retrieve all assets under a specific policy ID using Maestro API.
    Args:
        policy_id (str): Policy ID.
    Returns:
        list: List of assets.
    """
    headers = {"Authorization": f"Bearer {API_KEY}"}
    url = f"{BASE_URL}/policies/{policy_id}/assets"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
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