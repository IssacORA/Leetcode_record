 >时间上已经尽量减少复杂度，能不能甚至不占用额外空间？
 
 
 
    给定一个整数数组，判断是否存在重复元素。

    如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。   
    class Solution:
        def containsDuplicate(self, nums: List[int]) -> bool:
            if not nums:
                return False
            test=dict()
            for i in nums:
                if i in test:
                    return True
                else:
                    test[i]=1
            return False


