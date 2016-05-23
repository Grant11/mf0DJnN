class DNASign(DNANode):
    def __init__(self):
        DNANode.__init__(self, '')
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
        decNode = nodePath.find('**/sign_decal')
        if decNode.isEmpty():
            decNode = nodePath.find('**/*_front')
        if decNode.isEmpty() or not decNode.getNode(0).isGeomNode():
            decNode = nodePath.find('**/+GeomNode')
        node = None
        if self.code != '':
            node = dnaStorage.findNode(self.code)
            node = node.copyTo(decNode, 0)
            node.setName('sign')
        else:
            node = ModelNode('sign')
            node = decNode.attachNewNode(node, 0)
        #node.getNode(0).setEffect(DecalEffect.make())
        node.setDepthOffset(50)
        origin = nodePath.find('**/*sign_origin')
        node.setPosHprScale(origin, self.pos, self.hpr, self.scale)
        for child in self.children:
            child.traverse(node, dnaStorage)
        node.flattenStrong()