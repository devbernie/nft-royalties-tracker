# File: tracker/blockchain.py

import subprocess
import json

def run_cli_command(command):
    """
    Run a Cardano CLI command and return the output.
    Args:
        command (list): Command arguments as a list.
    Returns:
        dict: Parsed JSON output from the CLI.
    """
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        raise ValueError(f"CLI command failed: {e.stderr}")

def get_transactions(address, socket_path):
    """
    Retrieve transactions related to a Cardano address using Cardano CLI.
    Args:
        address (str): Cardano wallet address.
        socket_path (str): Path to the Cardano node socket.
    Returns:
        list: List of transactions.
    """
    command = [
        "cardano-cli", "query", "utxo",
        "--address", address,
        "--testnet-magic", "1097911063",  # Thay bằng giá trị magic nếu dùng mainnet
        "--socket-path", socket_path
    ]
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        raw_output = result.stdout.splitlines()
        if len(raw_output) <= 2:
            return []  # Không có giao dịch
        transactions = []
        for line in raw_output[2:]:
            parts = line.split()
            if len(parts) < 3:
                continue  # Bỏ qua dòng không hợp lệ
            transactions.append({
                "tx_hash": parts[0],
                "tx_index": parts[1],
                "amount": parts[2:]
            })
        return transactions
    except subprocess.CalledProcessError as e:
        raise ValueError(f"Failed to fetch transactions: {e.stderr}")


def get_metadata(transaction_id):
    """
    Retrieve metadata of an NFT transaction using Cardano CLI.
    Args:
        transaction_id (str): Transaction ID on the blockchain.
    Returns:
        dict: Metadata of the transaction.
    """
    command = [
        "cardano-cli", "query", "tx-metadata",
        "--tx-in", transaction_id,
        "--testnet-magic", "1097911063"
    ]
    try:
        return run_cli_command(command)
    except ValueError as e:
        raise ValueError(f"Failed to fetch metadata for transaction {transaction_id}: {e}")


def get_policy_assets(policy_id):
    """
    Retrieve all assets under a specific policy ID using Cardano CLI.
    Args:
        policy_id (str): Policy ID.
    Returns:
        list: List of assets.
    """
    command = [
        "cardano-cli", "query", "policy-id",
        "--policy-id", policy_id,
        "--testnet-magic", "1097911063"
    ]
    try:
        return run_cli_command(command)
    except ValueError as e:
        raise ValueError(f"Failed to fetch assets for policy {policy_id}: {e}")


def is_nft_transaction(transaction):
    """
    Check if a transaction involves NFTs.
    Args:
        transaction (dict): Transaction data.
    Returns:
        bool: True if the transaction involves NFTs, False otherwise.
    """
    # Example logic: Look for specific metadata or tags
    return "policy_id" in transaction or "asset" in transaction