import click
from tracker.utils import read_json, write_csv, write_pdf, log_message
from tracker.blockchain import get_transactions, get_metadata
from tracker.royalties import calculate_royalties, calculate_contributor_shares


@click.group()
def cli():
    """
    NFT Royalties Tracker CLI
    """
    pass


@cli.command()
@click.option('--address', required=True, help='Cardano wallet address.')
def list_transactions(address):
    """
    List NFT transactions from a wallet address using Maestro API.
    """
    try:
        transactions = get_transactions(address)
        if not transactions:
            click.echo(f"No transactions found for address: {address}")
        else:
            for tx in transactions:
                click.echo(tx)
    except ValueError as e:
        click.echo(f"Error: {e}")


@cli.command()
@click.option('--address', required=True, help='Cardano wallet address.')
def calculate(address):
    """
    Calculate total royalties from a list of NFT transactions using Maestro API.
    """
    try:
        transactions = get_transactions(address)
        total_royalties = calculate_royalties(transactions)
        click.echo(f"Total royalties: {total_royalties:.2f} ADA")
    except Exception as e:
        log_message(str(e), level="error")


@cli.command()
@click.option('--address', required=True, help='Cardano wallet address.')
@click.option('--contributors', required=True, type=click.Path(exists=True), help='JSON file containing contributor information.')
def contributor_shares(address, contributors):
    """
    Calculate royalty shares among contributors using Maestro API.
    """
    try:
        transactions = get_transactions(address)
        contributors_data = read_json(contributors)
        shares = calculate_contributor_shares(transactions, contributors_data)
        for contributor, amount in shares.items():
            click.echo(f"{contributor}: {amount:.2f} ADA")
    except Exception as e:
        log_message(str(e), level="error")


@cli.command()
@click.option('--address', required=True, help='Cardano wallet address.')
@click.option('--output', default='report.csv', help='Output file name.')
@click.option('--format', default='csv', type=click.Choice(['csv', 'pdf']), help='Output format (csv or pdf).')
def export_report(address, output, format):
    """
    Export a report from the list of NFT transactions.
    """
    try:
        transactions = get_transactions(address)
        if not transactions:
            click.echo(f"No transactions found for address: {address}")
            return
        if format == 'csv':
            write_csv(transactions, output)
        elif format == 'pdf':
            write_pdf(transactions, output, title="NFT Transactions Report")
        click.echo(f"Report has been exported to file {output}")
    except Exception as e:
        log_message(str(e), level="error")


if __name__ == '__main__':
    cli()