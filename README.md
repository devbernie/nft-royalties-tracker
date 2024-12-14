# NFT Royalties Tracker

NFT Royalties Tracker is a powerful CLI tool designed to help artists and content creators track and manage royalties for NFTs on the Cardano blockchain. With this tool, you can calculate royalties, split revenues among contributors, and export detailed reports.

## 1. Current Situation

NFTs have become a significant trend in the blockchain space, providing opportunities for artists and content creators. However, tracking and managing royalties from NFT resales often depend on third-party platforms such as marketplaces. This reliance leads to a lack of transparency and autonomy for artists, especially when quick data retrieval or revenue sharing is needed.

## 2. Opportunities

- **Practical Demand:** Artists and creators increasingly need independent tools to manage royalties without relying on marketplaces.
- **Scalability:** Cardano, with its growing NFT community, offers a large market for tools like NFT Royalties Tracker.
- **Transparency:** This CLI tool provides clear and accurate information directly from the blockchain.

## 3. Challenges

- **Complex Data Handling:** NFT transactions may involve multiple contributors and complex royalty structures.
- **Standards Integration:** Ensuring compliance with new standards like CIP-68 on Cardano.
- **User Experience:** Making the CLI tool user-friendly for non-technical users.

## 4. Solution

NFT Royalties Tracker is an open-source CLI tool offering:
- **Automated Royalties Calculation:** Based on transaction data from the blockchain.
- **Revenue Sharing:** Supports royalty distribution among multiple contributors.
- **Report Exporting:** Easily create detailed reports in CSV or PDF formats.

## 5. Usage Demo

### **Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/nft-royalties-tracker.git
   cd nft-royalties-tracker
   ```

2. Install the tool:
   ```bash
   pip install .
   ```

### **CLI Commands**

#### **List Transactions**
Retrieve NFT transactions from a Cardano wallet:
```bash
python -m tracker.cli list-transactions --address <Cardano_wallet_address>
```
Example:
```bash
python -m tracker.cli list-transactions --address addr_test1qp28mg795hwlnptmdyr47zcrc87m8kk0pwvxrwrw24ppdzzquca5pnk4ew6068z6wu4tc9ee2rr2rnn06spkkvj0llqq7fnt8u
```
Example Output:
```bash
{'value': '10000000000', 'tx_hash': 'd3b8b38df483babb8c2ba5d1d20b798024784c29a51a7637ee6e99da0ea6fc16', 'tx_index': 0, 'asset_list': [], 'block_time': 1734005201, 'datum_hash': None, 'block_height': 2762260, 'inline_datum': None, 'reference_script': None}
```


#### **Calculate Total Royalties**
Compute total royalties from a JSON file containing transaction data:
```bash
python -m tracker.cli calculate --address <Cardano_wallet_address>
```
Example:
```bash
python -m tracker.cli calculate --address addr_test1qp28mg795hwlnptmdyr47zcrc87m8kk0pwvxrwrw24ppdzzquca5pnk4ew6068z6wu4tc9ee2rr2rnn06spkkvj0llqq7fnt8u
```
Example Output:
```bash
Total royalties: 2000.00 ADA
```


#### **Calculate Contributor Shares**
Distribute royalties among contributors:
```bash
python -m tracker.cli contributor-shares --address <Cardano_wallet_address> --contributors <contributors_file_path>
```
Example:
```bash
python -m tracker.cli contributor-shares --address addr_test1qp28mg795hwlnptmdyr47zcrc87m8kk0pwvxrwrw24ppdzzquca5pnk4ew6068z6wu4tc9ee2rr2rnn06spkkvj0llqq7fnt8u --contributors contributors.json
```
Example Output:
```bash
Alice: 1000.00 ADA
Bob: 1000.00 ADA
```

#### **Export Reports**
Generate NFT transaction reports in CSV or PDF format:
```bash
python -m tracker.cli export-report --address <Cardano_wallet_address> --output <output_file_name> --format <output_format>
```
Example:
```bash
python -m tracker.cli export-report --address addr_test1qp28mg795hwlnptmdyr47zcrc87m8kk0pwvxrwrw24ppdzzquca5pnk4ew6068z6wu4tc9ee2rr2rnn06spkkvj0llqq7fnt8u --output report.csv --format csv
```

```bash
python -m tracker.cli export-report --address addr_test1qp28mg795hwlnptmdyr47zcrc87m8kk0pwvxrwrw24ppdzzquca5pnk4ew6068z6wu4tc9ee2rr2rnn06spkkvj0llqq7fnt8u --output report.pdf --format pdf
```

### **Example JSON Files**

#### Transactions File (`transactions.json`)
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

#### Contributors File (`contributors.json`)
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

## 6. Conclusion

NFT Royalties Tracker provides a practical and efficient solution for artists and creators to manage NFT royalties. This tool not only enhances transparency but also improves user autonomy within the blockchain ecosystem.

## 7. Future Improvements and Development Directions

- **Integrating New Standards:** Support for CIP-68 and advanced NFT standards.
- **Automation Features:** Directly distribute royalties to contributor wallets.
- **User Interface:** Develop a GUI version to reach non-technical users.
- **Multi-Blockchain Support:** Expand to other blockchains like Ethereum and Solana.

## Development

To set up the development environment:
```bash
pip install -r requirements.txt
```

Run tests using `pytest`:
```bash
pytest
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, contact [dev.bernie@gmail.com](mailto:dev.bernie@gmail.com).
