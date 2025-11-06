#https://leetcode.com/problems/course-schedule/

#time complexity: O(n+e) where n is the number of nodes and e is the number of edges. kahns algorithm takes up O(n+e), adding courses in queue takes up O(n) and creating adjacency list takes up O(n+e)
#space complexity: O(n+e) where n the number of nodes and e is the number of edges. this is the space taken up by the adjacency list. queue and array take up O(n) space
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        queue = deque()
        graph = defaultdict(list)
        in_degrees = [0] * numCourses

        for course, prerequisite in prerequisites:
            in_degrees[course] += 1
            graph[prerequisite].append(course)

        for i in range(numCourses):
            if in_degrees[i] == 0:
                queue.append(i)
        
        enrolled_courses = 0

        while queue:
            node = queue.popleft()
            enrolled_courses += 1
            for course in graph[node]:
                in_degrees[course] -= 1
                if in_degrees[course] == 0:
                    queue.append(course)

        return enrolled_courses == numCourses
            


        