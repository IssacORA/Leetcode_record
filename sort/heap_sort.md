```
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.heap_sort(nums)
        return nums

    def heap_sort(self,heap):
        self.heap_build(heap)
        for i in range(len(heap)-1,-1,-1):
            
            heap[0],heap[i]=heap[i],heap[0]
            self.MaxHeapfy(heap,0,i)
    
    def heap_build(self,heap):
        for i in range(len(heap)-1,-1,-1):
            self.MaxHeapfy(heap,i,len(heap))
    
    def MaxHeapfy(self,heap,root,heaplen):
        r = root
        while 2*r+1<heaplen:
            left,right =2*r+1,2*r+2
            if right == heaplen or heap[left]>heap[right]:
                mid = left
            else:
                mid = right
            if heap[r] < heap[mid]:
                heap[r],heap[mid] =heap[mid],heap[r]  
                r=mid
            else:
                break
```

- 构建最大堆后，每次将顶部元素与第i个元素交换后将前i个元素构建最大堆
- - 何为最大堆
