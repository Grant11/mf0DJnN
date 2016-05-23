class DNAWall(DNANode):
    def __init__(self, name):
        DNANode.__init__(self, name)
        self.code = ''
        self.height = 10
        self.color = LVector4f(1, 1, 1, 1)

    def getCode(self):
        return self.code

    def getColor(self):
        return self.color

    def getHeight(self):
        return self.height

    def setCode(self, code):
        self.code = code

    def setColor(self, color):
        self.color = color

    def setHeight(self, height):
        self.height = height

    def traverse(self, nodePath, dnaStorage):
        node = dnaStorage.findNode(self.code)
        if node is None:
            raise DNAError('DNAWall code ' + self.code + ' not found in DNAStorage')
        node = node.copyTo(nodePath, 0)
        self.pos.setZ(DNAFlatBuilding.currentWallHeight)
        self.scale.setZ(self.height)
        node.setPosHprScale(self.pos, self.hpr, self.scale)
        node.setColor(self.color)
        for child in self.children:
            child.traverse(node, dnaStorage)
        DNAFlatBuilding.currentWallHeight += self.height