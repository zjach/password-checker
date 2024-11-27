import logging
import time

# Set up logging configuration
logging.basicConfig(
    level=logging.DEBUG,  # You can change this to INFO, WARNING, ERROR, etc.
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('blockchain_logs.txt'),  # Log to a file
        logging.StreamHandler()  # Print logs to the console
    ]
)

logger = logging.getLogger(__name__)

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.new_block(previous_hash='1', proof=100)

    def new_block(self, proof, previous_hash=None):
        """
        Creates a new Block and adds it to the chain
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        self.current_transactions = []  # Reset the list of current transactions
        self.chain.append(block)

        logger.info(f"New Block Added: {block}")  # Log the new block

        return block

    def new_transaction(self, sender, recipient, amount):
        """
        Adds a new transaction to the list of transactions
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        logger.debug(f"New Transaction: {sender} sends {amount} to {recipient}")  # Log the transaction

        return self.last_block['index'] + 1
