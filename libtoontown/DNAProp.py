class DNAProp(DNANode):
    def __init__(self, name):
        DNANode.__init__(self, name)
        self.code = ''
        self.color = LVector4f(1, 1, 1, 1)

    def setCode(self, code):
        self.code = code

    def setColor(self, color):
        self.color = color

    def getCode(self):
        return self.code

    def getColor(self):
        return self.color

    def traverse(self, nodePath, dnaStorage):
        if self.code == 'DCS':
            node = ModelNode(self.name)
            node.setPreserveTransform(ModelNode.PTNet)
            node = nodePath.attachNewNode(node)
        else:
            node = dnaStorage.findNode(self.code)
            if node is None:
                return
            node = node.copyTo(nodePath, 0)
        node.setPosHprScale(self.pos, self.hpr, self.scale)
        node.setName(self.name)
        node.setColorScale(self.color, 0)
        for child in self.children:
            child.traverse(node, dnaStorage)