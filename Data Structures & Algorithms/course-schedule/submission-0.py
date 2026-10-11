class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqMap = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            prereqMap[course].append(prereq)

        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if not prereqMap[course]:
                return True
                
            visited.add(course)
            for pre in prereqMap[course]:
                if not dfs(pre): return False
            visited.remove(course)
            prereqMap[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course): return False
        return True


        