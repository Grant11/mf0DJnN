class DNASignGraphic(DNANode):
    def __init__(self, name):
        DNANode.__init__(self, name)
        self.code = ''
        self.color = LVector4f(1, 1, 1, 1)
        self.width = 0
        self.height = 0
        self.bDefaultColor = True

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getCode(self):
        return self.code

    def getColor(self):
        return self.Color

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height

    def setCode(self, code):
        self.code = code

    def setColor(self, color):
        self.color = color
        self.bDefaultColor = False

    def traverse(self, nodePath, dnaStorage):
        nodePath.getTop().getNode(0).setEffect(DecalEffect.make())
        node = dnaStorage.findNode(self.code)
        if node is None:
            raise DNAError('DNASignGraphic code ' + self.code + ' not found in storage')
        node = node.copyTo(nodePath, 0)
        node.setScale(self.scale)
        node.setScale(node, self.getParent().scale)
        node.setPosHpr(self.pos, self.hpr)
        for child in self.children:
            child.traverse(node, dnaStorage)