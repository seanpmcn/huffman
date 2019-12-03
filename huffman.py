class Tree:
    def __init__(self, char, frequency, leftTree = None, rightTree = None):
        self.char = char
        self.frequency = frequency
        self.leftTree = leftTree
        self.rightTree = rightTree
    
    def __init__(self):
        self.char = None
        self.frequency = None
        self.leftTree = None
        self.rightTree = None

    def __init__(self, frequency, leftTree, rightTree):
        self.char = None
        self.frequency = frequency
        self.leftTree = leftTree
        self.rightTree = rightTree

    def getChar(self):
        return self.char
    
    def getFrequency(self):
        return self.frequency

    def getLeftTree(self):
        return self.leftTree
    
    def getRightTree(self):
        return self.rightTree

enc = input("Enter string to be encoded: ")
freq = {}
for c in enc:
    if c in freq:
        freq.update({c : freq.get(c) + 1})
    else:
        freq.update({c : 1})
freqTree = [Tree(k, v) for k,v in freq.items()]
while(freqTree.count > 1):
    m = max
    l = Tree()
    r = Tree()
    for i in freqTree:
        if(i.getFrequency < min):
            l = i
            m = i.getFrequency
    freqTree.remove(l)
    for i in freqTree:
        if(i.getFrequency < min):
            r = i
            m = i.getFrequency
    freqTree.remove(r)
    freqTree.append(Tree(l.getFrequency+r.getFrequency, l, r))