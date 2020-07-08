class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.len = k+1
        self.cqueue = [None] * self.len
        self.head = 0
        self.tail =0
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if ((self.tail+1) % self.len) == self.head:
            print("full")
            return False
        else: 
            self.cqueue[self.tail] = value
            self.tail = (self.tail+1) % self.len
        print(self.cqueue)
        return True

        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """

        if self.head == self.tail:
            return False
        else:
            self.cqueue[self.head] = None
            self.head = (self.head+1)% self.len
        print(self.cqueue)
        return True
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.tail == self.head:
            return -1
        else:
            print(self.head)
            print(self.cqueue[self.head])
            return self.cqueue[self.head]
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.tail == self.head:
            return -1
        else:
            print(self.tail)
            print(self.cqueue[self.tail-1])
            return self.cqueue[self.tail-1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if self.tail == self.head:
            return True
        else:
            return False


    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """

        if (self.tail+1) % self.len == self.head:
            print('full')
            return True
        else:
            print('not full')
            return False


new = MyCircularQueue(3)
new.enQueue(1)
new.enQueue(2)
new.enQueue(3)
new.enQueue(4)
new.Rear()
new.isFull()
new.deQueue()
new.enQueue(4)
new.Rear()
new.Front()
