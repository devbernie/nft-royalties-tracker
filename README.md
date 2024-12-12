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
nft-tracker list-transactions --address <CardanoWalletAddress>
```

#### **Calculate Total Royalties**
Compute total royalties from a JSON file containing transaction data:
```bash
nft-tracker calculate --transactions transactions.json
```

#### **Calculate Contributor Shares**
Distribute royalties among contributors:
```bash
nft-tracker contributor-shares --transactions transactions.json --contributors contributors.json
```

#### **Export Reports**
Generate NFT transaction reports in CSV or PDF format:
```bash
nft-tracker export-report --transactions transactions.json --output report.pdf --format pdf
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

For questions or support, contact [your.email@example.com](mailto:your.email@example.com).
