# coding:utf-8
# _*_coding:utf-8_*_
__author__ = 'Lenny'

#       A
#   B       C
#D    E    F
#以下代码模拟这样的二叉树


class BinaryTreeNode(object):
    def __init__(self,data,left,right):
        self.left = left
        self.right = right
        self.data = data


class BinaryTree(object):

    def __init__(self, root=None):
        self.root = root

    def is_empty(self):
        return self.root == None

    def preOrder(self,binaryNode):#先打印根结点，再打印左结点，后打印右结点
        if binaryNode == None:
            return
        print(binaryNode.data)
        self.preOrder(binaryNode.left)
        self.preOrder(binaryNode.right)

    def midOrder(self,binaryNode):# 先打印左结点，再打印根结点，后打印右结点
        if binaryNode == None:
            return
        self.midOrder(binaryNode.left)
        print(binaryNode.data)
        self.midOrder(binaryNode.right)

    def postOrder(self,binaryNode):# 先打印左结点，再打印右结点，后打印根结点
        if binaryNode == None:
            return
        self.postOrder(binaryNode.left)
        self.postOrder(binaryNode.right)
        print(binaryNode.data)


n1 = BinaryTreeNode(data="D",left=None,right=None)
n2 = BinaryTreeNode(data="E",left=None,right=None)
n3 = BinaryTreeNode(data="F",left=None,right=None)
n4 = BinaryTreeNode(data="B", left=n1, right=n2)
n5 = BinaryTreeNode(data="C", left=n3, right=None)
root = BinaryTreeNode(data="A", left=n4, right=n5)

bt = BinaryTree(root)
print("先序遍历")
bt.preOrder(bt.root)
print("中序遍历")
bt.midOrder(bt.root)
print("后序遍历")
bt.postOrder(bt.root)