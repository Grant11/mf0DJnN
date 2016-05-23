class DNASignBaseline(DNANode):
    def __init__(self):
        DNANode.__init__(self, '')
        self.code = ''
        self.color = LVector4f(1, 1, 1, 1)
        self.font = None
        self.flags = ''
        self.indent = 0.0
        self.kern = 0.0
        self.wiggle = 0.0
        self.stumble = 0.0
        self.stomp = 0.0
        self.width = 0
        self.height = 0

    def setCode(self, code):
        self.code = code

    def setColor(self, color):
        self.color = color

    def getCode(self):
        return self.code

    def getColor(self):
        return self.color

    def getFont(self):
        return self.font

    def getHeight(self):
        return self.height

    def getIndent(self):
        return self.indent

    def getKern(self):
        return self.kern

    def getStomp(self):
        return self.stomp

    def getStumble(self):
        return self.stumble

    def getWidth(self):
        return self.width

    def getWiggle(self):
        return self.wiggle

    def setFont(self, font):
        self.font = font

    def setHeight(self, height):
        self.height = height

    def setIndent(self, indent):
        self.indent = indent

    def setKern(self, kern):
        self.kern = kern

    def setStomp(self, stomp):
        self.stomp = stomp

    def setStumble(self, stumble):
        self.stumble = stumble

    def setWidth(self, width):
        self.width = width

    def setWiggle(self, wiggle):
        self.wiggle = wiggle

    def setFlags(self, flags):
        self.flags = flags

    def getFlags(self):
        return self.flags

    def traverse(self, nodePath, dnaStorage):
        nodePath = nodePath.attachNewNode('baseline', 0)
        nodePath.setPos(self.pos)
        nodePath.setHpr(self.hpr)
        nodePath.setDepthOffset(50)

        texts = []
        for child in self.children:
            if child.__class__ == DNASignText:
                texts.append(child.letters)
            else:
                child.traverse(nodePath, dnaStorage)

        typesetter = DNATypesetter(self, dnaStorage)
        np = typesetter.generate(texts)
        if np:
            np.reparentTo(nodePath)