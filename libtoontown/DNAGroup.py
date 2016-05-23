class DNAGroup:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None
        self.visGroup = None

    def add(self, child):
        self.children += [child]

    def at(self, index):
        return self.children[index]

    def clearParent(self):
        self.parent = None
        self.visGroup = None

    def getVisGroup(self):
        return self.visGroup

    def getNumChildren(self):
        return len(self.children)

    def getParent(self):
        return self.parent

    def remove(self, child):
        self.children.remove(child)

    def setParent(self, parent):
        self.parent = parent
        self.visGroup = parent.getVisGroup()

    def getName(self):
        return self.name

    def traverse(self, nodePath, dnaStorage):
        node = PandaNode(self.name)
        nodePath = nodePath.attachNewNode(node, 0)
        for child in self.children:
            child.traverse(nodePath, dnaStorage)