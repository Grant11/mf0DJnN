class DNAFlatDoor(DNADoor):
    def traverse(self, nodePath, dnaStorage):
        node = dnaStorage.findNode(self.getCode())
        node = node.copyTo(nodePath, 0)
        node.setScale(NodePath(), (1, 1, 1))
        node.setPosHpr((0.5, 0, 0), (0, 0, 0))
        node.setColor(self.getColor())
        node.getNode(0).setEffect(DecalEffect.make())