```
import random
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        def partion(low,high):
            mid = random.randint(low,high)
            v = nums[mid] 
            nums[low],nums[mid]=nums[mid],nums[low] 
            i,j = low,low+1
            while j <= high:
                if nums[j] < v:
                    nums[j],nums[i+1] = nums[i+1],nums[j]
                    i+=1
                j+=1
            nums[i],nums[low]=nums[low],nums[i]
            return i
                
        def quick_sort(low,high):
            if low < high:
                mid = partion(low,high)
                quick_sort(low,mid-1) #-1 and +1 is necessary or we cannot apply the sort to 2-element-long array 
                quick_sort(mid+1,high)
```

> Put the middle element to the head first. After the quick pointer(?) goes through the array, all elements left to the slow pointer are
> no bigger than middle element. Then change middle element and element with slow pointer.
