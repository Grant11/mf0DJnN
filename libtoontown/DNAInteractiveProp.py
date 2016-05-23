class DNAInteractiveProp(DNAAnimProp):
    def __init__(self, name):
        DNAAnimProp.__init__(self, name)
        self.cellId = -1

    def setCellId(self, id):
        self.cellId = id

    def getCellId(self):
        return cellId

    def traverse(self, nodePath, dnaStorage):
        node = None
        if self.getCode() == "DCS":
            node = ModelNode(self.getName())
            node.setPreserveTransform(ModelNode.PTNet)
            node = nodePath.attachNewNode(node, 0)
        else:
            node = dnaStorage.findNode(self.getCode())
            node = node.copyTo(nodePath, 0)
            node.setName(self.getName())
        node.setTag('DNAAnim', self.getAnim())
        node.setTag('DNACellIndex', str(self.cellId))
        node.setPosHprScale(self.getPos(), self.getHpr(), self.getScale())
        node.setColorScale(self.getColor(), 0)
        for child in self.children:
            child.traverse(node, dnaStorage)