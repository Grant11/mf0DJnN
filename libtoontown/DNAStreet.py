class DNAStreet(DNANode):
    def __init__(self, name):
        DNANode.__init__(self, name)
        self.code = ''
        self.streetTexture = ''
        self.sideWalkTexture = ''
        self.curbTexture = ''
        self.streetColor = LVector4f(1, 1, 1, 1)
        self.sidewalkColor = LVector4f(1, 1, 1, 1)
        self.curbColor = LVector4f(1, 1, 1, 1)
        self.setTexCnt = 0
        self.setColCnt = 0

    def setCode(self, code):
        self.code = code

    def getCode(self):
        return self.code

    def getStreetTexture(self):
        return self.streetTexture

    def getSidewalkTexture(self):
        return self.sidewalkTexture

    def getCurbTexture(self):
        return self.curbTexture

    def getStreetColor(self):
        return self.streetColor

    def getSidewalkColor(self):
        return self.sidewalkColor

    def getCurbColor(self):
        return self.curbColor

    def setStreetTexture(self, texture):
        self.streetTexture = texture

    def setSidewalkTexture(self, texture):
        self.sidewalkTexture = texture

    def setCurbTexture(self, texture):
        self.curbTexture = texture

    def setStreetColor(self, color):
        self.streetColor = color

    def setSidewalkColor(self, color):
        self.SidewalkColor = color

    def setTextureColor(self, color):
        self.Color = color

    def setTexture(self, texture):
        if self.setTexCnt == 0:
            self.streetTexture = texture
        if self.setTexCnt == 1:
            self.sidewalkTexture = texture
        if self.setTexCnt == 2:
            self.curbTexture = texture
        self.setTexCnt += 1

    def setColor(self, color):
        if self.setColCnt == 0:
            self.streetColor = color
        if self.setColCnt == 1:
            self.sidewalkColor = color
        if self.setColCnt == 2:
            self.curbColor = color
        self.setColCnt += 1

    def traverse(self, nodePath, dnaStorage):
        node = dnaStorage.findNode(self.code)
        if node is None:
            raise DNAError('DNAStreet code ' + self.code + ' not found in DNAStorage')
        nodePath = node.copyTo(nodePath, 0)
        node.setName(self.getName())
        streetTexture = dnaStorage.findTexture(self.streetTexture)
        sidewalkTexture = dnaStorage.findTexture(self.sidewalkTexture)
        curbTexture = dnaStorage.findTexture(self.curbTexture)
        if streetTexture is None:
            raise DNAError('street texture not found in DNAStorage : ' + self.streetTexture)
        if sidewalkTexture is None:
            raise DNAError('sidewalk texture not found in DNAStorage : ' + self.sidewalkTexture)
        if curbTexture is None:
            raise DNAError('curb texture not found in DNAStorage : ' + self.curbTexture)
        streetNode = nodePath.find('**/*_street')
        sidewalkNode = nodePath.find('**/*_sidewalk')
        curbNode = nodePath.find('**/*_curb')

        if not streetNode.isEmpty():
            streetNode.setTexture(streetTexture, 1)
            streetNode.setColorScale(self.streetColor, 0)
        if not sidewalkNode.isEmpty():
            sidewalkNode.setTexture(sidewalkTexture, 1)
            sidewalkNode.setColorScale(self.sidewalkColor, 0)
        if not curbNode.isEmpty():
            curbNode.setTexture(curbTexture, 1)
            curbNode.setColorScale(self.curbColor, 0)

        nodePath.setPosHprScale(self.getPos(), self.getHpr(), self.getScale())

