# tests/test_royalties.py

import pytest
from tracker.royalties import calculate_royalties, split_royalties, validate_royalty_structure, calculate_contributor_shares

TOLERANCE = 1e-9  # Ngưỡng sai số cho các phép so sánh dấu chấm động

def test_calculate_royalties():
    transactions = [
        {"metadata": {"sale_price": 1000, "royalty_percentage": 5}},
        {"metadata": {"sale_price": 2000, "royalty_percentage": 10}},
    ]
    total = calculate_royalties(transactions)
    assert abs(total - 250.0) < TOLERANCE

def test_split_royalties():
    transaction = {"metadata": {"sale_price": 1000, "royalty_percentage": 10}}
    contributors = [{"name": "Alice", "share": 50}, {"name": "Bob", "share": 50}]
    splits = split_royalties(transaction, contributors)
    assert abs(splits["Alice"] - 50.0) < TOLERANCE
    assert abs(splits["Bob"] - 50.0) < TOLERANCE

def test_validate_royalty_structure():
    valid_metadata = {"sale_price": 1000, "royalty_percentage": 5}
    invalid_metadata = {"sale_price": 1000}
    assert validate_royalty_structure(valid_metadata) is True
    assert validate_royalty_structure(invalid_metadata) is False

def test_calculate_contributor_shares():
    transactions = [
        {"metadata": {"sale_price": 1000, "royalty_percentage": 10}},
        {"metadata": {"sale_price": 2000, "royalty_percentage": 5}},
    ]
    contributors = [{"name": "Alice", "share": 50}, {"name": "Bob", "share": 50}]
    shares = calculate_contributor_shares(transactions, contributors)
    assert abs(shares["Alice"] - 100.0) < TOLERANCE  # Alice's share
    assert abs(shares["Bob"] - 100.0) < TOLERANCE    # Bob's share