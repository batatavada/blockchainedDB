import block_header as bh



class Blockchain():
    def __init__(self):
        """
        CHAIN FORMAT:    KEY    -->      VALUE
                    hashpointer --> block header data
        """
        self.chain = {}
        self.current_transactions = []



        
    def newlock(self, block):
        block = bh.BlockHeader()
        block.createBlock("01000000")





    
    @staticmethod
    def add_Block(block):
        """ Adds a block to the main chain
        """
        validation = self.validate(block)





    @staticmethod
    def __validate(block):
        """ Adds a block to the main chain
        """

        validation = false

        return validation






    
    @property
    def last_block(self):
        # Returns the last Block in the chain
        pass




    
    def new_transaction(self):
        # Adds a new transaction to the list of transactions
        pass



