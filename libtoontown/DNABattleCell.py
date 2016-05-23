class DNABattleCell:
    def __init__(self, width, height, pos):
        self.width = width
        self.height = height
        self.pos = pos

    def __str__(self):
        return 'DNABattleCell width: ' + str(self.width) + ' height: ' + str(self.height) + ' pos: ' + str(self.pos)

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getPos(self):
        return self.pos

    def setWidthHeight(self, width, height):
        self.width = width
        self.height = height