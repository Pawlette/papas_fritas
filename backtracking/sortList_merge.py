class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def printList(self, root, name):
        print ("Linked List Values for ", name)
        while (root != None):
            print (root.val)
            root = root.next

    def sortList(self, head):
        if(head == None or head.next == None):
            return head
        return self.split(head)

    def split(self, head):
        if(head == None or head.next == None):
            return head
        listA = nxtA = ListNode(head.val)
        head = head.next
        listB = None
        if (head != None):
            listB = nxtB = ListNode(head.val)
        while (head != None):
            head = head.next
            if(head):
                nxtA.next = ListNode(head.val)
                nxtA = nxtA.next
                head = head.next

            if(head):
                nxtB.next = ListNode(head.val)
                nxtB = nxtB.next

        orderedA = self.split(listA)
        orderedB = self.split(listB)

        return self.merge(orderedA, orderedB)
        #return None

    def merge(self, list1, list2):
        # print ("* * * Merge * * *")
        # self.printList(list1, "List 1")
        # self.printList(list2, "List 2")
        if (list1 == None):
            return list2
        elif (list2 == None):
            return list1

        if (list1.val <= list2.val):
            root = ListNode(list1.val)
            list1 = list1.next
        else:
            root = ListNode(list2.val)
            list2 = list2.next
        rootNX = root
        while(list1 != None or list2 != None):
            if (list1 == None):
                rootNX.next = list2
                return root
            elif (list2 == None):
                rootNX.next = list1
                return root
                
            if (list1.val <= list2.val):
                rootNX.next = ListNode(list1.val)
                list1 = list1.next
            else:
                rootNX.next = ListNode(list2.val)
                list2 = list2.next
            rootNX = rootNX.next
        return root

myList = ListNode(7)
nodeB = ListNode(4) 
myList.next = nodeB #
"""
nodeC = ListNode(9)
nodeB.next = nodeC  #
nodeD = ListNode(2)
nodeC.next = nodeD  #
nodeE = ListNode(3)
nodeD.next = nodeE  #
nodeF = ListNode(-3)
nodeE.next = nodeF  #
"""
mySol = Solution()
mySol.printList(myList, "List before sort")
sortedList = mySol.sortList(myList)
mySol.printList(sortedList, "Sorted List")
