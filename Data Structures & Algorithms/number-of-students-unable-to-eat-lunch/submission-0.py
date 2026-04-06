from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)

        count = 0  # number of consecutive rejections

        while students and count < len(students):
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
                count = 0  # reset since someone ate
            else:
                students.append(students.popleft())
                count += 1  # one rejection

        return len(students)



        