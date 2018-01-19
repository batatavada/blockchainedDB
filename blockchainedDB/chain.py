import block_header as bh



class Blockchain():

    def createChain(self):
        print("createChain")
        """
        CHAIN FORMAT:    KEY    -->      VALUE
                    hashpointer --> block header data
        """
        self.chain = []

        return self



  


    def extendChain(self, version):   
        print("extendChain")
        update_limit = 2
        num_blocks = 10 
        expected_time = 60*5
        self.version = version
        block = self.newBlock(version)
        newBlock = block.getNextBlock(self.chain, update_limit, num_blocks, expected_time)
        return newBlock






    def newBlock(self, version):
        print("newBlock")
        blockHeader = bh.BlockHeader()
        blockHeader.createBlock(self.version, self.prevBlock())
        return blockHeader






    def prevBlock(self):
        print("prevBlock")
        return self.chain[-1]






    def addBlock(self, block):
        print("addBlock")
        self.chain.append(block)




'''
    
    @staticmethod
    def add_Block(block):
        """ Adds a block to the main chain
        """
        validation = self.validate(block)
        if(validation):
            chain.append(block)






    @staticmethod
    def __validate(block):
        """ Adds a block to the main chain
        """

        validation = true

        return validation

'''

