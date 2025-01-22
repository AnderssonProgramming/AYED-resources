
class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def getKey(self):
        return self.key

    def getValue(self):
        return self.value

    def setKey(self, new_key):
        if new_key is not None:
            self.key = new_key
        else:
            raise Exception('Key must not be None')

    def setValue(self, value):
        if value is not None:
            self.value = value
        else:
            raise Exception('Value must not be None')

    def __str__(self):
        return 'TreeNode' +  str( (self.key, self.value) )

class BinTree:
    def __init__(self, pair):
        self.root = TreeNode(pair[0], pair[1]) if pair is not None else None
        #Trees on the left
        self.left = None
        #Trees on the right
        self.right = None

    def getRoot(self):
        return self.root

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setLeft(self, leftTree):
        if isinstance(leftTree, BinTree) or isinstance(leftTree, BST) or leftTree is None:
            self.left = leftTree
        else:
            raise Exception('Left Tree must be a valid BinTree')

    def setRight(self, rightTree):
        if isinstance(rightTree, BinTree) or isinstance(rightTree, BST)  or rightTree is None:
            self.right = rightTree
        else:
            raise Exception('Right Tree must be a valid BinTree')

    def setRoot(self, new_root):
        self.root = new_root


    #Traversal-paths
    def inOrder(self):
        root, left, right = self.getRoot(), self.getLeft(), self.getRight()
        if root is not None:
            #Left Tree
            if left is not None:
                left.inOrder()
            # Root
            print(root.getValue())
            # right Tree
            if right is not None:
                right.inOrder()

    def preOrder(self):
        root, left, right = self.getRoot(), self.getLeft(), self.getRight()
        if root is not None:
            # Root
            print(root.getValue())
            # Left Tree
            if left is not None:
                left.preOrder()
            # right Tree
            if right is not None:
                right.preOrder()

    def posOrder(self):
        root, left, right = self.getRoot(), self.getLeft(), self.getRight()
        if root is not None:
            # Left Tree
            if left is not None:
                left.posOrder()
            # right Tree
            if right is not None:
                right.posOrder()
            # Root
            print(root.getValue())

    def inOrderArray(self, result):
        root, left, right = self.getRoot(), self.getLeft(), self.getRight()
        if root is not None:
            # Left Tree
            if left is not None:
                left.inOrderArray(result)
            # Root
            result.append(root.getValue())
            # right Tree
            if right is not None:
                right.inOrderArray(result)

    def preOrderArray(self, result):
            root, left, right = self.getRoot(), self.getLeft(), self.getRight()
            if root is not None:
                # Root
                result.append(root.getValue())
                # Left Tree
                if left is not None:
                    left.preOrderArray(result)
                # right Tree
                if right is not None:
                    right.preOrderArray(result)

    def posOrderArray(self, result):
        root, left, right = self.getRoot(), self.getLeft(), self.getRight()
        if root is not None:
            # Left Tree
            if left is not None:
                left.posOrderArray(result)
            # right Tree
            if right is not None:
                right.posOrderArray(result)
            # Root
            result.append(root.getValue())

    def search(self, value):
        root = self
        while root.getRoot().getValue() != value and root != None:
            if root.getRoot().getValue() > value:
                root = root.getLeft()
            else:
                root = root.getRight()

        return root

    def insert(self, value):
        root = self
        while root:
            if root.getRoot().getValue() > value:
                root, root2 = root.getLeft(), root
                if root == None:
                    root2.setLeft(BinTree((value, value)))
            else:
                root, root2 = root.getRight(), root
                if root == None:
                    root2.setRight(BinTree((value, value)))

    def minValue(self):
        root = self
        while root.getLeft():
            root = root.getLeft()
        return root.getRoot().getValue()

    def maxValue(self):
        root = self
        while root.getRight():
            root = root.getRight()
        return root.getRoot().getValue()


class BST:
    def __init__(self, value_root):
        self.balance_factor = 0
        self.tree = BinTree(value_root)

    def find(self, key):
        root, left, right = self.tree.getRoot(), self.tree.getLeft(), self.tree.getRight()
        if root is not None and root.getKey() == key:
            return root.getValue()
        elif root.getKey() < key and right is not None:
            return right.find(key)
        elif root.getKey() > key and left is not None:
            return left.find(key)
        return None

    def insert(self, pair):
        treeNode = TreeNode(pair[0], pair[1])
        self.insert_tree_node(treeNode)
        print('Inserted', pair, 'with new balance factor of', self.balance_factor)

    def insert_many(self, list):
        for e in list:
            self.insert(e)

    def insert_tree_node(self, new_tree_node):
        root, left, right = self.tree.getRoot(), self.tree.getLeft(), self.tree.getRight()
        if root is None:
            self.tree.setRoot(new_tree_node)
        else:
            key, value = new_tree_node.getKey(), new_tree_node.getValue()
            if root.getKey() <= key:
                #right
                if right is None:
                    self.tree.setRight(BST((key, value)))
                else:
                    right.insert_tree_node(new_tree_node)
                self.tree.getRight().calculate_balance_factor()
            else:
                #left
                if left is None:
                    self.tree.setLeft(BST((key, value)))
                else:
                    left.insert_tree_node(new_tree_node)
                self.tree.getLeft().calculate_balance_factor()
        self.calculate_balance_factor()

    def __str__(self):
        preOrderA, posOrderA = [], []
        self.tree.preOrderArray(preOrderA)
        self.tree.posOrderArray(posOrderA)
        return 'BST Tree\nPRE:'+str(preOrderA) + '\nPOS:'+str(posOrderA)

    def showBalanceFactors(self):
        right, left = self.tree.getRight(), self.tree.getLeft()
        print(self.tree.getRoot(), 'with balance factor :', self.balance_factor)
        if left is not None:
            left.showBalanceFactors()
        if right is not None:
            right.showBalanceFactors()


    def preOrderArray(self, arr):
        return self.tree.preOrderArray(arr)

    def posOrderArray(self, arr):
        return self.tree.posOrderArray(arr)


    def height(self):
        right, left = self.tree.getRight(), self.tree.getLeft()
        height_right = right.height() if right is not None else 0
        height_left = left.height() if left is not None else 0
        return 1 + max(height_right, height_left)

    def isBalanced(self):
        right, left = self.tree.getRight(), self.tree.getLeft()
        height_right = right.height() if right is not None else 0
        height_left = left.height() if left is not None else 0
        return abs(height_right-height_left) <= 1

    def calculate_balance_factor(self):
        right, left = self.tree.getRight(), self.tree.getLeft()
        height_right = right.height() if right is not None else 0
        height_left = left.height() if left is not None else 0
        self.balance_factor = height_right - height_left

def main():
    #6,5,7,2,5,8
    v6 = BinTree((6, 6))
    v5 = BinTree((5, 5))
    v7 = BinTree((7, 7))
    v2 = BinTree((2, 2))
    v5_2 = BinTree((5, 5))
    v8 = BinTree((8, 8))

    v5.setLeft(v2)
    v5.setRight(v5_2)
    v7.setRight(v8)
    v6.setLeft(v5)
    v6.setRight(v7)

    v6.insert(9)
    print("Min:", v6.minValue())
    print("Max:", v6.maxValue())
    """
    print('============== IN-ORDER ===========')
    v6.inOrder()
    inOrderResult = []
    v6.inOrderArray(inOrderResult)
    print(inOrderResult)

    print('============== PRE-ORDER ===========')
    v6.preOrder()
    preOrderResult = []
    v6.preOrderArray(preOrderResult)
    print(preOrderResult)

    print('============== POS-ORDER ===========')
    v6.posOrder()
    posOrderResult = []
    v6.posOrderArray(posOrderResult)
    print(posOrderResult)

    searchTree = BST(None)
    elements = [
                (15,'Alvaro'),
                (6, 'Monica'),
                (18, 'Juan'),
                (3, 'Maria'),
                (7,'Jose'),
                (17, 'Isabella'),
                (20, 'Laura'),
                (2, 'Camilo'),
                (4, 'Daniel'),
                (13, 'Juanita'),
                (9, 'Wilmer')
               ]
    for e in elements:
        searchTree.insert(e)
    print(searchTree)
    print(searchTree.find(13))

    test_AVL = BST(None)
    elements = [
        (6,6),
        (5,5),
        (7,7),
        (2,2),
        (5,5),
        (8,8)
    ]
    test_AVL.insert_many(elements)
    print('==================================== TESTING AVL PROPERTIES ===============================================')
    print(test_AVL)
    print(test_AVL.height())
    test_AVL.showBalanceFactors()"""
main()
