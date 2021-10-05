>Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:

>[4,5,6,7,0,1,4] if it was rotated 4 times.
>[0,1,4,4,5,6,7] if it was rotated 7 times.
>Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

>Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

>You must decrease the overall operation steps as much as possible.

- My solution
```

  def findMin(nums: List[int]) -> int:

      start = nums[0]
      temp = start
      for i in nums:
          if i>= temp:
              temp = i
          else:
              return i
      return start
```

- divide and conquer
```
    def findMin( nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]: left = mid + 1
            elif nums[mid] < nums[right]: right = mid
            else: right = right - 1 # key
        return nums[left]

```
- If R=L+1, (L+R)//2 is always L, so R is alwasy at right side. But L has chance to cross the cliff, 
 because L is updated until it reaches the right side, that the while end condition.
 That situation must be 'M > R' to trigger L update so it must be L=M & R=L+1.
 It means that we can change the while end condition to 'while L!=R'
