
# coding:utf-8
# _*_coding:utf-8_*_
__author__ = 'Lenny'

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def get(self, index):
        i = 0
        node = self.next
        while (node and i <= index):
            if i == index:
                return node.val
            else:
                node = node.next
                i = i + 1
        return -1

    def addAtHead(self, val):
        anext = self.next
        head = ListNode(val)
        head.next = anext
        self.next = head

    def addAtTail(self, val):
        tail = ListNode(val)
        pre = self.next
        if pre == None:
            self.next = tail
        else:
            while (pre.next):
                pre = pre.next
            pre.next = tail

    def addAtIndex(self, index, val):

        if index == 0:
            self.addAtHead(val)
            return

        node = ListNode(val)
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

    def printSelf(self):
        linkedList = self
        while(linkedList != None):
            print(linkedList.val)
            linkedList = linkedList.next
        print('end print')


class Solution:
    def addTwoNumbers(self, l1, l2):
        num1  = self.aNumber(l1)
        num2 = self.aNumber(l2)
        towSum = num1 + num2
        L = self.creatLinkedList(towSum)
        return L
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

    def aNumber(self,l1):
        node = l1.next
        num = 0
        if node == None:
            return
        n = 1
        while(node):
            num = node.val * n  + num
            n = n * 10
            node = node.next
        return num

    def creatLinkedList(self, N):

        if N == 0:
            return ListNode(N)
        num = N
        L = None
        nextNode = L
        while (num > 0):
            n = num % 10
            num = num // 10
            node = ListNode(n)
            if L == None:
                L = node
                nextNode = L
            else:
                nextNode.next = node
                nextNode = nextNode.next
        return L

    def add_two_numbers(self, l1, l2):
        tmp_carry = 0
        tmp_sol = None
        head_sol = None

        while l1 != None or l2 != None or tmp_carry>0:
            tmp_sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + tmp_carry
            tmp_carry = tmp_sum//10#(tmp_sum - tmp_sum%10)/10
            new_val = tmp_sum%10
            if tmp_sol:
                tmp_sol.next = ListNode(new_val)
                tmp_sol = tmp_sol.next
            else:
                tmp_sol = ListNode(new_val)
                head_sol = tmp_sol
            l1 = l1.next if l1!=None else None
            l2 = l2.next if l2!=None else None
        return head_sol

    def addTwoNumbers2(self, l1, l2):

        if l1 == None:
            return l2

        if l2 == None:
            return l1

        sval = l1.val + l2.val
        if sval < 10:
            ansNode = ListNode(sval)
            ansNode.next = self.addTwoNumbers(l1, l2)
            return ansNode
        else:
            rval = l1.val + l2.val - 10
            ansNode = ListNode(rval)
            ansNode.next = self.addTwoNumbers(ListNode(1), self.addTwoNumbers(l1, l2))
            return ansNode



linkedList1 = ListNode(2)
linkedList1.addAtHead(2)
linkedList1.addAtHead(4)
linkedList1.addAtHead(3)
# linkedList1.addAtIndex(3, 1)  #1>2>7>0
# linkedList1.printSelf()
# linkedList.deleteAtIndex(2)  #1>2>0
# linkedList.addAtHead(6)      #6>1>2>0
# linkedList.addAtTail(4)      #6>1>2>0>4
# linkedList1.printSelf()

linkedList2 = ListNode(0)
linkedList2.addAtHead(5)
linkedList2.addAtHead(6)
linkedList2.addAtHead(4)
# linkedList2.addAtIndex(3, 0)  #1>2>7>0
# linkedList2.printSelf()

solution = Solution()
# solution.aNumber(linkedList)
# linkedList = solution.addTwoNumbers(linkedList1,linkedList2)
# linkedList = solution.add_two_numbers(linkedList1,linkedList2)
linkedList = solution.addTwoNumbers2(linkedList1,linkedList2)
linkedList.printSelf()
