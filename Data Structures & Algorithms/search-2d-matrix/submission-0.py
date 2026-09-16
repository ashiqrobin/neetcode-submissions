class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            arr= matrix[i]
            n = len(arr)
            if target > arr[n-1]:
                continue
            elif target < arr[n-1]:
                s, e = 0, n-1
                return self.searchBinary(s, e, arr, target)
            elif target == arr[n-1]:
                return True
        return False

    def searchBinary(self, s, e, arr, target):
        while s <= e:
            mid = s+(e-s)//2
            if target > arr[mid]:
                return self.searchBinary(mid+1, e, arr, target)
            elif target < arr[mid]:
                return self.searchBinary(s, mid-1, arr, target)
            elif target == arr[mid]:
                return True
        return False

        