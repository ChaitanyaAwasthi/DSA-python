"""
if we want to append a new item to a linked list 
then we can just make the last item 'point' towards the new item and dont O(1)

what if we want to remove an item 
it might seem very simple to just remove the last item and make the tail point towards the prev node 
but no... the tail can't point to the element as there is no random indexing 
but it has to point towards another pointer which leads to the new last node 
so it has to point towards the prev. node to the new last node 
for that the linked list has to iterate over evey node till it reached the goal 
and then the tail node is going to point towards the 2nd last node which then makes it 
point towards the new True last node"""

"""if you want to insert a new item at the start of the list 
then you can just point the new element to the new 2nd node now 
as it was pointed prev by the head variable 
which now makes the new node the head variable O(1)"""


"""removing the first node
we can just say head = head.next which is going to move the variable to the next node 
and then we can remove the first varible 
no of operations = 2, no matter what the operations will be constant"""

"""adding an item in the middle
for example [1,2, 3, 5]
we want to add 4 after 3
what we do is that we iterate through the list till we find 3 
we want 4 to point to 5 to include it 
but rn 3 is pointing towards 5 
so we make 3 point to 4 
and make 4 point to 5
O(n) """


"""in that above example again if I want to remove 4 from the list now
i want 3 to point to 5 now 
so i'll make 3 point to 5 again
and remove 4, O(n)
cause we first have to iterate to find 3"""

"""looking up for an element is O(n) as there is no random  indexing"""
