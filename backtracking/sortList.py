class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def printList(root, name):
    print "LinkedList values for", name
    while(root != None):
        print root.val
        root = root.next

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head == None or (head and head.next == None)):
            return head

        HD = HF = TL = ListNode(head.val)
        head = head.next
        listSize = 1

        while(head != None):
            value = head.val

            if (value <= HD.val): #Insert First to Left, update HD
                tmp = HD
                HD = ListNode(value)
                HD.next = tmp
            elif (value >= TL.val): #Inser Last to Right, update TL
                TL.next = ListNode(value)
                TL = TL.next
            elif (value == HF.val): #Insert to Right, update HF
                new = ListNode(value)
                new.next = HF.next
                HF.next = new
                HF = HF.next
            elif (value < HF.val): #Navigate from HD until finding a place
                nxt = HD
                while (nxt.next != None):
                    if (value < nxt.next.val):
                        newNode = ListNode(value)
                        newNode.next = nxt.next
                        nxt.next = newNode
                        break
                    nxt = nxt.next
            elif (value > HF.val): #Navigate from HF until finding a place
                nxt = HF
                while (nxt.next != None):
                    if (value < nxt.next.val):
                        newNode = ListNode(value)
                        newNode.next = nxt.next
                        nxt.next = newNode
                        break
                    nxt = nxt.next
                HF = HF.next

            #printList(HD)
            listSize += 1
            if(listSize == 3): #We can't go BCKWRDS, small trick to move back half
                HF = HD.next
            """
            print "Head:", HD.val
            print "HF:", HF.val
            print "TL:", TL.val
            print "List Size:", listSize
            """
            head = head.next #Navigate through list
            
        #printList(HD)
        return HD

myList = ListNode(7)
nodeB = ListNode(4) 
myList.next = nodeB #
nodeC = ListNode(9)
nodeB.next = nodeC  #
nodeD = ListNode(2)
nodeC.next = nodeD  #
nodeE = ListNode(3)
nodeD.next = nodeE  #
nodeF = ListNode(-3)
nodeE.next = nodeF  #

mySol = Solution()
printList(myList, "List before sort")
sortedList = mySol.sortList(myList)
printList(sortedList, "Sorted List")
