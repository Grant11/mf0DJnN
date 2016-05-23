class DNALandmarkBuilding(DNANode):
    def __init__(self, name):
        DNANode.__init__(self, name)
        self.code = ''
        self.wallColor = LVector4f(1, 1, 1, 1)
        self.title = ''
        self.article = ''
        self.buildingType = ''
        self.door = None

    def getArticle(self):
        return self.article

    def getBuildingType(self):
        return self.buildingType

    def getTitle(self):
        return self.title

    def setCode(self, code):
        self.code = code

    def setWallColor(self, color):
        self.wallColor = color

    def getCode(self):
        return self.code

    def getWallColor(self):
        return self.wallColor

    def setArticle(self, article):
        self.article = article

    def setBuildingType(self, buildingType):
        self.buildingType = buildingType

    def setTitle(self, title):
        self.title = title

    def setupSuitBuildingOrigin(self, nodePathA, nodePathB):
        if (self.getName()[:2] == 'tb') and (self.getName()[3].isdigit()) and (self.getName().find(':') != -1):
            name = self.getName()
            name = 's' + name[1:]
            node = nodePathB.find('**/*suit_building_origin')
            if node.isEmpty():
                print 'DNALandmarkBuilding ' + name + ' did not find **/*suit_building_origin'
                node = nodePathA.attachNewNode(name)
                node.setPosHprScale(self.getPos(), self.getHpr(), self.getScale())
            else:
                node.wrtReparentTo(nodePathA, 0)
                node.setName(name)

    def traverse(self, nodePath, dnaStorage):
        node = dnaStorage.findNode(self.code)
        if node is None:
            raise DNAError('DNALandmarkBuilding code ' + self.code + ' not found in DNAStorage')
        npA = nodePath
        nodePath = node.copyTo(nodePath, 0)
        nodePath.setName(self.getName())
        nodePath.setPosHprScale(self.getPos(), self.getHpr(), self.getScale())
        self.setupSuitBuildingOrigin(npA, nodePath)
        for child in self.children:
            child.traverse(nodePath, dnaStorage)
        nodePath.flattenStrong()