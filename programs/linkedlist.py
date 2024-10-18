class Node:
    
    data = None
    next_node = None
    previous_node = None

    def __init__(self, data):
        self.data = data


    def __repr__(self):
        return str(self.data)




n1 = Node(10)
print(n1)


n2 = Node(20)
print(n2)

n1.next_node=n2

print(n1.next_node)
print(n2.next_node)


n2.previous_node = n1
print(n2.previous_node)
