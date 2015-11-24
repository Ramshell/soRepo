from Queue import Queue
import copy


class OwnHeap(object):
    
    # __slots__ = ('list', 'size', 'compareFunc','semaphore')

    
    def __init__(self, semaphore, compareFunc):
        self.list = [None] * 1000
        self.size = 0
        self.compareFunc = compareFunc
        self.semaphore = semaphore
        
    def parent(self, i):
        return (i - 1) // 2  

    def lChild(self, i):
        return 2 * i + 1
    
    def rChild(self, i):
        return 2 * i + 2
    
    
    def get(self):
        """
           getAndRemoveMin : Heap -> Comparable
           getAndRemoveMin removes and returns the minimum element in the heap.
        """
        self.semaphore.acquire()
        res = self.list[0]
        self.size = self.size - 1
        self.list[0] = self.list[self.size]
        self.list[self.size] = None
        self.siftDown(0)
        self.semaphore.release()
        return res
    
    def siftDown(self, startIndex):
        """
           siftDown : Heap * NatNum -> NoneType 
           Move the value at startIndex down to its proper spot in
           the given heap. Assume that the value does not have
           to move up.
        """
        curIndex = startIndex
        a = self.list
        swapIndex = self.first_of_3(curIndex)
        while (swapIndex != curIndex):
            (a[swapIndex], a[curIndex]) = (a[curIndex], a[swapIndex])  # swap
            curIndex = swapIndex
            swapIndex = self.first_of_3(curIndex)
            
            
            
            
    def first_of_3(self, index):
        """
        _first_of_3 : Heap * NatNum -> NatNum 
        _first_of_3 is a private, utility function.
           Look at the values at:
           - index
           - the left child position of index, if in the heap
           - the right child position of index, if in the heap
           and return the index of the value that should come
           first, according to heap.compareFunc().
        """
        lt = self.lChild(index)
        rt = self.rChild(index)
        thisVal = self.list[index]
        if rt < self.size:  # If there are both left and right children
            lVal = self.list[lt]
            rVal = self.list[rt]
            if self.compareFunc(lVal, thisVal)    \
            or self.compareFunc(rVal, thisVal):
                if self.compareFunc(lVal, rVal):
                    return lt  # The left child goes first
                else:
                    return rt  # The right child goes first
            else:
                    return index  # This one goes first
        elif lt < self.size:  # If there is only a left child
            lVal = self.list[lt]
            if self.compareFunc(lVal, thisVal):
                return lt  # The left child goes first
            else:
                return index  # This one goes first
        else:  # There are no children
            return index
        
        
        
        
    def siftUp(self, startIndex):
        """
           siftUp : Heap * NatNum -> NoneType 
           Move the value at startIndex up to its proper spot in
           the given heap. Assume that the value does not have
           to move down.
        """
        i = startIndex
        a = self.list
        while i > 0 and not self.compareFunc(a[self.parent(i)], a[i]):
            (a[self.parent(i)], a[i]) = (a[i], a[self.parent(i)])  # swap
            i = self.parent(i)
            
            
    def put(self, newValue):
        """
           add : Heap * Comparable -> NoneType
           add inserts the element at the correct position in the heap.
        """
        if self.size == len(self.list):
            self.list = self.list + ([None] * len(self.list))

        self.semaphore.acquire()
        self.list[self.size] = newValue
        self.siftUp(self.size)
        self.size = self.size + 1
        self.semaphore.notify()
        self.semaphore.release()
        
    def updateValue(self, index, newValue):
        """
           Fix the heap after changing the value in one of its nodes.
        """
        oldValue = self.list[index]
        self.list[index] = newValue
        if self.compareFunc(newValue, oldValue):
            self.siftUp(index)
        else:
            self.siftDown(index)
            
    def top(self):
        """
           top : Heap -> Comparable
           top returns a deep copy of the current 'top' of the heap
        """
        res = copy.deepcopy(self.list[0])
        return res
    
    def empty(self):
        return self.size == 0
    
    def length(self):
        return self.size
    

class OwnQueue(Queue):
    
    def __init__(self, semaphore):
        self.semaphore = semaphore
        Queue.__init__(self)
        
    
    def put(self, item, block=True, timeout=None):
        self.semaphore.acquire()
        Queue.put(self, item, block=block, timeout=timeout)        
        self.semaphore.notify()
        self.semaphore.release()
    
