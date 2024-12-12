**NFT Royalties Tracker**

NFT Royalties Tracker is a powerful CLI tool designed to help artists and content creators track and manage royalties for NFTs on the Cardano blockchain. With this tool, you can calculate royalties, split revenues among contributors, and export detailed reports.

**Features**

- **List NFT Transactions:** Retrieve and display NFT-related transactions from a Cardano wallet.
- **Calculate Royalties:** Compute total royalties earned from a list of transactions.
- **Split Royalties:** Distribute royalties among multiple contributors based on predefined shares.
- **Export Reports:** Generate transaction reports in CSV or PDF format.

**Installation**

1. Clone the repository:
2. git clone <https://github.com/yourusername/nft-royalties-tracker.git>

cd nft-royalties-tracker

1. Install the tool using pip:
    ```bash
    pip install .

**Usage**

After installation, you can use the nft-tracker command. Below are the available commands:

**List Transactions**

Retrieve a list of NFT-related transactions from a Cardano wallet.
    ```bash
    nft-tracker list-transactions --address &lt;CardanoWalletAddress&gt;

**Calculate Total Royalties**

Compute total royalties from a JSON file containing transaction data.
    ```bash
    nft-tracker calculate --transactions transactions.json

**Calculate Contributor Shares**

Distribute royalties among contributors based on their shares.
    ```bash
    nft-tracker contributor-shares --transactions transactions.json --contributors contributors.json

**Export Reports**

Generate a report of NFT transactions in CSV or PDF format.
    ```bash
    nft-tracker export-report --transactions transactions.json --output report.pdf --format pdf

**NFT Royalties Tracker**

NFT Royalties Tracker is a powerful CLI tool designed to help artists and content creators track and manage royalties for NFTs on the Cardano blockchain. With this tool, you can calculate royalties, split revenues among contributors, and export detailed reports.

**Features**

- **List NFT Transactions:** Retrieve and display NFT-related transactions from a Cardano wallet.
- **Calculate Royalties:** Compute total royalties earned from a list of transactions.
- **Split Royalties:** Distribute royalties among multiple contributors based on predefined shares.
- **Export Reports:** Generate transaction reports in CSV or PDF format.

**Installation**

1. Clone the repository:

   ```bash
   git clone <https://github.com/yourusername/nft-royalties-tracker.git>
   ```

2. Navigate to the project directory:

   ```bash
   cd nft-royalties-tracker
   ```

3. Install the tool using pip:

   ```bash
   pip install .
   ```

**Usage**

After installation, you can use the `nft-tracker` command. Below are the available commands:

**List Transactions**

Retrieve a list of NFT-related transactions from a Cardano wallet.

```bash
nft-tracker list-transactions --address <CardanoWalletAddress>
```

**Calculate Total Royalties**

Compute total royalties from a JSON file containing transaction data.

```bash
nft-tracker calculate --transactions transactions.json
```

**Calculate Contributor Shares**

Distribute royalties among contributors based on their shares.

```bash
nft-tracker contributor-shares --transactions transactions.json --contributors contributors.json
```

**Export Reports**

Generate a report of NFT transactions in CSV or PDF format.

```bash
nft-tracker export-report --transactions transactions.json --output report.pdf --format pdf
```

**Example JSON Files**

**Transactions File (`transactions.json`)**

```json
[
  {
    "metadata": {
      "sale_price": 1000,
      "royalty_percentage": 10
    }
  },
  {
    "metadata": {
      "sale_price": 2000,
      "royalty_percentage": 5
    }
  }
]
```

**Contributors File (`contributors.json`)**

```json
[
  {
    "name": "Alice",
    "share": 50
  },
  {
    "name": "Bob",
    "share": 50
  }
]
```

**Development**

To set up the development environment:

```bash
pip install -r requirements.txt
```

Run tests using pytest:

```bash
pytest
```

**Contributing**

Contributions are welcome! Please open an issue or submit a pull request with your improvements.

**License**

This project is licensed under the MIT License. See the LICENSE file for details.

**Contact**

For questions or support, contact <dev.bernie@gmail.com>.

**Development**

To set up the development environment:

```bash
pip install -r requirements.txt
```

Run tests using pytest:

```bash
pytest
```

**Contributing**

Contributions are welcome! Please open an issue or submit a pull request with your improvements.

**License**

This project is licensed under the MIT License. See the LICENSE file for details.

**Contact**

For questions or support, contact <dev.bernie@gmail.com>.
