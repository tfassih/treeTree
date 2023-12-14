# treeTree is an open-source BST tree data structure library for python3
# 33
# Author: Thomas Fassih // github.com/tfassih // thomasfassih.com
# Initial Release: 14 DEC 2023

# BINARY SEARCH TREE #

class BSTNode:
    left, right = None, None

    def __init__(self, data):
        self.data = data

    def insert(self, data):
        if data <= self.data:
            if self.left is None:
                self.left = BSTNode(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = BSTNode(data)
            else:
                self.right.insert(data)

    def removeNode(self, val):
        if self is None:
            return self

        if val < self.data:
            self.left = self.left.removeNode(val)
        elif val > self.data:
            self.right = self.right.removeNode(val)
        else:
            if self.left is None:
                tNode = self.right
                self = None
                return tNode
            elif self.right is None:
                tNode = self.left
                self = None
                return tNode

            tNode = BSTNode.findMin(self.right)
            self.data = tNode.data
            self.right = self.right.removeNode(tNode.data)

        return self

    def clearTree(self):
        if self is not None:
            BSTNode.clearTree(self.left)
            BSTNode.clearTree(self.right)
            del self

    def printInOrder(self):
        if self.left is not None:
            self.left.printInOrder()
        print(self.data)
        if self.right is not None:
            self.right.printInOrder()

    def printPreOrder(self):
        print(self.data)
        if self.left is not None:
            self.left.printPreOrder()
        if self.right is not None:
            self.right.printPreOrder()

    def printPostOrder(self):
        if self.left is not None:
            self.left.printPostOrder()
        if self.right is not None:
            self.right.printPostOrder()
        print(self.data)

    def getInOrderList(self, temp):
        if self.left is not None:
            self.left.getInOrderList(temp)
        temp.append(self.data)
        if self.right is not None:
            self.right.getInOrderList(temp)
        return temp

    def getPreOrderList(self, temp):
        temp.append(self.data)
        if self.left is not None:
            self.left.getPreOrderList(temp)
        if self.right is not None:
            self.right.getPreOrderList(temp)
        return temp

    def getPostOrderList(self, temp):
        if self.left is not None:
            self.left.getPostOrderList(temp)
        if self.right is not None:
            self.right.getPostOrderList(temp)
        temp.append(self.data)
        return temp

    def contains(self, val):
        if self is None:
            return False
        if self.data == val:
            return True
        if val < self.data:
            return self.left.contains(val)
        if val > self.data:
            return self.right.contains(val)

    def findMin(self):
        current = self

        while current and current.left is not None:
            current = current.left

        return current

    def findMax(self):
        current = self

        while current and current.right is not None:
            current = current.right

        return current

    def getSum(self):
        if self is not None:
            return sum(self.getPreOrderList([]))
        else:
            return 0

    def countNodes(self):
        if self is None:
            return 0
        else:
            return BSTNode.countNodes(self.left) + BSTNode.countNodes(self.right) + 1

    def getHeight(self):
        if self is None:
            return 0
        else:
            lHeight = BSTNode.getHeight(self.left)
            rHeight = BSTNode.getHeight(self.right)

            if lHeight > rHeight:
                return lHeight + 1
            else:
                return rHeight + 1
        pass

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right