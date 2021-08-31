from linklist import Node
from linklist import LinkedList

ls = LinkedList()
ls.addToHead("5")
ls.addToHead("7")
ls.addToHead("9")
ls.addToHead("4")
ls.addToHead("20")

ls.addNodeAfter("10", "20")

ls.printList()
