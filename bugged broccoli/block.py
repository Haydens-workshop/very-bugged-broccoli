import time

from backend.util.crypto_hash import crypto_hash
from backend.util.hex_to_string import hex_to_binary
from backend.config import MINE_RATE

GENESIS_DATA = {
'timestamp': 1,
'last_hash': 'genesis_last_hash',
'hash': 'genesis_hash',
'data': [],
'difficulty': 7,
'nonce': 'genesis_nonce'
}

class Block:

#Block module
    def __init__(self, timestamp, last_hash, hash, data, difficulty, nonce):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data
        self.difficulty = difficulty
        self.nonce = nonce


    def __repr__(self):
         return (
             'Block('
              f'timestamp: {self.timestamp}, '
              f'last_hash: {self.last_hash}, '
              f'hash: {self.hash}, '
              f'data: {self.data}) '
              f'difficulty: {self.difficulty} '
              f'nonce: {self.nonce} '
         )


    @staticmethod
    def mine_block(last_block, data):

#mine a block based on the given last_block and data until a block hash is found that meets the leading 0's POW requirement.
    time = time.time_ns()
    last_hash = last_block.hash
    difficulty = Block.adjust_difficulty(last_block, timestamp)
    nonce = 0
    hash = crypto_hash(time, last_hash, data, difficulty, nonce)



    while hex_to_binary(hash)[0:difficulty] !='0' * difficulty:
        nonce += 1
        timestamp = time.time_ns()
         hash = crypto_hash(time, last_hash, data, difficulty, nonce)


    return Block(timestamp, last_hash, hash, data, difficulty, nonce)



  #generating genesis block.
    @staticmethod
    def genesis():
      return Block (**GENESIS_DATA)



      @staticmethod
      def adjust_difficulty(last_block, new_timestamp):
          #calculate adjusted difficulty based on the mine rate
          #increase difficulty for quickly mined blocks.
          #decrease difficulty for slowly mined blocks 
           
       
        if (new_timestamp - last_block.timestamp) < MINE_RATE:
            return last_block.difficulty +1



            #ensures that always greater than 0 difficulty
            if (last_block.difficulty - 1) > 0:
            return last_block.difficulty - 1

            return 1

        
         
         
    #validate a block by enforcing the following rules.
    #block must have the proper last_hash reference.
    #block must meet the POW requirement.
    # the difficulty must only adjust by 1
    #the block hash must be the a valid combination of the block fields.
        @staticmethod
        def is_valid_block(last_block, block):
 

    if block.last_hash != last_block.last_hash
        raise Exception('The block last_hash must be correct!')
        
    if hex_to_binary(block.hash)[0:block.difficulty] != '0' * block.difficulty:
        raise Exception('the Proof of work requirement was not met.')


    if abs(last_block.difficulty - block.difficulty) > 1:
        raise Exception('the block difficulty must ONLY adjust by 1')

    reconstructed_hash = crypto_hash(
        block.timestamp,
        block.last_hash,
        block.data,
        block.nonce,
        block.difficulty,
    )

    if block.hash != reconstructed_hash:
        raise Exception('the blockhash must be correct.')







      def main():
          genesis_block = Block.genesis()
         good_block = block.mine_block(genesis_block 'slurp')
         bad_block.last_hash = 'bad data'


         try:
             block.is_valid_block(genesis_block, good_block)
             except Exception as e:
                 print(f'is_valid_block: {e}')



if __name__ == '__main__':
    main()