class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s, e = 0, len(nums)-1
        return self.binary_search(s, e, nums, target)


    
    def binary_search(self, s, e, nums, target) -> int:
        if s > e:
            return -1
        mid = s+(e-s)//2
        if target > nums[mid]:
            return self.binary_search(mid+1, e, nums, target)
        elif target < nums[mid]:
            return self.binary_search(s, mid-1, nums, target)
        else:
            return mid
        
        

             
        