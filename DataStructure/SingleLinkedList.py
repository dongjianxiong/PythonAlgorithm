# coding:utf-8
# _*_coding:utf-8_*_
__author__ = 'Lenny'

class MyLinkedList:

    def __init__(self):
        self.next = None
        self.data = 0
        """
        Initialize your data structure here.
        """

    def get(self, index):
        i = 0
        node = self.next
        while (node and i <= index):
            if i == index:
                return node.data
            else:
                node = node.next
                i = i + 1
        return -1
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """

    def addAtHead(self, val):
        anext = self.next
        head = MyLinkedList()
        head.data = val
        head.next = anext
        self.next = head
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """

    def addAtTail(self, val):
        tail = MyLinkedList()
        tail.data = val
        tail.next = None
        pre = self.next
        if pre == None:
            self.next = tail
        else:
            while (pre.next):
                pre = pre.next
            pre.next = tail

        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """

    def addAtIndex(self, index, val):

        if index == 0:
            self.addAtHead(val)
            return

        node = MyLinkedList()
        node.data = val
        node.next = None

        currentNode = self.next
        i = 0
        while (currentNode and i <= index-1):
            if i == index - 1:
                node.next = currentNode.next
                currentNode.next = node
                break
            else:
                i = i + 1
                currentNode = currentNode.next
        if i != index - 1:
            print("invalid index")


        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """

    def deleteAtIndex(self, index):
        currentNode = self.next
        if index == 0:
            self.next = currentNode.next
            return
        i = 0
        while (currentNode and i <= index-1):
            if i == index - 1:
                anext = currentNode.next
                currentNode.next = anext.next
                return
            i = i + 1
            currentNode = currentNode.next
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
    def printSelf(self):
        linkedList = self.next
        while(linkedList != None):
            print(linkedList.data)
            linkedList = linkedList.next
        print('end print')

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


# linkedList = MyLinkedList()
# linkedList.addAtHead(7)
# linkedList.addAtHead(2)
# linkedList.addAtHead(1)
# linkedList.addAtIndex(3, 0)  #1>2>7>0
# # linkedList.printSelf()
# linkedList.deleteAtIndex(2)  #1>2>0
# linkedList.addAtHead(6)      #6>1>2>0
# linkedList.addAtTail(4)      #6>1>2>0>4
# # print(linkedList.get(4))     #4
# linkedList.addAtHead(4)      #4>6>1>2>0>4
# linkedList.addAtIndex(5, 0)  #4>6>1>2>0>0>4
# linkedList.addAtHead(6)      #6>4>6>1>2>0>0>4
# linkedList.printSelf()

# # linkedList.printSelf()
# linkedList.addAtTail(3)
# # linkedList.printSelf()
# linkedList.addAtIndex(1, 2)    # linked list becomes 1->2->3
# linkedList.printSelf()
# linkedList.get(1)              # returns 2
# # print(linkedList.get(1))
# # linkedList.printSelf()
# linkedList.deleteAtIndex(1)    # now the linked list is 1->3
# linkedList.printSelf()
# linkedList.get(1)              # returns 3
# print(linkedList.get(2))
# # linkedList.printSelf()

