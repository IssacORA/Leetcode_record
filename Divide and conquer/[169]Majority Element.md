>Given an array nums of size n, return the majority element.
>
>The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



`class Solution:  
    def majorityElement(self, nums: List[int]) -> int:  
        count=0  
        val = nums[0]  
        for i in nums:  
            if val == i:  
                count+=1
            elif count == 0:
                val,count = i,1
            else:
                count-=1
        return val`
