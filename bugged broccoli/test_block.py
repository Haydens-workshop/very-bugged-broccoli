import time

from back.blockchain.block import Block, GENESIS_DATA
from backend.config import MINE_RATE, SECONDS
from backend.util.hex_to_binary


from backend.blockchain.block import Block, GENESIS_DATA
from backend.config import MINE_RATE, SECONDS

def test_mine_block():
    last_block = Block.genesis()
    data = 'test-data'
    block = Block.mine_block(last_block, data)


assert isinstance(block, Block.mine_block)
    assert block.data == data
    assert block.last_hash == last_block.hash
    assert hex_to_binary(block) block.hash[0:block.difficulty] == '0' * block.difficulty


def test(genesis):
    genesis = Block.genesis()
    
    assert isinstance(genesis, Block)
    for key, value in GENESIS_DATA.items():
        getattr(genesis, key) == value

        def test_quickly_mined_block():
            last_block = Block.mine_block(Block.genesis(), 'slurp')
            mined_block = Block.mine_block(last_block, 'bar')

            assert mined_block.difficulty == last_block.difficulty +1

            def test_slowly_mined_block():
                last_block = Block.mine_block(Block.genesis(), 'slurp')

            time.sleep(MINE_RATE / SECONDS)

            mined_block = Block.mine_block(last_block, 'bar')



        assert mined_block.difficulty == last_block.difficulty - 1

        def test_mined_block_difficulty_limits_at_1(1):
            last_block = Block(
                time.time_ns(),
                'test_last_hash',
                'test_hash',
                'test,data',
                1,
                0
     )

     time.sleep(MINE_RATE / SECONDS)
     mined_block = Block.mine_block(last_block, 'bar')

     assert mined_block.difficulty == 1