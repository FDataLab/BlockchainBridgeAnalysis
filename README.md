
# Hedge Funds on a Swamp
## Analyzing Patterns, Vulnerabilities, and Defense Measures in Blockchain Bridges

This repository contains all code, data, and artifacts supporting our paper:

**Hedge Funds on a Swamp: Analyzing Patterns, Vulnerabilities, and Defense Measures in Blockchain Bridges [Experiment, Analysis & Benchmark]**  
**Authors:** Poupak Azad (University of Manitoba), Jiahua Xu (University College London), Feng Yebo (Nanyang Technological University), Cüneyt Gürcan Akçora (University of Central Florida)

---

## Overview

Blockchain bridges have become vital for cross-chain interoperability, but they remain the single largest source of financial loss in Web3. This repository provides the code, datasets, and reproducibility instructions for our multi-layered study:
- Formalization of bridge models and security priors.
- Static analysis of 13 bridge smart contracts.
- Transaction network analysis covering 43 real-world exploits.
- A unified vulnerability taxonomy and threat model.
- Design guidelines and benchmarks for future bridge security.

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

 
 
