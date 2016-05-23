class DNAAnimBuilding(DNALandmarkBuilding):
    def __init__(self, name):
        DNALandmarkBuilding.__init__(self, name)
        self.animName = ''

    def setAnim(self, anim):
        self.animName = anim

    def getAnim(self):
        return self.animName

    def traverse(self, nodePath, dnaStorage):
        node = dnaStorage.findNode(self.getCode())
        if node is None:
            raise DNAError('DNAAnimBuilding code ' + self.getCode() + ' not found in dnastore')
        node = node.copyTo(nodePath, 0)
        node.setName(self.getName())
        node.setPosHprScale(self.getPos(), self.getHpr(), self.getScale())
        node.setTag('DNAAnim', self.animName)
        self.setupSuitBuildingOrigin(nodePath, node)
        for child in self.children:
            child.traverse(nodePath, dnaStorage)
        nodePath.flattenStrong()