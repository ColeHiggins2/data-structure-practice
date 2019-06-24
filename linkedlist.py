class node:
    def __init__(self, data=None):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head = node()
# iterates through nodes in linked list, when next node is NONE, new node gets inserted as new node
    def append(self, data):
        new_node = node(data)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

#iterates over nodes incrementing total untill last node.
    def length(self):
        current = self.head
        total = 0
        while current.next != None:
            total+=1
            current = current.next
        return total
# display all elements in linked list, loops through nodes, prints elements
    def display(self):
        elements = []
        currnt_node = self.head
        while currnt_node.next!=None:
            currnt_node = currnt_node.next
            elements.append(currnt_node.data)
        print(elements)

# iterate through list to check if current index is same as user index
    def get(self, index):
        if index>=self.length():
            print("Error, 'Get' out of range!")
            return None
        current_index = 0
        currnt_node=self.head
        while True:
            currnt_node=currnt_node.next
            if current_index == index: return currnt_node.data
            current_index+=1

#saving current node as the last node, making sure the next node before the one erased points to the correct node
    def erase(self, index):
        if index>=self.length():
            print("Error, 'Erase' out of range!")
            return None
        current_index = 0
        currnt_node = self.head
        while True:
            last_node = currnt_node
            currnt_node = currnt_node.next
            if current_index == index:
                last_node.next = currnt_node.next
                return

            current_index+=1
# reverse linked list, Time Complexity : O(n) Space Complexity O(1)

    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
'''
    def reverseUtil(self, curr, prev)
        if curr.next is None:
            self.head = curr
            curr.next = prev
            return
        next = curr.next
        curr.next = prev
        self.reverseUtil(next, curr)

    def reverse(self):
        if self.head is None:
            return
        self.reverseUtil(self.head, None)

'''



#Helper code for testing


my_list = linkedlist()

my_list.display()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)


my_list.display()

print(my_list.get(1))

my_list.erase(3)


my_list.display()
my_list.reverse()
my_list.display()
