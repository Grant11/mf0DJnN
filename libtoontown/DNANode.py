class DNANode(DNAGroup):
    def __init__(self, name):
        DNAGroup.__init__(self, name)
        self.pos = LVector3f()
        self.hpr = LVector3f()
        self.scale = LVector3f(1, 1, 1)

    def getPos(self):
        return self.pos

    def getHpr(self):
        return self.hpr

    def getScale(self):
        return self.scale

    def setPos(self, pos):
        self.pos = pos

    def setHpr(self, hpr):
        self.hpr = hpr

    def setScale(self, scale):
        self.scale = scale

    def traverse(self, nodePath, dnaStorage):
        node = PandaNode(self.name)
        node = nodePath.attachNewNode(node, 0)
        node.setPosHprScale(self.pos, self.hpr, self.scale)
        for child in self.children:
            child.traverse(node, dnaStorage)