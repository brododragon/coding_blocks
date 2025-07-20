class Block: # base class, everything inherits from
    def __init__(self, block_type):
        self.block_type = block_type

    def __repr__(self):
        return self.block_type
    
class BlockCollection(): # multiple blocks put together; think of a whole script
    def __init__(self, blocks: list):
        self.blocks = blocks

    def run(self): # run through each block
        for block in self.blocks:
            block.run()


## intermediate classes, will be derived from again
class ImperativeBlock(Block):
    def __init__(self, imperative):
        super().__init__("imperative")
        self.imperative = imperative

## end of intermediate classes


class PrintBlock(ImperativeBlock): # simple class to print a string message; could be improved with variable printing, string concat, etc.
    def __init__(self, msg):
        self.block_type = "imperative"
        super().__init__("print")
        self.msg = msg
        
    def run(self):
        print(self.msg)


class ForBlock(Block): # TODO: should inherit from unwritten loop class (I think, maybe just have it inherit nothing? Idk what I would really have it inherit but it may be useful to know that it inherits from loop)
    def __init__(self, contents: BlockCollection, block_min: int, block_max: int):
        super().__init__("loop")
        self.block_min = block_min
        self.block_max = block_max
        self.i = None
        self.contents = contents # the code blocks contained inside of this loop
    
    def run(self):
        self.i = self.block_min
    
        while(self.block_min <= self.i and self.i < self.block_max):
            self.contents.run()

            self.i += 1
            

if __name__ == "__main__":
    test_print = PrintBlock("your mama!")
    test_print_2 = PrintBlock("cheese burgers")

    test_for_block = ForBlock(BlockCollection([test_print, test_print_2]), 0, 10)

    test_for_block.run()