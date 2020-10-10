import numpy as np
class Node:
    def __dir__(self, val=0 , next=None):
        self.val=val
        self.next=next

class solution1(object):
    def removeNthNode(self, head: Node, n:int):
        dummy=Node(-1)
        dummy.next=head
        slowPrt, fastPtr=dummy , dummy

        while n+1:
            fastPtr=fastPtr.next
            n=n-1
        while fastPtr:
            slowPrt=slowPrt.next
            fastPtr=fastPtr.next
        slowPrt.next=slowPrt.next.next
        return dummy.next

    Node1=Node(1)
    Node2=Node(2)
    Node3=Node(3)
    Node4=Node(4)
    Node5=Node(5)
    head=Node1
    sol=solution1.removeNthNode(head, 2)
    print(sol)


