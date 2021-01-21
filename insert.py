class adil:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def push(self,new_data):
        new_node= adil(new_data)
        new_node.next=self.head
        self.head=new_node
    #def insert(self,prev_node,new_data):
        #new_node=adil(new_data)
        #new_node.next=prev_node.next
        #prev_node.next=new_node
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
llist=LinkedList()
llist.push(6)
llist.push(5)
llist.push(2)
llist.push(9)
llist.printlist()

