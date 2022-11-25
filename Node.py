class Node:
    def __init__(self,initdata) -> None:
        self.data = initdata
        self.next = None
    def getDate(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,newdata):
        self.data = newdata
    def setNext(self,newnext):
        self.next = newnext
    
class UnorderreList:
    def __init__(self) -> None:
        self.head = None
    def isEmpty(self):
        return self.head == None
    def create(self,items):
        for i in range(len(items)):
            if self.isEmpty():
                self.head = Node(items[i])
            else:
                node  = Node(items[i])
                cur = self.head
                cur.next = node
                cur = cur.next
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    def length(self):
        current = self.head
        count = 0
        while current != None:
            count = count+1
            current = current.getNext()
        return count
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getDate() ==item:
                found=True
            else:
                current = current.getNext()
        return found
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getDate()==item:
                found=True
            else:
                previous=current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        
    def append(self,item):
        '''
        链表尾部插入元素
        算法实现的步骤为：

        先创建一个值为 item 的链节点 node。
        使用指针 cur 指向链表的头节点 head。
        通过链节点的 next 指针移动 cur 指针，从而遍历链表，直到 cur.next == None。
        令 cur.next 指向将新的链节点 node。
        '''
        node = Node(item)
        if self.isEmpty():
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self,item):
        '''
        链表头部插入元素
        算法实现的步骤为：
        
        先创建一个值为 val 的链节点 node。
        然后将 node 的 next 指针指向链表的头节点 head。
        再将链表的头节点 head 指向 node。
        '''
        node = Node(item)
        node.next = self.head
        self.head = node
    def insertMid(self,index,item):
        '''
        链表中间插入元素
        算法的实现步骤如下：

        使用指针变量 cur 和一个计数器 count。令 cur 指向链表的头节点，count 初始值赋值为 0。
        沿着链节点的 next 指针遍历链表，指针变量 cur 每指向一个链节点，计数器就做一次计数。
        当 count == index - 1 时，说明遍历到了第 index - 1 个链节点，此时停止遍历。
        创建一个值为 val 的链节点 node。
        将 node.next 指向 cur.next。
        然后令 cur.next 指向 node。
        '''
        count = 0
        cur = self.head
        while cur and count < index-1:
            count +=1
            cur = cur.next
        if not cur:
            return 'Error'
        node = Node(item)
        node.next = cur.next
        cur.next = node




mylist = UnorderreList()
mylist.create([1,2,3,4])
mylist.append(98)
print(mylist)
print(mylist.append(56))



