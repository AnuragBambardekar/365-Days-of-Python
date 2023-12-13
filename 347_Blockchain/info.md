# Coding a Blockchain

## Background

A blockchain is a secure and transparent way of recording and transferring information across a network of computers, without the need for a central authority. It's the technology behind cryptocurrencies like Bitcoin, but its applications go beyond currency, reaching into areas like supply chain management, voting systems, and more.

1. What is a Blockchain?

A blockchain is like a digital ledger or a record-keeping system, but instead of being stored in one central place, it is distributed across a network of computers. Imagine it as a shared document that many people can access and update simultaneously.

2. How Does it Work?

Each piece of information (like a transaction in a financial system) is grouped into a "block." When a block is filled with data, it gets a unique code called a "hash." This hash is like a fingerprint for that block and is based on the information inside it.

The clever part is that each block also contains the hash of the previous block in the chain. This creates a link between all the blocks, forming a "chain" of information. If someone tries to tamper with a block, it not only changes that block's hash but also the hashes of all the subsequent blocks, alerting the network that something is amiss.

3. Why is it Called a Blockchain?

It's called a "blockchain" because of this chain of blocks, where each block points to the previous one, creating a continuous and unbroken chain of information.

4. Decentralization and Security:

Because the information is stored on a network of computers (often referred to as nodes), there's no central authority or single point of control. This decentralized nature makes it very secure. For someone to tamper with the information in a block, they would need to control the majority of the network, which is highly unlikely in a well-designed blockchain.

5. Transparency and Trust:

Everyone in the network has a copy of the entire blockchain. This transparency ensures that everyone can verify the transactions, making the system trustworthy. If one copy of the ledger is altered, it won't match the others, and the tampering attempt will be identified.

6. Smart Contracts (Optional):

Some blockchains, like Ethereum, allow the creation of "smart contracts." These are self-executing contracts where the terms of the agreement are directly written into the code. For example, if certain conditions are met, like a payment arriving on a specific date, the contract automatically executes without the need for intermediaries.

## Example
A simple example of a blockchain for a hypothetical cryptocurrency called BambaCoin (BC). In this example, you're using the function BambaHash() for hashing, and each block in the blockchain will contain information about transactions and the hash of the previous block.

**Genesis Block (B1):**

Initial state: "AAA" <br>
*Transactions:* <br>
Alice sends Bob 2 BC <br>
Bob sends Daniel 4.3 BC <br>
Mark sends Charlie 3.2 BC <br>
Hash: BambaHash("AAA", t1, t2, t3) -> 76fd89 <br>
So, the first block (Genesis Block) has the information "AAA" and transactions t1, t2, and t3. Its hash is 76fd89.

**Second Block (B2):**

Previous Hash: 76fd89 (hash of the first block) <br>
*Transactions:* <br>
[Additional transactions, let's call them t4, t5, t6] <br>
Hash: BambaHash(76fd89, t4, t5, t6) -> 8923ff <br>
The second block refers to the first block by including its hash (76fd89) and contains new transactions (t4, t5, t6). Its own hash is calculated using BambaHash() and is 8923ff. <br>

**Third Block (B3):**

Previous Hash: 8923ff (hash of the second block) <br>
*Transactions:* <br>
[Additional transactions, let's call them t7, t8, t9] <br>
Hash: BambaHash(8923ff, t7, t8, t9) -> [new hash] <br>
Similarly, the third block refers to the second block, includes new transactions, and calculates its own hash using BambaHash(). <br>

This process continues as you add more blocks to the chain. Each block references the hash of the previous block, creating a chain that is secure against tampering. If someone tries to alter the information in a block, it will change that block's hash and all subsequent blocks' hashes, alerting the network to the tampering attempt.

In real-world scenarios, the BambaHash() function would be a cryptographic hash function, such as SHA-256, providing the necessary security for the blockchain.

