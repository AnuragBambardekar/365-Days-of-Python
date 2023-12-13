import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        # Create the first block (genesis block)
        genesis_block = Block(0, "0", time.time(), "Genesis Block", self.calculate_hash(0))
        self.chain.append(genesis_block)

    def add_block(self, data):
        # Add a new block to the blockchain
        previous_block = self.chain[-1]
        index = previous_block.index + 1
        timestamp = time.time()
        hash = self.calculate_hash(index, previous_block.hash, timestamp, data)
        new_block = Block(index, previous_block.hash, timestamp, data, hash)
        self.chain.append(new_block)

    def calculate_hash(self, index, previous_hash=None, timestamp=None, data=None):
        # Calculate the hash of a block
        hash_string = str(index) + str(previous_hash) + str(timestamp) + str(data)
        return hashlib.sha256(hash_string.encode()).hexdigest()

if __name__ == "__main__":
    # Create a blockchain
    my_blockchain = Blockchain()

    # Add some blocks
    my_blockchain.add_block("Transaction 1")
    my_blockchain.add_block("Transaction 2")
    my_blockchain.add_block("Transaction 3")

    # Print the blockchain
    for block in my_blockchain.chain:
        print(f"Block #{block.index} [{block.timestamp}]: {block.data}, Hash: {block.hash}")
