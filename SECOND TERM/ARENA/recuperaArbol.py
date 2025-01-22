from sys import stdin
class BinaryTree:
    def __init__(self, elements=[]):
        if len(elements) > 0:
            self.initialize(elements[0])
            self.avl = 0
            for e in elements[1:]:
                self.insert(e)
        else:
            self.initialize()

    def __len__(self):
        if self.isEmpty ():
            return 1
        else:
            left, right = self.getLeft (), self.getRight ()
            leftSize = len (left) if left is not None else 0
            rightSize = len (right) if right is not None else 0
            return 1 + leftSize + rightSize

    def isEmpty(self):
        return self.getRoot () is None and \
                self.isLeaf () and \
                self.getParent () is None

    def initialize(self, value=None):
        self.setLeft ()
        self.setRight ()
        self.setParent ()
        self.setRoot (value)
        self.setHeight ()
        self.setAVL ()

    def setRight(self, newValue=None):
        if isinstance (newValue, BinaryTree) or newValue is None:
            self.right = newValue
            if self.right is not None:
                self.right.setParent (self)

    def setLeft(self, newValue=None):
        if isinstance (newValue, BinaryTree) or newValue is None:
            self.left = newValue
            if self.left is not None:
                self.left.setParent (self)

    def setParent(self, newValue=None):
        if isinstance (newValue, BinaryTree) or newValue is None:
            self.parent = newValue

    def setRoot(self, newValue=None):
        self.root = newValue

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    def getRoot(self):
        return self.root

    def getParent(self):
        return self.parent

    def isLeaf(self):
        return self.left is None and self.right is None

    def setAVL(self):
        if self.isEmpty ():
            self.avl = 0
        else:
            left, right = self.getLeft (), self.getRight ()
            left_height = (0 if not left else left.getHeight ())
            right_height = (0 if not right else right.getHeight ())
            self.avl = right_height - left_height

    def isBalanced(self):
        return abs (self.avl) <= 1

    def insertMany(self, elements=[]):
        for e in elements:
            self.insert (e)

    def insert(self, v):
        if not self.getRoot ():
            self.setRoot (v)
        else:
            directionLeft = (v < self.getRoot ())
            toInsert = self.getLeft () if directionLeft else self.getRight ()
            if toInsert is None:
                newLeaf = BinaryTree ([v])
                if directionLeft:
                    self.setLeft(newLeaf)
                else:
                    self.setRight(newLeaf)
            else:
                toInsert.insert(v)
        self.setHeight()
        self.setAVL()
        #Detect Unbalance
        if self.isBalanced():
            self.balance()

    def rotateLeft(self):
        s, left, right = self.getRoot (), self.getLeft (), self.getRight ()
        r, rl = right.getRoot (), right.getLeft ()
        self.setRoot (r)
        self.setRight (right.getRight ())
        self.setLeft (BinaryTree ([s]))
        self.getLeft ().setLeft (left)
        self.getLeft ().setRight (rl)
        self.setHeight ()
        self.setAVL ()

    def rotateLeftRight(self):
        s, right = self.getRoot (), self.getRight ()
        r, lv = right.getRoot (), right.getLeft ().getRoot ()
        rr, lvl, lvr = right.getRight (), right.getLeft ().getLeft (), right.getLeft ().getRight ()
        right.setRoot (lv)
        right.setLeft (lvl)
        right.setRight (BinaryTree ([r]))
        right.getRight ().setLeft (lvr)
        right.getRight ().setRight (rr)
        self.rotateLeft ()

    def rotateRightLeft(self):
        s, left = self.getRoot (), self.getLeft ()
        l, lv = left.getRoot (), left.getRight ().getRoot ()
        ll, lvl, lvr = left.getLeft (), left.getRight ().getLeft (), left.getRight ().getRight ()
        left.setRoot (lv)
        left.setRight (lvr)
        left.setLeft (BinaryTree ([l]))
        left.getLeft ().setLeft (ll)
        left.getLeft ().setRight (lvl)
        self.rotateRight ()

    def rotateRight(self):
        s, left, right = self.getRoot (), self.getLeft (), self.getRight ()
        l, lr = left.getRoot (), left.getRight ()
        self.setRoot (l)
        self.setLeft (left.getLeft ())
        self.setRight (BinaryTree ([s]))
        self.getRight ().setLeft (lr)
        self.getRight ().setRight (right)
        self.setHeight ()
        self.setAVL ()

    def balance(self):
        if self.avl > 1 and self.right.avl >= 1 :
            self.rotateLeft()
        if self.avl > 1 and self.right.avl <= -1 :
            self.rotateLeftRight()
        if self.avl < -1 and self.left.avl <= -1 :
            self.rotateRight()
        if self.avl < -1 and self.left.avl >= 1:
            self.rotateRightLeft()
        self.setHeight()
        self.setAVL()

    def preOrder(self, buffer=[]):
        buffer.append(self.getRoot())
        left, right = self.getLeft(), self.getRight()
        if left is not None:
            left.preOrder(buffer)
        if right is not None:
            right.preOrder(buffer)

    def inOrder(self, buffer=[]):
        left, right = self.getLeft (), self.getRight ()
        if left is not None:
            left.inOrder (buffer)
        buffer.append (self.getRoot ())
        if right is not None:
            right.inOrder (buffer)

    def posOrder(self, buffer=[]):
        left, right = self.getLeft (), self.getRight ()
        if left is not None:
            left.posOrder (buffer)
        if right is not None:
            right.posOrder (buffer)
        buffer.append (self.getRoot ())

    def search(self, v, hops=0):
        if v == self.getRoot ():
            return (self, hops + 1)
        else:
            toSearch = self.getLeft () if (v < self.getRoot ()) else self.getRight ()
            return toSearch.search (v, hops + 1) if toSearch else (None, hops + 1)

    def setHeight(self):
        left, right = self.getLeft (), self.getRight ()
        if left:
            left.setHeight ()
        if right:
            right.setHeight ()
        left_height = (0 if not left else left.getHeight ())
        right_height = (0 if not right else right.getHeight ())
        self.height = 1 + max (left_height, right_height)

    def getHeight(self):
        return self.height

    def getAVLFactor(self):
        return self.avl

    def getMaximum(self):
        result = self

        while result.right is not None:
            result = result.getRight ()
        return result

    def getMinimum(self):
        result = self
        while result.left is not None:
            result = result.getLeft ()
        return result

    def detectAndBalance(self):
        self.setHeight ()
        self.setAVL ()
        if abs(self.avl) > 1:
            self.balance()

    def delete(self, search):
        return self

    def update(self, old, new):
        self.delete (old)
        self.insert (new)

    def __str__(self):
        buffer = []
        self.preOrder (buffer)
        bufferIn = []
        self.inOrder (bufferIn)
        return "Tree(" + str (buffer) + ', ' + str (bufferIn) + ")"

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None
    root_value = preorder[0]  # El primer valor en el recorrido en preorden es el valor de la raíz
    root = Node(root_value)  # Creamos un nodo con el valor de la raíz
    root_index = inorder.index(root_value)  # Encontramos la posición de la raíz en el recorrido inorden
    # Construimos los subárboles izquierdo y derecho recursivamente
    root.left = build_tree(preorder[1:root_index + 1], inorder[:root_index])
    root.right = build_tree(preorder[root_index + 1:], inorder[root_index + 1:])
    return root


def postorder_traversal(root, result):
    if root:
        # Realiza un recorrido en postorden recursivamente: primero el subárbol izquierdo, luego el subárbol derecho, y finalmente el nodo raíz
        postorder_traversal(root.left, result)
        postorder_traversal(root.right, result)
        result.append(root.value)  # Agrega el valor del nodo al resultado


def recupera_el_arbol(preorder, inorder):
    # Construye el árbol binario a partir de los recorridos en preorden e inorden
    root = build_tree(preorder, inorder)
    result = []  # Lista para almacenar el recorrido en postorden
    # Realiza el recorrido en postorden del árbol y guarda los valores en 'result'
    postorder_traversal(root, result)
    return ''.join(result)  # Devuelve el recorrido en postorden como una cadena


def main():
    for line in stdin:
        preorder, inorder = line.split()
        postorder = recupera_el_arbol(preorder, inorder)
        print(postorder)

if __name__ == "__main__":
    main()

