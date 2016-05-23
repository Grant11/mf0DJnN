class DNACornice(DNAGroup):
    def __init__(self, name):
        DNAGroup.__init__(self, name)
        self.setCode('')
        self.setColor(LVector4f(1, 1, 1, 1))

    def setCode(self, code):
        self.code = code

    def setColor(self, color):
        self.color = color

    def getCode(self):
        return self.code

    def getColor(self):
        return self.color

    def traverse(self, nodePath, dnaStorage):
        pParentXScale = nodePath.getParent().getScale().getX()
        parentZScale = nodePath.getScale().getZ()
        node = dnaStorage.findNode(self.getCode())
        if node is None:
            raise DNAError('DNACornice code {0} not found in '
                           'DNAStorage'.format(self.getCode()))
        nodePathA = nodePath.attachNewNode('cornice-internal', 0)
        node = node.find('**/*_d')
        np = node.copyTo(nodePathA, 0)
        np.setPosHprScale(
            LVector3f(0, 0, 0),
            LVector3f(0, 0, 0),
            LVector3f(1, pParentXScale/parentZScale,
                      pParentXScale/parentZScale))
        np.setEffect(DecalEffect.make())
        node = node.getParent().find('**/*_nd')
        np = node.copyTo(nodePathA, 1)
        np.setPosHprScale(
            LVector3f(0, 0, 0),
            LVector3f(0, 0, 0),
            LVector3f(1, pParentXScale/parentZScale,
                      pParentXScale/parentZScale))
        nodePathA.setPosHprScale(
            LVector3f(0, 0, node.getScale().getZ()),
            LVector3f(0, 0, 0),
            LVector3f(1, 1, 1))
        nodePathA.setColor(self.getColor())