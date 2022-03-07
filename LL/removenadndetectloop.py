class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # code here
        slow=head
        fast=head
        while(slow  and fast  and fast.next):
            slow=slow.next
            fast=fast.next.next
            
            if(slow==fast):
                slow=head
                while(slow.next!=fast.next):
                    fast=fast.next
                    slow=slow.next
                fast.next=None   