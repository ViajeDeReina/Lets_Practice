class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def add(head, data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)

nodeStart = Node("head starts")
head1 = nodeStart

#input data into each node
for data in range(1,10):
    add(head1, data)

# ADDING NEW NODE IN THE MIDDLE
newNode = Node(1.5)
node = head1

while True:
    if node.data == 1:
        break
    else:
        node = node.next

tmp = node.next
node.next = newNode
newNode.next = tmp

node = head1
while node.next:
    print(node.data)
    node = node.next
print(node.data)