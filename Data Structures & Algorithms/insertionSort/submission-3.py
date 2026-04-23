# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        output = []
        output.append(pairs[:])
        if len(pairs) == 0:
            return []
        for i in range(1, len(pairs)):
            current = pairs[i]
            j = i-1
            while j>=0:
                if pairs[j].key > current.key:
                    pairs[j], pairs[j+1] = pairs[j+1], pairs[j]
                    j -=1
                    continue
                else:
                    break
            pairs[j + 1] = current
            output.append(pairs[:])

        
        return output
