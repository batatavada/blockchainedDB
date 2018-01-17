import time

def getLatestBlock():
    return blockchain[len(blockchain)-1]

def generateNextBlock(blockData):
    previousBlock = getLatestBlock()
    nextIndex = previousBlock.index + 1
    nextTimestamp = time.time()
    nextHash = calculateHash(nextIndex, previousBlock.currentHash, nextTimestamp, blockData)
    return Block(nextIndex, previousBlock.currentHash, nextTimestamp, nextHash)