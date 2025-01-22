class BinaryTree:
    def __init__(self, root = None):
        self.root = root
        self.left = None
        self.right = None
        self.parent = None

    #Getter
    def __str__(self):
        result = "T("+str(self.root)+")"
        if self.left:
            result += ("-left->["+ str(self.left)+"]")
        if self.right:
            result += ("-right->["+ str(self.right)+"]")
        return result

    def getRoot(self):
        return self.root

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    #Setters
    def _setParent(self, parent):
        if isinstance(parent, BinaryTree):
            self.parent = parent

    def _setRoot(self, root):
        self.root = root

    def _setRight(self, right):
        if isinstance(right, BinaryTree):
            self.right = right
            right._setParent(self)

    def _setLeft(self, left):
        if isinstance(left, BinaryTree):
            self.left = left
            left._setParent(self)

    def printRoot(self):
        print(self.root)

    def inOrder(self):
        if self.left:
            self.left.inOrder()
        self.printRoot()
        if self.right:
            self.right.inOrder()

    def preOrder(self):
        self.printRoot()
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()

    def posOrder(self):
        if self.left:
            self.left.posOrder()
        if self.right:
            self.right.posOrder()
        self.printRoot()

    def search(self, value):
        if value > self.root:
            if self.right:
                return self.right.search(value)
        elif value < self.root:
            if self.left:
                return self.left.search(value)
        return self if self.root == value else None

    def insertMany(self, values):
        for e in values:
            self.insert(e)

    def getMax(self):
        currentNode = self
        while currentNode.getRight():
            currentNode = currentNode.getRight()
        return currentNode

    def getMin(self):
        currentNode = self
        while currentNode.getLeft():
            currentNode = currentNode.getLeft()
        return currentNode

    def getHeight(self):
        heightRight = self.right.getHeight() if self.right else 0
        heightLeft = self.left.getHeight() if self.left else 0
        finalHeight = max(heightRight, heightLeft) + 1
        return finalHeight

    def isBalanced(self):
        heightRight = self.right.getHeight() if self.right else 0
        heightLeft = self.left.getHeight() if self.left else 0
        isbalanced = abs(heightLeft-heightRight) <= 1
        isBalancedRight = ( not self.right ) or self.right.isBalanced()
        isBalancedLeft = ( not self.left ) or self.left.isBalanced()
        return isbalanced \
               and isBalancedRight \
               and isBalancedLeft

    def getOrderedLeafs(self):
        return self._getInOrderLeafs([])

    def _getInOrderLeafs(self, arr):
        if self.left:
            self.left._getInOrderLeafs(arr)
        arr.append(self.root)
        if self.right:
            self.right._getInOrderLeafs(arr)
        return arr

    def _balanceTree(self, low, high, orderedLeafs):
        if low > high:
            return None
        mid = low + abs(high - low)//2
        newRoot = BinaryTree(orderedLeafs[mid])
        newRoot.left = self._balanceTree(low, mid-1, orderedLeafs)
        newRoot.right = self._balanceTree(mid+1, high, orderedLeafs)
        return newRoot

    def balanceTree(self):
        orderedLeafs = self.getOrderedLeafs()
        return self._balanceTree(0, len(orderedLeafs)-1, orderedLeafs)

    def insert(self, value):
        if self.root is None :
            self._setRoot(value)
        else:
            if value >= self.root:
                if self.right:
                    self.right.insert(value)
                else:
                    self._setRight(BinaryTree(value))
            else:
                if self.left:
                    self.left.insert(value)
                else:
                    self._setLeft(BinaryTree(value))





main()
