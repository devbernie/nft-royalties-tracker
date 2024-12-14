# File: tracker/royalties.py

def calculate_royalties(transactions):
    """
    Tính toán tổng tiền bản quyền từ danh sách giao dịch NFT.
    Args:
        transactions (list): Danh sách các giao dịch NFT.
    Returns:
        float: Tổng tiền bản quyền.
    """
    total_royalties = 0.0
    for tx in transactions:
        metadata = tx.get("metadata", {})
        royalty_percentage = metadata.get("royalty_percentage", 0)
        sale_price = metadata.get("sale_price", 0)

        royalty = (royalty_percentage / 100) * sale_price
        total_royalties += royalty

    return total_royalties


def split_royalties(transaction, contributors):
    """
    Chia tiền bản quyền giữa nhiều tác giả.
    Args:
        transaction (dict): Thông tin giao dịch NFT.
        contributors (list): Danh sách đồng tác giả với tỷ lệ phân chia.
    Returns:
        dict: Tiền bản quyền phân chia cho từng đồng tác giả.
    """
    metadata = transaction.get("metadata", {})
    royalty_percentage = metadata.get("royalty_percentage", 0)
    sale_price = metadata.get("sale_price", 0)

    total_royalty = (royalty_percentage / 100) * sale_price
    splits = {}

    for contributor in contributors:
        name = contributor.get("name")
        share = contributor.get("share", 0)  # Share tính theo %
        splits[name] = (share / 100) * total_royalty

    return splits


def validate_royalty_structure(metadata):
    """
    Kiểm tra cấu trúc metadata có tuân thủ tiêu chuẩn royalties.
    Args:
        metadata (dict): Metadata cần kiểm tra.
    Returns:
        bool: True nếu hợp lệ, False nếu không.
    """
    required_keys = ["royalty_percentage", "sale_price"]
    for key in required_keys:
        if key not in metadata:
            return False
    return True


def calculate_contributor_shares(transactions, contributors):
    """
    Calculate detailed royalty shares for each contributor across multiple transactions.
    Args:
        transactions (list): List of NFT transactions.
        contributors (list): List of contributors with their share percentages.
    Returns:
        dict: Total royalties for each contributor.
    """
    # Initialize totals for each contributor
    contributor_totals = {contributor.get("name"): 0 for contributor in contributors}

    for tx in transactions:
        metadata = tx.get("metadata", {})
        royalty_percentage = metadata.get("royalty_percentage", 0)
        sale_price = metadata.get("sale_price", 0)

        # Total royalty for this transaction
        total_royalty = (royalty_percentage / 100) * sale_price

        # Distribute royalties among contributors
        total_share_percentage = sum(contributor.get("share", 0) for contributor in contributors)
        if total_share_percentage == 0:
            raise ValueError("Total contributor share percentage cannot be zero.")

        for contributor in contributors:
            name = contributor.get("name")
            share = contributor.get("share", 0)  # Share in %
            # Adjust share proportional to the total percentage
            contributor_totals[name] += (share / total_share_percentage) * total_royalty

    return contributor_totals