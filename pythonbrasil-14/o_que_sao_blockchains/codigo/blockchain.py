import datetime as dt
import hashlib

class Block:
    blockNumber = 0
    data = None
    next = None
    hash = None
    nonce = 0
    previous_hash = '0x0'
    #Timestamp to register the transaction
    timestamp = dt.datetime.now()

    def __init__(self, data):
        self.data = data

    #Creating our hash of the transaction
    def hash(self):
        h = hashlib.sha256()
        h.update(
            str(self.nonce).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.previous_hash).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.blockNumber).encode('utf-8')
        )

        return h.hexdigest()

    def __str__(self):
        return "Hash: " + str(self.hash()) + "\nBlock Number: " + str(self.blockNumber) + "\nBlock Data: " + str(self.data) + "\nHashes: " + str(self.nonce) + "\n"

class Blockchain:
    # Difficulty of mining
    diff = 20
    maxNonce = 2 ** 32
    target = 2 ** (256 - diff)

    block = Block("Genenis")
    #Genesis is the first block of a blockchain, we instantiate a new Block for start the blockchain
    dummy = head = block

    def add(self, block):
        #Here we do a simple change of data in a linked list
        block.previous_hash = self.block.hash()
        block.blockNumber = self.block.blockNumber + 1

        #The next block of the Blockchain is the block that will be add (block in add method)
        self.block.next = block
        self.block = self.block.next

    def mine(self, block):
        for n in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1

blockchain = Blockchain()

for n in range(10):
    blockchain.mine(Block("Block " + str(n+1)))

while(blockchain.head != None):
    print(blockchain.head)
    blockchain.head = blockchain.head.next