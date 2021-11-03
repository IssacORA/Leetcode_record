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

- 构建最大堆后，每次将顶部元素与第i个元素交换后将前i-1个元素构建最大堆
- - 何为最大堆？
- - 将列表视作完全二叉树，每个节点元素都比其左右子树更大
- MaxHeapfy函数是算法的核心，用来将某个节点及其左右子树调整为最大堆的形式，在两个过程中使用
- - 一是预构建堆的过程，将节点从数组的末尾遍历到开头
- - 二是置换并修复的过程，最大堆的顶部总是堆中最大的元素，将此元素与倒序指针处的元素交换，再将其之前的元素修复为最大堆，如此反复
