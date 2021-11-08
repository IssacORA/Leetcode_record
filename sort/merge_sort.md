```

class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        def sort_update(low, mid, high):
            temp = [0] * (high - low + 1)
            i, j, k = low, mid+1, 0
            while i <= mid and j <= high:
                if nums[i] <= nums[j]:
                    temp[k] = nums[i]
                    i += 1
                else:
                    temp[k] = nums[j]
                    j += 1
                k += 1
            while i <= mid:
                temp[k] = nums[i]
                i += 1
                k += 1
            while j <= high:
                temp[k] = nums[j]
                j += 1
                k += 1
            for i in range(k):
                nums[i + low] = temp[i]
            # print(temp)

        def merge_sort(low, high):
            if low < high:

                mid = (high - low) // 2 +low
                # print(low, mid, high)
                merge_sort(low, mid)
                merge_sort(mid + 1, high)
                sort_update(low, mid, high)

            return nums

        return merge_sort(0, len(nums) - 1)

```
sort_update的作用是，假设手头是两个已经排好序的升序数组，它们的长度相同或相差1，现在将他们合并后排序再更新到nums上。  
利用升序的条件，从左向右比较两个数组的元素，依次将较小的元素添加到temp中。  
但如果相对大小的情况不均匀，会出现提前终止的情况，从而遗漏另一个数组中的元素。  
这时就需要穷尽指针保证涉及所有元素。  
由于跳出的条件是low<high，sort_update中的数组长度至少是2.

We need two functions to deal with it. One for dividing the array half by half and one for sorting each pair at same place. 
We can do these things simultaneously and recursively. 
The merge_sort(low, high) takes two indexs and returns a sorted array.
Every time it splits the array and leaves a task to deal with then complete the task from bottom of structure.
Once one task is completed, we should trust it DOES sort part of array.  
The recursive function: two neighboring ascending array --> one ascending array
