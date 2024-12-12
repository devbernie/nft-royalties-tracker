# File: tracker/blockchain.py

import requests

API_BASE_URL = "https://api.koios.rest/api/v0"


def get_transactions(address):
    """
    Truy xuất danh sách giao dịch từ địa chỉ ví Cardano.
    Args:
        address (str): Địa chỉ ví Cardano.
    Returns:
        list: Danh sách các giao dịch liên quan đến NFT.
    """
    url = f"{API_BASE_URL}/address_txs?address={address}"
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Failed to fetch transactions for address {address}: {response.text}")

    transactions = response.json()
    # Lọc các giao dịch liên quan đến NFT
    nft_transactions = [tx for tx in transactions if is_nft_transaction(tx)]
    return nft_transactions


def get_metadata(transaction_id):
    """
    Lấy metadata của NFT từ một giao dịch.
    Args:
        transaction_id (str): ID giao dịch trên blockchain.
    Returns:
        dict: Metadata của giao dịch.
    """
    url = f"{API_BASE_URL}/tx_metadata?tx_hash={transaction_id}"
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Failed to fetch metadata for transaction {transaction_id}: {response.text}")

    metadata = response.json()
    return metadata


def get_policy_assets(policy_id):
    """
    Lấy danh sách tất cả tài sản thuộc một policy NFT.
    Args:
        policy_id (str): ID policy của NFT.
    Returns:
        list: Danh sách tài sản thuộc policy.
    """
    url = f"{API_BASE_URL}/asset_list?policy_id={policy_id}"
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Failed to fetch assets for policy {policy_id}: {response.text}")

    assets = response.json()
    return assets


def is_nft_transaction(transaction):
    """
    Kiểm tra xem giao dịch có liên quan đến NFT không.
    Args:
        transaction (dict): Dữ liệu giao dịch.
    Returns:
        bool: True nếu giao dịch liên quan đến NFT, False nếu không.
    """
    return "nft" in transaction.get("tags", [])