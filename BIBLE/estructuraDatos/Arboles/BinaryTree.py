
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

class BST:

    def __init__(self, value_root):
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
            else:
                #left
                if left is None:
                    self.tree.setLeft(BST((key, value)))
                else:
                    left.insert_tree_node(new_tree_node)

    def __str__(self):
        preOrderA, posOrderA = [], []
        self.tree.preOrderArray(preOrderA)
        self.tree.posOrderArray(posOrderA)
        return 'BST Tree\nPRE:'+str(preOrderA) + '\nPOS:'+str(posOrderA)

    def preOrderArray(self, arr):
        return self.tree.preOrderArray(arr)

    def posOrderArray(self, arr):
        return self.tree.posOrderArray(arr)

def main():
    #6,5,7,2,5,8
    v6 = BinTree((6, 6))
    v5 = BinTree((5, 5))
    v7 = BinTree((7, 7))
    v2 = BinTree((2,2))
    v5_2 = BinTree((5,5))
    v8 = BinTree((8,8))

    v5.setLeft(v2)
    v5.setRight(v5_2)
    v7.setRight(v8)
    v6.setLeft(v5)
    v6.setRight(v7)

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
main()