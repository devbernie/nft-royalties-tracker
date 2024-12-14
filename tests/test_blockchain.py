# tests/test_blockchain.py

import pytest
import requests
from tracker.blockchain import get_transactions, get_metadata, get_policy_assets, is_nft_transaction

@pytest.fixture
def mock_transactions():
    return [
        {"policy_id": "policy_1", "asset": "asset_1"},
        {"metadata": {"key": "value"}}
    ]

@pytest.fixture
def mock_address():
    return "addr_test1qpz..."

@pytest.fixture
def mock_transaction_id():
    return "abc123..."

@pytest.fixture
def mock_policy_id():
    return "policy_id_123"

@pytest.fixture
def mock_maestro_api_key():
    return "test_api_key"

def test_get_transactions_success(mocker, mock_address):
    mock_response = [
        {"tx_hash": "abc123...", "tx_index": 0, "amount": [{"unit": "lovelace", "quantity": "1000000"}]},
        {"tx_hash": "def456...", "tx_index": 1, "amount": [{"unit": "lovelace", "quantity": "2000000"}]}
    ]
    mocker.patch("requests.get", return_value=mocker.Mock(status_code=200, json=lambda: mock_response))

    transactions = get_transactions(mock_address)
    assert len(transactions) == 2
    assert transactions[0]["tx_hash"] == "abc123..."
    assert transactions[1]["tx_index"] == 1


def test_get_transactions_error(mocker, mock_address):
    mocker.patch("requests.get", side_effect=requests.exceptions.RequestException("Connection error"))
    with pytest.raises(ValueError, match="Failed to fetch transactions"):
        get_transactions(mock_address)


def test_get_metadata_success(mocker, mock_transaction_id):
    mock_response = {"key": "value"}
    mocker.patch("requests.get", return_value=mocker.Mock(status_code=200, json=lambda: mock_response))

    metadata = get_metadata(mock_transaction_id)
    assert metadata["key"] == "value"


def test_get_metadata_error(mocker, mock_transaction_id):
    mocker.patch("requests.get", side_effect=requests.exceptions.RequestException("Connection error"))
    with pytest.raises(ValueError, match=f"Failed to fetch metadata for transaction {mock_transaction_id}"):
        get_metadata(mock_transaction_id)


def test_get_policy_assets_success(mocker, mock_policy_id):
    mock_response = [{"asset": "asset1"}, {"asset": "asset2"}]
    mocker.patch("requests.get", return_value=mocker.Mock(status_code=200, json=lambda: mock_response))

    assets = get_policy_assets(mock_policy_id)
    assert len(assets) == 2
    assert assets[0]["asset"] == "asset1"
    assert assets[1]["asset"] == "asset2"


def test_get_policy_assets_error(mocker, mock_policy_id):
    mocker.patch("requests.get", side_effect=requests.exceptions.RequestException("Connection error"))
    with pytest.raises(ValueError, match=f"Failed to fetch assets for policy {mock_policy_id}"):
        get_policy_assets(mock_policy_id)


def test_is_nft_transaction(mock_transactions):
    assert is_nft_transaction(mock_transactions[0]) is True
    assert is_nft_transaction(mock_transactions[1]) is False