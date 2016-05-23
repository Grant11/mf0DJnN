class DNASignText(DNANode):
    def __init__(self):
        DNANode.__init__(self, '')
        self.letters = ''

    def setLetters(self, letters):
        self.letters = letters

    def traverse(self, nodePath, dnaStorage):
        return