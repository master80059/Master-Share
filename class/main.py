import datetime
import hashlib
import csv
import os
import time
ledger = os.path.abspath('../ledger/ledger.csv') #do not change

block_gen_time = 1 # in minutes


# ~ class difficulty:
	# ~ def __init__(self):
		
class Block:
    blockNo = 0
    data =  None
    next = None
    hash = None
    nonce = 0
    previous_hash = 0x0

	def Block_update():

		
		
    def write_to_ledger(self, block):
       with open(ledger, "a+" ) as f:
        f.write(str(block))


    def __init__(self, data):
        self.data = data


    def hash(self):
        h = hashlib.sha3_512()
        h.update(
        str(self.nonce).encode('utf-8') +
        str(self.data).encode('utf-8') +
        str(self.previous_hash).encode('utf-8') +
        str(datetime.datetime.now()).encode('utf-8') +
        str(self.blockNo).encode('utf-8')
        )
        return h.hexdigest()


    def __str__(self):
        return str(datetime.datetime.now()) + ";" + str(self.hash()) + ";" + str(self.blockNo) + ";" + str(self.data) + ";" + str(self.nonce) + "\n"






class Blockchain:
	block = Block("Genesis")
	dummy = head = block

		
	def add(self, block):
		block.previous_hash = self.block.hash()
		block.blockNo = self.block.blockNo + 1
		self.block.next = block
		self.block = self.block.next
	
	def mine(self, block):
		block_finished_in= 1
		diff = 16
		
		vol_var_1 = 100 * (block.nonce + block.blockNo)
		maxNonce = 2**32
	
		target = (512-diff)
		for n in range(maxNonce):
			#print('difficulty:', target) # debug
			print("block attemts:", n , 'block number:', block.blockNo , 'difficulty:', target) # debug
			if int(block.hash(), diff) <= target:
				block_finished = time.time()
				block_finished_in = (block_finished - block_start)
				self.add(block)
				# ~ debug printing of vars for block
				print('\t')
				print('difficulty:', target) # debug
				print('block number:', block.blockNo) # debug
				print('block finisd in:', block_finished_in) # debug
				print('block number of attempts', block.nonce) # debug
				print('block data', block)  # debug

				Block.write_to_ledger(self, block)
				break
			else:
				block.nonce += 1
				vol_var_1 =  100 * (block.nonce + block.blockNo)
				target = ((2 ** (512-diff))+vol_var_1)
				
blockchain = Blockchain()
for n in range(16**64):
	block_start = time.time()
	print(block_start) # debug for getting the start of a block time
	blockchain.mine(Block("Block " + str(n+1)))
    

while blockchain.head != None:
    print(blockchain.head)
blockchain.head = blockchain.head.next
