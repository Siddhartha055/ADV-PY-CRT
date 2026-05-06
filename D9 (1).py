#. recourtion 
# used to penerate tree structures and traversing them



def k(a):
    if a<=1:
        return
    i=2
    while a%i!=0:
        i+=1
    print(i,end=" ")
    k(a//i)
k(int(input("Enter a number : ")))

##############################################################################################

# mearge list with constructor and methods

'''
constructors: 
            should be same as class name
            used to initialize instance and class variables
            should be defined

methods: 
            should be defined with df keyword
            used to perform operations
            should be defined with df keyword
            create object with some dimensions

refer---->D8.py line 73 to 160

'''

class rectangle:
    def __init__(self,a,b):
        self.area=a*b

    def display(self):
        print("area of rectangle : ", self.area)
    
rectangle(int(input("Enter the length : ")),int(input("Enter the breadth : "))).display()

##############################################################################################

class circle:
    def __init__(self):
        self.x=int(input("radius : "))
    def display(self):
        print("area : ",3.14*self.x*self.x)

a=int(input("Enter : "))
l=[]
for i in range(a):
    print("\n *---------- ",i+1,"----------*")
    c=circle()
    l.append(c)
    c.display()


##############################################################################################

#linked list refer -------> Data-Structures.md
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
defination for node constructor : 
        when new node created with data it self assigned to the node next isnone
        used to define the structure of node
'''


class linked_list:
    '''
    defination of linked list constructor : 
        when new linked list created it self assigned to the headisnull
        used to define the structure of linked list
    '''
    def __init__(self):
        self.head = None

    # Insert at beginning
    '''
    defination for insert at beginning method : 
        when new node created with data it self assigned to the node next isnone
        used to define the structure of node
    '''
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at end
    '''
    defination for insert at end method : 
        when new node created with data it self assigned to the node next isnone
        used to define the structure of node
    '''
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        
        temp.next = new_node

    # Insert after a given value
    '''
    defination for insert after a given value method : 
        when new node created with data it self assigned to the node next isnone
        used to define the structure of node
    '''
    def insert_after_value(self, target, data):
        temp = self.head

        while temp:
            if temp.data == target:
                new_node = Node(data)
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next

        print("Value not found")

    # Search element
    '''
    defination for search element method : 
        when new node created with data it self assigned to the node next isnone
        used to define the structure of node
    '''
    def search(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                return True
            temp = temp.next
        return False

    # Display list
    '''
    defination for display method : 
        when new node created with data it self assigned to the node next isnone
        used to define the structure of node
    '''
    def display(self):
        temp = self.head
        if temp is None:
            print("List is empty")
            return
        
        while temp:
            print(temp.data, end=" --> ")
            temp = temp.next
        print("None")


# Main program
'''
defination for main program :
        when new main program created it self assigned to the headisnull
        used to define the structure of main program
'''
ll = linked_list()

while True:
    print("\n1.Insert at Beginning")
    print("2.Insert at End")
    print("3.Insert after a value")
    print("4.Search")
    print("5.Display")
    print("6.Exit")

    a = int(input("Enter choice: "))

    if a == 1:
        b = int(input("Enter data: "))
        ll.insert_at_beginning(b)

    elif a == 2:
        b = int(input("Enter data: "))
        ll.insert_at_end(b)

    elif a == 3:
        target = int(input("Insert after which value: "))
        data = int(input("Enter new data: "))
        ll.insert_after_value(target, data)

    elif a == 4:
        b = int(input("Enter data to search: "))
        if ll.search(b):
            print("Element found")
        else:
            print("Element not found")

    elif a == 5:
        ll.display()

    elif a == 6:
        print("Exiting...")
        break

    else:
        print("Invalid input")


##############################################################################################
