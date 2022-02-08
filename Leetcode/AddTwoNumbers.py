#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(self, l1, l2):
    head=ListNode(0)
    curr=head
    carry=0
    while l1 or l2 or carry:
        x=l1.val if l1 else 0
        y=l2.val if l2 else 0
        summ=x+y+carry
        carry=summ//10
        curr.next=ListNode(summ%10)
        curr=curr.next
        if(l1!=None):
            l1=l1.next
        if(l2!=None):
            l2=l2.next
    return head.next
print(addTwoNumbers(addTwoNumbers,[2,4,3],[5,6,4]))