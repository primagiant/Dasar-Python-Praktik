# Class Node
class Node:
    # inisialisasi Type data node
    def __init__(self, value=None):
        self.value = value
        self.next = None


# Class Likedlist
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Printing semua value dalam linklist
    def printList(self):
        printval = self.head
        while printval is not None:
            print(printval.value)
            printval = printval.next

    # printing value dari head
    def headVal(self):
        print(self.head.value)

    # Printing value dari tail
    def tailVal(self):
        print(self.tail.value)

    # Menambahkan Node di Depan
    def addToHead(self, value):
        tmp = Node(value)
        tmp.next = self.head
        self.head = tmp
        if self.tail is None:
            self.tail = self.head

    # Menambahkan Node di Belakang
    def addToTail(self, value):
        tmp = Node(value)
        if self.head is None:
            self.head = tmp
            self.tail = self.head
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = tmp
        self.tail = last.next

    # Menambahkan Node di Sembarang Tempat
    def addNodeafter(self, value, into):
        # jika into sama dengan head maka lakukan method addToHead
        if into is self.head.value:
            self.addToHead(value)
        # jika into sama dengan tail maka lakukan method addToTail
        if into is self.tail.value:
            self.addToTail(value)
        # jika tidak lakukan hal berikut
        # tmp = Node(value)
        # ref = self.head
        # while(ref.next != into):
        #     ref = ref.next
        # ref.next = tmp
