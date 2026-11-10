class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        std::vector<int> inDegree(numCourses, 0);
        std::vector<std::vector<int>> adj(numCourses);

        for (auto& pre : prerequisites) {
            inDegree[pre[1]]++;
            adj[pre[0]].push_back(pre[1]);
        }

        std::queue<int> q;
        for(int i = 0; i < numCourses; i++) {
            if (inDegree[i] == 0) q.push(i);
        }

        int count = 0;
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            count++;

            for (int neighbor : adj[node]) {
                inDegree[neighbor]--;
                if (inDegree[neighbor] == 0) q.push(neighbor);
            } 
        }
        return count == numCourses;
    }
    
};
