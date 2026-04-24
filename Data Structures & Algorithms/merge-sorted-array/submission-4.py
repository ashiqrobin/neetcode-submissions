class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = 0
        j = 0

        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                i += 1
            else:
                nums1[i+1:m+1] = nums1[i:m]
                nums1[i] = nums2[j]
                i += 1
                j += 1
                m += 1   # important: valid nums1 length increased

        while j < n:
            nums1[i] = nums2[j]
            i += 1
            j += 1