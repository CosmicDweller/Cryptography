import datetime as d # import the datetime library for our block timestamp and rename it as d for simplicity while typing 
import hashlib as h # import the library for hashing our block data and rename it as h for simplicity while typing 


class Block: # create a Block class
    def __init__(self,index,timestamp,data ,prevhash, nonce): # declare an initial method that defines a block, a block contains the following information
        self.index = index # a block contains an ID
        self.timestamp =timestamp # a block contains a timestamp
        self.data = data # a block contains some transactions
        self.prevhash =prevhash # a block contains a hash of the previous block
        self.nonce = nonce
        self.hash =self.hashblock()

    def hashblock (self):
        block_encryption=h.sha256()
        block_encryption.update((str(self.index)+str(self.timestamp)+str(self.data)+str(self.prevhash) + str(self.nonce)).encode())
        return block_encryption.hexdigest()
    
    @staticmethod
    def genesisblock():
        return Block(0,d.datetime.now(),"genesis block transaction"," ", " ")
    
    @staticmethod
    def newblock(lastblock, nonce):
        index = lastblock.index+1
        timestamp = d.datetime.now()
        hashblock = lastblock.hash
        data = "Transaction " +str(index)
        return Block(index,timestamp,data,hashblock, nonce)
    
    def __str__(self):
        
        return "-----\nIndex: {}\nTimestamp: {}\nData: {}\nPrev Hash: {}\nNonce: {}\nHash: {}\n-----".format(self.index, self.timestamp, self.data, self.prevhash, self.nonce, self.hash)

def validate_blockchain(blockchain):
    for i in range(1, len(blockchain)):
        current_block = blockchain[i]
        previous_block = blockchain[i - 1]

        if current_block.prevhash != previous_block.hash:
            return False

        recalculated_hash = current_block.hashblock()
        if current_block.hash != recalculated_hash:
            return False

    return True 


blockchain = [Block.genesisblock()]
prevblock = blockchain[0]
num_zeros = 10

for i in range(1, 6):
    prevblock = blockchain[i - 1]
    nonce = 0
    while True:
        block = Block.newblock(prevblock, nonce)
        block_hash = block.hash

        first_n_digits = block_hash[0:num_zeros]

        if first_n_digits == "0"*num_zeros:
            blockchain.append(block)
            # print("Successful Nonce:", nonce)
            # print("Valid block:", block.hash)
            break
        nonce += 1

for block in blockchain:
    print(block)
