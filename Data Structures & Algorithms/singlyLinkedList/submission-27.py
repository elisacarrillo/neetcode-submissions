class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.linkedList = []
        self.head = None


    
    def get(self, index: int) -> int:
        iteratorNode = self.head
        i = 0
        while (iteratorNode != None) :
            if (i == index) :
                return iteratorNode.data
            i = i + 1
            iteratorNode = iteratorNode.next
        return -1
        
        

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
   
        
        

    def insertTail(self, val: int) -> None:
        if (self.head == None):
            self.head = Node(val)
            return None
        iteratorNode = self.head
        while (iteratorNode != None):
            if (iteratorNode.next == None) :
                new_node = Node(val)
                iteratorNode.next = new_node
                return None
            iteratorNode = iteratorNode.next
        

    def remove(self, index: int) -> bool:
        if (self.head == None):
            return False
        iteratorNode = self.head
        i = 0
        if (iteratorNode.next == None and index == 0):
            self.head = None
            return True

        if (iteratorNode == None and index == 0) :
            self.head = None
            return True

        while (iteratorNode.next != None) :
            if (index == 0):
                to_remove = self.head
                to_remove_next = self.head.next
                self.head = to_remove_next
                return True
            if (i + 1 == index) :
                next_node = iteratorNode.next.next
                curr_node = iteratorNode
                to_remove = iteratorNode.next

                curr_node.next = next_node
                return True

            i = i + 1
            iteratorNode = iteratorNode.next
        
        return False
        

    def getValues(self) -> List[int]:
        iteratorNode = self.head
        arr = []
        while (iteratorNode != None):
            arr.append(iteratorNode.data)
            print(iteratorNode.data)
            iteratorNode = iteratorNode.next
            

        return arr
            
def trythis():
    ll = LinkedList()
    # ll.insertHead(1)
    # ll.insertHead(2)
    ll.insertTail(1)
    ll.insertTail(2)
    print(ll.getValues())

    print(ll.get(1))
    print(ll.getValues())

# trythis()