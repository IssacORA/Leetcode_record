>Given an array nums of size n, return the majority element.
>
>The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array。

- 摩尔投票法  
超过半数的元素如果聚集在数据结构入口，可以轻松的计算出其超过剩余元素数量之和的部分，因为“身份”已经确认。  
将所有元素打乱，数字差异保持不变，需要做的操作就是“确认身份”  
完全遍历后，优胜者总能胜出，因此只需即时更新“潜在优胜者”的身份。
```class Solution:  
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
        return val
```
        
- 计数方式  
sum(1 for elem in nums if elem == num)   
- 计数式字典  
counts = collections.Counter(nums)  
- 排序后取半数考前的元素  
nums.sort()  
return nums[len(nums)//2]
    
> iterate over 遍历
> recurse 递归
