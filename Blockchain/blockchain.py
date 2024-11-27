import logging
import hashlib
import json
import time

# Configure logging to a file
logging.basicConfig(filename='blockchain_logs.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.new_block(previous_hash='1', proof=100)

    def new_block(self, proof, previous_hash=None):
        """
        Creates a new block and adds it to the blockchain.
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        self.current_transactions = []  # Reset the list of current transactions
        self.chain.append(block)

        logging.info(f"New block added: {block}")  # Log block addition
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined block.
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        logging.info(f"New transaction added: {sender} -> {recipient}, Amount: {amount}")  # Log transaction
        return self.last_block['index'] + 1

    def add_password_log(self, password, label):
        """
        Logs a password and its predicted label to the blockchain.
        This method adds a transaction where:
        - sender: 'password'
        - recipient: the predicted label (e.g., 'strong' or 'weak')
        - amount: password length (or any other logic you want to track)
        """
        # Here, 'amount' is the length of the password, and 'recipient' is the predicted label
        self.new_transaction('password', label, len(password))
        logging.info(f"Password added to blockchain: {password} -> {label}")  # Log password addition

        print(f"Added Block: {self.chain[-1]}")  # Debug print


    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a block.
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        """
        Simple proof of work algorithm:
        Find a number p' such that hash(pp') contains 4 leading zeroes,
        where p is the previous proof, and p' is the new proof.
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validates the proof: Does hash(last_proof, proof) contain 4 leading zeroes?
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    def get_chain(self):
        """
        Returns the current blockchain.
        """
        return self.chain

# Initialize Blockchain
blockchain = Blockchain()

# Example usage: Adding password log (Replace with actual password and prediction)
password = 'StrongPassword123'
label = 'strong'  # This should be based on the model's prediction
blockchain.add_password_log(password, label)

# Get and display blockchain chain data
chain_data = blockchain.get_chain()
print("Blockchain:")
for block in chain_data:
    print(block)
    print(f"Block {block['index']}: {block['transactions']}")
