# File: tracker/cli.py

import click
import os
from tracker.utils import read_json, write_csv, write_pdf, log_message
from tracker.blockchain import get_transactions, get_metadata
from tracker.royalties import calculate_royalties, calculate_contributor_shares

def auto_detect_socket_path():
    # Danh sách các đường dẫn phổ biến của node.socket
    common_paths = [
        "/db/node.socket",
        "/home/cardano/node.socket"
    ]
    for path in common_paths:
        if os.path.exists(path):
            return path
    raise ValueError("Node socket not found. Please set CARDANO_SOCKET_PATH in .env or provide --socket-path.")

def get_socket_path():
    """
    Retrieve the Cardano node socket path from the environment or configuration.
    Returns:
        str: Path to the Cardano node socket.
    """
    import os
    from dotenv import load_dotenv

    load_dotenv()
    socket_path = os.getenv("CARDANO_SOCKET_PATH")
    if not socket_path or not os.path.exists(socket_path):
        raise ValueError("Node socket not found. Please set CARDANO_SOCKET_PATH in .env or provide --socket-path.")
    return socket_path

@click.group()
def cli():
    """
    NFT Royalties Tracker CLI
    """
    pass


@cli.command()
@click.option('--address', required=True, help='Cardano wallet address.')
@click.option('--socket-path', default=None, help='Path to the Cardano node socket.')
def list_transactions(address, socket_path):
    """
    List NFT transactions from a wallet address.
    """
    try:
        # Nếu người dùng không cung cấp socket-path, lấy từ biến môi trường
        socket_path = socket_path or get_socket_path()
        transactions = get_transactions(address, socket_path)
        if not transactions:
            click.echo(f"No transactions found for address: {address}")
        else:
            for tx in transactions:
                click.echo(tx)
    except ValueError as e:
        click.echo(f"Error: {e}")


@cli.command()
@click.option('--socket-path', required=True, help='Path to the Cardano node socket.')
def configure(socket_path):
    """
    Configure the path to the Cardano node socket.
    """
    with open('.env', 'w') as f:
        f.write(f"CARDANO_SOCKET_PATH={socket_path}\n")
    click.echo("Configuration saved.")

@cli.command()
@click.option('--transactions', required=True, type=click.Path(exists=True), help='JSON file containing transaction list.')
def calculate(transactions):
    """
    Calculate total royalties from a list of NFT transactions.
    """
    try:
        tx_data = read_json(transactions)
        total_royalties = calculate_royalties(tx_data)
        click.echo(f"Total royalties: {total_royalties:.2f} ADA")
    except Exception as e:
        log_message(str(e), level="error")


@cli.command()
@click.option('--transactions', required=True, type=click.Path(exists=True), help='JSON file containing transaction list.')
@click.option('--contributors', required=True, type=click.Path(exists=True), help='JSON file containing contributor information.')
def contributor_shares(transactions, contributors):
    """
    Calculate royalty shares among contributors.
    """
    try:
        tx_data = read_json(transactions)
        contributors_data = read_json(contributors)
        shares = calculate_contributor_shares(tx_data, contributors_data)
        for contributor, amount in shares.items():
            click.echo(f"{contributor}: {amount:.2f} ADA")
    except Exception as e:
        log_message(str(e), level="error")


@cli.command()
@click.option('--transactions', required=True, type=click.Path(exists=True), help='JSON file containing transaction list.')
@click.option('--output', default='report.csv', help='Output file name.')
@click.option('--format', default='csv', type=click.Choice(['csv', 'pdf']), help='Output format (csv or pdf).')
def export_report(transactions, output, format):
    """
    Export a report from the list of NFT transactions.
    """
    try:
        tx_data = read_json(transactions)
        if format == 'csv':
            write_csv(tx_data, output)
        elif format == 'pdf':
            write_pdf(tx_data, output, title="NFT Transactions Report")
        click.echo(f"Report has been exported to file {output}")
    except Exception as e:
        log_message(str(e), level="error")


if __name__ == '__main__':
    cli()