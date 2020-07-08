import random
import numpy


class Quicksort:

    def sortinit(self, a: list):
        self.sortrun(a, 0, (len(a)-1))
        self.li = a

    def sortrun(self, a: list, first: int, last: int):
        if first < last:
            p = self.FrontPartition(first, last, a)
            self.sortrun(a, first, p-1)
            self.sortrun(a, p+1, last)
        
        print(a)
        

    def partition(self, first, last, a):
        pivot = a[last]
        i = first
        
        while j < (last-1):
            if a[j] < pivot:
                a[j], a[i] = a[i], a[j]
                i = i +1
            j = j+1

    def FrontPartition(self, first, last, a):
        pivot = a[first]
        mem = first
        j = first + 1
        while j <= last:
            q = a[j]
            w = a[mem]
            if a[j] < pivot:
                mem = mem+1
                a[j] , a[mem] = a[mem], a[j]
            j = j+1
        
        a[mem], a[first] = a[first], a[mem]

        return mem        

arr = numpy.arange(20)
numpy.random.shuffle(arr)
print(arr)
so = Quicksort()
so.sortinit(list(arr))
print(so.li)
# result = 
