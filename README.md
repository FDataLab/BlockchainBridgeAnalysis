
# Hedge Funds on a Swamp: Analyzing Patterns, Vulnerabilities, and Defense Measures in Blockchain Bridges

This repository contains all code, data, and artifacts supporting our paper. Please see the introduction page at https://fdatalab.github.io/BlockchainBridgeAnalysis/.

---

## Overview

Blockchain bridges are critical for moving assets across blockchains, but they have also caused the largest single losses in Web3, often due to repeating the same security mistakes. This repository contains the full code, data, figures, and instructions for reproducing our study, which combines a formal bridge model, static smart contract analysis, and transaction graph evidence to show how and why these failures persist.

Our findings show that even widely used bridges often skip basic safeguards, such as reentrancy protection, apply inconsistent access controls, and rely on small, trusted validator sets or multisignatures that can get compromised. This makes it possible for attackers to forge proofs, bypass verification logic, and drain locked funds. The transaction-level analysis of 43 real exploits shows consistent attacker behavior: funding fresh wallets from mixers for gas fees, probing contracts with small transactions, and rapidly laundering stolen assets through multiple chains and services.

In contrast, we observe that bridges designed around stronger trustless guarantees, such as light-client proofs or rollup-native fraud proofs, have so far avoided catastrophic failures. This suggests that rigorous formal guarantees and minimizing off-chain trust assumptions are effective paths to greater security. By combining static and dynamic perspectives, this work provides a concrete baseline for comparing bridge implementations, identifying recurring weak points, and guiding the design of safer cross-chain systems.

 
 
