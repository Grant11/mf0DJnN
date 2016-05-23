class DNAVisGroup(DNAGroup):
    def __init__(self, name):
        DNAGroup.__init__(self,name)
        self.visibles = []
        self.suitEdges = []
        self.battleCells = []

    def getVisGroup(self):
        return self

    def addBattleCell(self, battleCell):
        self.battleCells.append(battleCell)

    def addSuitEdge(self, suitEdge):
        self.suitEdges.append(suitEdge)

    def addVisible(self, visible):
        self.visibles.append(visible)

    def getBattleCell(self, i):
        return self.battleCells[i]

    def getNumBattleCells(self):
        return len(self.battleCells)

    def getNumSuitEdges(self):
        return len(self.suitEdges)

    def getNumVisibles(self):
        return len(self.visibles)

    def getSuitEdge(self, i):
        return self.suitEdges[i]

    def getVisibleName(self, i):
        return self.visibles[i]

    def removeBattleCell(self, cell):
        self.battleCells.remove(cell)

    def removeSuitEdge(self, edge):
        self.suitEdges.remove(edge)

    def removeVisible(self, visible):
        self.visibles.remove(visible)

    def traverse(self, nodePath, dnaStorage):
        DNAGroup.traverse(self, nodePath, dnaStorage)