import pytest
import subprocess
from tracker.blockchain import get_transactions, get_metadata, get_policy_assets, is_nft_transaction

@pytest.fixture
def mock_transactions():
    return [
        {"policy_id": "policy_1", "asset": "asset_1"},
        {"metadata": {"key": "value"}}
    ]

@pytest.fixture
def mock_socket_path():
    return "cardano-node-10.1.3-win64/db/node.socket"

def test_get_transactions_success(mocker, mock_socket_path):
    mock_output = """
    TxHash                                 TxIx        Amount
    --------------------------------------------------------------------------------------
    abc123...                              0           1000000 lovelace + 1 policy1.asset1
    def456...                              1           2000000 lovelace + 1 policy1.asset2
    """
    mocker.patch("subprocess.run", return_value=mocker.Mock(stdout=mock_output, returncode=0))
    transactions = get_transactions("addr_test1...", mock_socket_path)  # Sử dụng mock_socket_path
    assert len(transactions) == 2
    assert transactions[0]["tx_hash"] == "abc123..."


def test_get_transactions_error(mocker):
    mocker.patch("subprocess.run", side_effect=subprocess.CalledProcessError(1, "cardano-cli", stderr="Failed to fetch transactions"))
    with pytest.raises(ValueError, match="Failed to fetch transactions"):
        get_transactions("addr_invalid", mock_socket_path)


def test_get_metadata_success(mocker):
    mock_output = '{"key": "value"}'
    mocker.patch("subprocess.run", return_value=mocker.Mock(stdout=mock_output, returncode=0))
    metadata = get_metadata("tx_hash")
    assert metadata["key"] == "value"


def test_get_policy_assets(mocker):
    mock_output = '[{"asset": "asset1"}, {"asset": "asset2"}]'
    mocker.patch("subprocess.run", return_value=mocker.Mock(stdout=mock_output, returncode=0))
    assets = get_policy_assets("policy_id")
    assert len(assets) == 2
    assert assets[0]["asset"] == "asset1"
    assert assets[1]["asset"] == "asset2"


def test_is_nft_transaction(mock_transactions):
    assert is_nft_transaction(mock_transactions[0]) is True
    assert is_nft_transaction(mock_transactions[1]) is False