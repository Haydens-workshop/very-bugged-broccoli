from backend.blockchain.block import Block

class Blockchain:

    def __init__(self):
        self.chain = [Block.genesis()]

    def add_block(self, data):
        self.chain.append(Block.mine_block(self.chain[-1], data))

    def __repr__(self):
        return f'Blockchain: {self.chain}'

def main():

    blockchain = Blockchain()
    blockchain.add_block('one')
    blockchain.add_block('two')

    print(blockchain)
    print(f'blockchain.py __name__: {__name__}')

    
    

@staticmethod

    def mine_block(last_block, data):
      #mine block based on the last_block and data.
      timestamp = time.time_ns()
      last_hash = last_block.hash
      hash = crypto_hash(timestamp, last_hash, data)
      return Block(timestamp, last_hash, hash, data)


def main():
    genesis_block = Block.genesis()
    block = Block.mine_block(genesis_block, 'slurp')
    print(block)

  
  
  
  #generating genesis block.
    @staticmethod
    def genesis():
      return Block(1, 'genesis_last_hash', 'genesis_hash', [])

if __name__ == '__main__':
    main()