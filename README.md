
# Hedge Funds on a Swamp: Analyzing Patterns, Vulnerabilities, and Defense Measures in Blockchain Bridges

This repository contains all code, data, and artifacts supporting our paper — including the [Main article + Appendix PDF](./BridgeArticle.pdf).


**Authors:** Poupak Azad (University of Manitoba), Jiahua Xu (University College London), Feng Yebo (Nanyang Technological University), Cüneyt Gürcan Akçora (University of Central Florida)

---

## Overview

Blockchain bridges are critical for moving assets across blockchains, but they have also caused the largest single losses in Web3, often due to repeating the same security mistakes. This repository contains the full code, data, figures, and instructions for reproducing our study, which combines a formal bridge model, static smart contract analysis, and transaction graph evidence to show how and why these failures persist.

Our findings show that even widely used bridges often skip basic safeguards, such as reentrancy protection, apply inconsistent access controls, and rely on small, trusted validator sets or multisignatures that can get compromised. This makes it possible for attackers to forge proofs, bypass verification logic, and drain locked funds. The transaction-level analysis of 43 real exploits shows consistent attacker behavior: funding fresh wallets from mixers for gas fees, probing contracts with small transactions, and rapidly laundering stolen assets through multiple chains and services.

In contrast, we observe that bridges designed around stronger trustless guarantees, such as light-client proofs or rollup-native fraud proofs, have so far avoided catastrophic failures. This suggests that rigorous formal guarantees and minimizing off-chain trust assumptions are effective paths to greater security. By combining static and dynamic perspectives, this work provides a concrete baseline for comparing bridge implementations, identifying recurring weak points, and guiding the design of safer cross-chain systems.


---

## Repository Structure

- `code/`: All analysis scripts for static code analysis, transaction extraction, and graph analytics.
- `data/`: Publicly available datasets, processed on-chain transactions, and contract code snapshots.
- `figs/`: Figures used in the paper. Example: 
  ![Model Diagram](figs/bridge)
- `README.md`: This file.

---

## Reproducing Our Results

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-org/bridge-security-analysis.git
   cd bridge-security-analysis
   ```

2. **Set up your Python environment**

   We recommend using a virtual environment:

   ```bash
   python3 -m venv env
   source env/bin/activate
   pip install -r code/requirements.txt
   ```

3. **Run Static Analysis**

   ```bash
   python code/static_analysis.py --input data/contracts/ --output results/static_results.json
   ```

4. **Run Transaction Network Analysis**

   ```bash
   python code/transaction_analysis.py --input data/transactions/ --output results/tx_analysis.json
   ```

5. **Generate Figures**

   Figures are generated automatically in `figs/`. Example output:

   ![Attack Surface Example](figs/attack_surface_overview.png)

---

## Citing This Work

If you use this code or data, please cite:

```
@article{Azad2025Bridges,
  author  = {Poupak Azad and Jiahua Xu and Feng Yebo and Cüneyt Gürcan Akçora},
  title   = {Hedge Funds on a Swamp: Analyzing Patterns, Vulnerabilities, and Defense Measures in Blockchain Bridges},
  journal = {PVLDB},
  year    = {2025}
}
```

---

## License

This project is released under an open academic license. See [LICENSE](LICENSE) for details.

---

## Contact

For questions or contributions, please open an issue or contact the corresponding author:
[Cüneyt Gürcan Akçora](mailto:cuneyt.akcora@ucf.edu)

 
 
