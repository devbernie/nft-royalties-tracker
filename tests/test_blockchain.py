import pytest
from tracker.blockchain import get_transactions, get_metadata, get_policy_assets, is_nft_transaction

@pytest.fixture
def mock_transactions():
    return [
        {"tags": ["nft"], "metadata": {"sale_price": 1000, "royalty_percentage": 5}},
        {"tags": [], "metadata": {}}
    ]

def test_get_transactions_success(mocker):
    mocker.patch("tracker.blockchain.requests.get", return_value=mocker.Mock(status_code=200, json=lambda: [{"tags": ["nft"]}, {"tags": []}]))
    result = get_transactions("addr_test")
    assert len(result) == 1
    assert is_nft_transaction(result[0])

def test_get_transactions_error(mocker):
    mocker.patch("tracker.blockchain.requests.get", return_value=mocker.Mock(status_code=404, text="Not Found"))
    with pytest.raises(ValueError):
        get_transactions("addr_invalid")

def test_get_metadata_success(mocker):
    mocker.patch("tracker.blockchain.requests.get", return_value=mocker.Mock(status_code=200, json=lambda: {"key": "value"}))
    metadata = get_metadata("tx_hash")
    assert metadata["key"] == "value"

def test_is_nft_transaction(mock_transactions):
    assert is_nft_transaction(mock_transactions[0]) is True
    assert is_nft_transaction(mock_transactions[1]) is False