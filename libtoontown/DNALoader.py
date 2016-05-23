class DNALoader:
    def __init__(self):
        node = PandaNode('dna')
        self.nodePath = NodePath(node)
        self.data = DNAData("loader_data")

    def buildGraph(self):
        self.data.traverse(self.nodePath, self.data.getDnaStorage())
        if self.nodePath.getChild(0).getNumChildren() == 0:
            return None
        return self.nodePath.getChild(0).getChild(0)

    def getData(self):
        return self.data