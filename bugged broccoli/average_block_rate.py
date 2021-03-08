import time
from backend.blockchain.blockchain import Blockchain
#https://www.youtube.com/watch?v=F8W9370CHkk

from backend.config import SECONDS


blockchain = Blockchain()

times = []

for i range(1000):
    start_time = time.time_ns()
    blockchain.add_block(i)
    end_time = time.time_ns()

    time_to_mine = end_time - start_time / SECONDS
    times.append(time_to_mine)

    average_time = sum(times) / len(times)

    print(f'new block difficulty: {blockchain.chain[-1].difficulty}')
    print(f'Time to mine new block: {time_to_mine}s')
    print(f'Average time to add all blocks: {average_time}s\n')
